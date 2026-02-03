#!/usr/bin/env python3
"""Setup script to initialize the database schema in Supabase."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from aire.data.storage.database import Database, Base
from aire.config.settings import Settings

def main():
    """Initialize database schema."""
    print("=" * 60)
    print("DATABASE SETUP")
    print("=" * 60)

    try:
        # Initialize database connection
        print("\n1. Connecting to database...")
        db = Database()

        # Create all tables
        print("\n2. Creating database schema...")
        Base.metadata.create_all(db.engine)
        print("✅ Schema created successfully!")

        # Verify tables
        print("\n3. Verifying tables...")
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()

        print(f"\n📊 Found {len(tables)} tables:")
        for table in tables:
            columns = inspector.get_columns(table)
            print(f"  - {table} ({len(columns)} columns)")
            for col in columns:
                print(f"    • {col['name']}: {col['type']}")

        print("\n✅ Database setup complete!")
        return 0

    except Exception as e:
        print(f"\n❌ Error during setup: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
