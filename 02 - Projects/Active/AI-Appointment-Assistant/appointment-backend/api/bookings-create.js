module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { name, contact, service, date, time, timezone, duration, notes } = req.body;

    if (!name || !contact || !service || !date || !time) {
      return res.status(400).json({ error: 'Missing required fields: name, contact, service, date, time' });
    }

    if (duration && (duration < 5 || duration > 20)) {
      return res.status(400).json({ error: 'Duration must be between 5 and 20 minutes' });
    }

const { supabase } = require('./lib/supabase');

    const timePH = new Date(`${date}T${time}:00+08:00`);

    const { data, error } = await supabase
      .from('appointments')
      .insert({
        name,
        contact,
        service,
        duration_minutes: duration || 15,
        time_ph: timePH.toISOString(),
        time_user_zone: timezone || 'Asia/Manila',
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

    if (process.env.DISCORD_WEBHOOK_URL) {
      const discordMsg = {
        content: `📅 **New Booking**\n**Name:** ${name}\n**Service:** ${service}\n**Date:** ${date} at ${time} (${timezone || 'PH time'})\n**Duration:** ${duration || 15} min\n**Contact:** ${contact}${notes ? `\n**Notes:** ${notes}` : ''}`
      };

      fetch(process.env.DISCORD_WEBHOOK_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(discordMsg)
      }).catch(() => {});
    }

    return res.status(201).json({
      success: true,
      booking: data,
      message: `Booked! ${service} on ${date} at ${time} (${timezone || 'PH time'}). ${duration || 15} min.`
    });

  } catch (err) {
    console.error('Booking error:', err);
    return res.status(500).json({ error: 'Internal server error' });
  }
};
