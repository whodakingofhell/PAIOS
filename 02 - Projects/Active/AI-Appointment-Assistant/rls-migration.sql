-- Supabase RLS Migration — Run in SQL Editor after table creation
-- Security: Enable Row Level Security + audit logging

-- 1. Enable RLS on appointments table
ALTER TABLE appointments ENABLE ROW LEVEL SECURITY;

-- 2. Allow anon INSERT (for booking form — public booking)
CREATE POLICY "Allow public insert" ON appointments
  FOR INSERT
  WITH CHECK (true);

-- 3. Allow anon SELECT (for listing confirmed bookings)
CREATE POLICY "Allow public read confirmed" ON appointments
  FOR SELECT
  USING (status = 'confirmed');

-- 4. Restrict UPDATE to service role only (admin operations)
CREATE POLICY "Service role update only" ON appointments
  FOR UPDATE
  USING (false)
  WITH CHECK (false);

-- 5. Restrict DELETE to service role only (admin operations)
CREATE POLICY "Service role delete only" ON appointments
  FOR DELETE
  USING (false);

-- 6. Create audit log table for booking attempts
CREATE TABLE IF NOT EXISTS booking_audit_log (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type text NOT NULL,
  booking_id uuid,
  customer_name text,
  customer_email text,
  ip_address text,
  details jsonb,
  created_at timestamptz NOT NULL DEFAULT now()
);

-- 7. Index for audit log queries
CREATE INDEX IF NOT EXISTS idx_audit_log_created ON booking_audit_log (created_at);
CREATE INDEX IF NOT EXISTS idx_audit_log_event ON booking_audit_log (event_type);

-- 8. Enable RLS on audit log (service role only)
ALTER TABLE booking_audit_log ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Service role only for audit" ON booking_audit_log
  FOR ALL
  USING (false)
  WITH CHECK (false);
