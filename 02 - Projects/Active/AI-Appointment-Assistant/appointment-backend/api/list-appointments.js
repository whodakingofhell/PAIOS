const { createClient } = require('@supabase/supabase-js');

const supabase = createClient(
  process.env.SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_ANON_KEY
);

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, x-app-api-key');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'GET') return res.status(405).json({ error: 'Method not allowed' });

  try {
    const { date, status } = req.query;

    let query = supabase
      .from('appointments')
      .select('*')
      .order('time_ph', { ascending: true });

    if (date) {
      query = query.gte('time_ph', date + 'T00:00:00+08:00')
                    .lte('time_ph', date + 'T23:59:59+08:00');
    }

    if (status) {
      query = query.eq('status', status);
    } else {
      query = query.eq('status', 'confirmed');
    }

    const { data, error } = await query;
    if (error) throw error;

    return res.status(200).json({
      success: true,
      count: data.length,
      bookings: data
    });

  } catch (err) {
    console.error('Query error:', err);
    return res.status(500).json({ error: 'Internal server error' });
  }
};
