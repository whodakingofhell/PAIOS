const { createClient } = require('@supabase/supabase-js');

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY
);

const APP_API_KEY = process.env.APP_API_KEY;
const ALLOWED_ORIGIN = process.env.ALLOWED_ORIGIN || 'https://appointment-backend-one.vercel.app';

const rateLimitMap = new Map();
function checkRateLimit(ip) {
  const now = Date.now();
  const window = 60 * 60 * 1000;
  if (!rateLimitMap.has(ip)) rateLimitMap.set(ip, []);
  const hits = rateLimitMap.get(ip).filter(t => now - t < window);
  rateLimitMap.set(ip, hits);
  if (hits.length >= 5) return false;
  hits.push(now);
  return true;
}

function sanitize(str) {
  if (typeof str !== 'string') return '';
  return str.replace(/<[^>]*>/g, '').replace(/[<>"'&]/g, '').trim().slice(0, 500);
}

async function auditLog(eventType, data) {
  try {
    const { error } = await supabase.from('booking_audit_log').insert({
      event_type: eventType,
      booking_id: data.bookingId || null,
      customer_name: data.name || null,
      customer_email: data.email || null,
      ip_address: data.ip || null,
      details: data.details || null
    });
    if (error) console.error('Audit log failed:', error.message);
  } catch (e) { console.error('Audit log error:', e.message); }
}

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', ALLOWED_ORIGIN);
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, x-app-api-key');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const ip = req.headers['x-forwarded-for'] || req.headers['x-real-ip'] || 'unknown';
  if (!checkRateLimit(ip)) {
    await auditLog('rate_limited', { ip, details: { reason: 'Max 5 bookings per hour' } });
    return res.status(429).json({ error: 'Rate limit exceeded. Max 5 bookings per hour.' });
  }

  if (APP_API_KEY) {
    const providedKey = req.headers['x-app-api-key'];
    if (providedKey !== APP_API_KEY) {
      return res.status(401).json({ error: 'Invalid or missing API key' });
    }
  }

  try {
    const raw = req.body;
    const name = sanitize(raw.name);
    const contact = sanitize(raw.contact);
    const phone = sanitize(raw.phone || '');
    const service = sanitize(raw.service);
    const date = sanitize(raw.date);
    const time = sanitize(raw.time);
    const timezone = sanitize(raw.timezone || 'Asia/Manila');
    const duration = parseInt(raw.duration) || 15;
    const notes = sanitize(raw.notes || '');

    if (!name || !contact || !service) {
      return res.status(400).json({ error: 'Missing required fields: name, contact, service' });
    }
    if (!date || !time) {
      return res.status(400).json({ error: 'Missing required fields: date, time' });
    }
    if (duration < 5 || duration > 20) {
      return res.status(400).json({ error: 'Duration must be between 5 and 20 minutes' });
    }

    const timePH = new Date(date + 'T' + time + ':00+08:00');
    if (isNaN(timePH.getTime())) {
      return res.status(400).json({ error: 'Invalid date or time format' });
    }

    const phHours = timePH.getUTCHours() + 8;
    const phMinutes = timePH.getUTCMinutes();
    const startTotalMin = phHours * 60 + phMinutes;
    const endTotalMin = startTotalMin + duration;

    if (startTotalMin < 540 || endTotalMin > 1080) {
      return res.status(400).json({ error: 'Appointment must be within 9AM-6PM Philippine time' });
    }

    const now = new Date();
    const hoursUntil = (timePH - now) / (1000 * 60 * 60);
    if (hoursUntil < 2) {
      return res.status(400).json({ error: 'Minimum 2 hours notice required' });
    }

    const dayStart = new Date(timePH);
    dayStart.setUTCHours(0, 0, 0, 0);
    const dayEnd = new Date(timePH);
    dayEnd.setUTCHours(23, 59, 59, 999);

    const { count } = await supabase
      .from('appointments')
      .select('*', { count: 'exact', head: true })
      .gte('time_ph', dayStart.toISOString())
      .lte('time_ph', dayEnd.toISOString())
      .eq('status', 'confirmed');

    if (count >= 12) {
      return res.status(400).json({ error: 'Maximum 12 bookings per day reached' });
    }

    const newStart = timePH.getTime();
    const newEnd = newStart + duration * 60000;

    const { data: existing } = await supabase
      .from('appointments')
      .select('time_ph, duration_minutes')
      .eq('status', 'confirmed')
      .gte('time_ph', dayStart.toISOString())
      .lte('time_ph', dayEnd.toISOString());

    if (existing) {
      for (const booking of existing) {
        const existStart = new Date(booking.time_ph).getTime();
        const existEnd = existStart + booking.duration_minutes * 60000;
        if (existStart < newEnd && existEnd > newStart) {
          await auditLog('conflict', { name, email: contact, ip, details: { date, time, duration } });
          return res.status(409).json({ error: 'This time slot overlaps with an existing booking' });
        }
      }
    }

    const { data, error } = await supabase
      .from('appointments')
      .insert({
        name,
        contact,
        service,
        duration_minutes: duration,
        time_ph: timePH.toISOString(),
        time_user_zone: timezone,
        notes: notes || null,
        status: 'confirmed'
      })
      .select()
      .single();

    if (error) {
      if (error.code === '23505') {
        return res.status(409).json({ error: 'This time slot is already booked' });
      }
      throw error;
    }

    await auditLog('booked', { bookingId: data.id, name, email: contact, ip, details: { service, date, time, duration } });

    if (process.env.DISCORD_WEBHOOK_URL) {
      const ref = data.id.slice(0, 8).toUpperCase();
      const discordMsg = {
        content: '**New Booking** `' + ref + '`\n**Name:** ' + name + '\n**Email:** ' + contact + '\n**Phone:** ' + (phone || 'N/A') + '\n**Service:** ' + service + '\n**Date:** ' + date + ' at ' + time + ' (PH Time)\n**Duration:** ' + duration + ' min' + (notes ? '\n**Details:** ' + notes : '')
      };

      try {
        const discordRes = await fetch(process.env.DISCORD_WEBHOOK_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(discordMsg)
        });
        if (!discordRes.ok) {
          console.error('Discord webhook failed:', discordRes.status, await discordRes.text());
        }
      } catch (discordErr) {
        console.error('Discord webhook error:', discordErr.message);
      }
    }

    return res.status(201).json({
      success: true,
      booking: data,
      reference: data.id.slice(0, 8).toUpperCase(),
      message: 'Booked! Ref: ' + data.id.slice(0, 8).toUpperCase() + '. ' + service + ' on ' + date + ' at ' + time + ' (PH Time). ' + duration + ' min.'
    });

  } catch (err) {
    console.error('Booking error:', err);
    return res.status(500).json({ error: 'Internal server error' });
  }
};
