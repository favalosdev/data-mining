#!/usr/bin/env python3
"""Query the actual Supabase schema to see what's really there."""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

def main():
    """Connect to Supabase and inspect actual tables and data."""

    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        print("❌ Missing Supabase credentials")
        return 1

    print("=" * 60)
    print("QUERYING ACTUAL SUPABASE DATABASE")
    print("=" * 60)

    try:
        # Connect using Supabase client
        supabase: Client = create_client(url, key)

        # Known tables from screenshot
        tables = ['incidents', 'benchmarks', 'evals', 'versions', 'epoch_models']

        for table in tables:
            try:
                print(f"\n{'='*60}")
                print(f"TABLE: {table}")
                print(f"{'='*60}")

                # Get a few sample records
                result = supabase.table(table).select("*").limit(3).execute()

                if result.data:
                    print(f"✅ Records found: {len(result.data)}")
                    print(f"\nColumns: {', '.join(result.data[0].keys())}")

                    print(f"\nSample records:")
                    for i, record in enumerate(result.data, 1):
                        print(f"\n  Record {i}:")
                        for key, value in record.items():
                            # Truncate long values
                            val_str = str(value)
                            if len(val_str) > 100:
                                val_str = val_str[:100] + "..."
                            print(f"    {key}: {val_str}")
                else:
                    print(f"⚠️  Table exists but is empty")

            except Exception as e:
                print(f"❌ Error querying {table}: {e}")

        print(f"\n{'='*60}")
        print("Query complete!")
        print(f"{'='*60}")

        return 0

    except Exception as e:
        print(f"\n❌ Error connecting to Supabase: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
