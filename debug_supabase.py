#!/usr/bin/env python3
"""Debug script for Supabase connection and schema validation."""

import os
import sys
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

def check_supabase_config():
    """Check Supabase configuration."""
    print("=" * 60)
    print("SUPABASE CONFIGURATION CHECK")
    print("=" * 60)
    
    supabase_url = os.getenv("SUPABASE_URL", "")
    supabase_key = os.getenv("SUPABASE_KEY", "")
    
    print(f"✓ SUPABASE_URL configured: {bool(supabase_url)}")
    if supabase_url:
        print(f"  URL: {supabase_url}")
        # Extract project reference
        try:
            project_ref = supabase_url.split("//")[1].split(".")[0]
            print(f"  Project Ref: {project_ref}")
        except:
            print("  ❌ Invalid URL format")
    
    print(f"✓ SUPABASE_KEY configured: {bool(supabase_key)}")

    if supabase_key:
        print(f"  Key (first 50 chars): {supabase_key[:50]}...")
    
    return supabase_url, supabase_key

def build_connection_string(supabase_url, supabase_key):
    """Build PostgreSQL connection string."""
    print("\n" + "=" * 60)
    print("CONNECTION STRING")
    print("=" * 60)
    
    try:
        project_ref = supabase_url.split("//")[1].split(".")[0]
        db_password = quote(supabase_key, safe="")
        conn_str = f"postgresql://postgres:{db_password}@db.{project_ref}.supabase.co:5432/postgres"
        print(f"✓ Generated connection string:")
        print(f"  postgresql://postgres:[REDACTED]@db.{project_ref}.supabase.co:5432/postgres")
        return conn_str
    except Exception as e:
        print(f"❌ Error building connection string: {e}")
        return None

if __name__ == "__main__":
    supabase_url, supabase_key = check_supabase_config()
    
    if supabase_url and supabase_key:
        conn_str = build_connection_string(supabase_url, supabase_key)