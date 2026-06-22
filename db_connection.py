SUPABASE_URL="https://uqyozmwyjegztzuhunfj.supabase.co"
SUPABASE_KEY="sb_publishable_rBifseQqxOCeZF9kf0aq_A_7cU8DeIQ"

from supabase import create_client

supabase_client_obj=create_client(
    SUPABASE_URL,
    SUPABASE_KEY


)