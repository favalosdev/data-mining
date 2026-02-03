#!/usr/bin/env python3
"""Inspect existing Supabase database schema."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aire.data.storage.database import Database
from sqlalchemy import inspect

def main():
    """Inspect and display database schema."""
    print("=" * 60)
    print("SUPABASE SCHEMA INSPECTION")
    print("=" * 60)

    try:
        db = Database()
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()

        print(f"\n📊 Database: {'Supabase PostgreSQL' if db.is_supabase else 'SQLite'}")
        print(f"📊 Tables found: {len(tables)}\n")

        for table in tables:
            print(f"\n{'='*60}")
            print(f"TABLE: {table}")
            print(f"{'='*60}")

            columns = inspector.get_columns(table)
            print(f"\nColumns ({len(columns)}):")
            for col in columns:
                nullable = "NULL" if col.get('nullable') else "NOT NULL"
                default = f" DEFAULT {col.get('default')}" if col.get('default') else ""
                print(f"  • {col['name']:20} {str(col['type']):15} {nullable}{default}")

            # Primary keys
            pk = inspector.get_pk_constraint(table)
            if pk and pk.get('constrained_columns'):
                print(f"\nPrimary Key: {', '.join(pk['constrained_columns'])}")

            # Foreign keys
            fks = inspector.get_foreign_keys(table)
            if fks:
                print(f"\nForeign Keys:")
                for fk in fks:
                    print(f"  • {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}")

            # Indexes
            indexes = inspector.get_indexes(table)
            if indexes:
                print(f"\nIndexes:")
                for idx in indexes:
                    unique = "UNIQUE" if idx.get('unique') else ""
                    print(f"  • {idx['name']}: {', '.join(idx['column_names'])} {unique}")

        print(f"\n{'='*60}")
        print("✅ Schema inspection complete!")
        print(f"{'='*60}\n")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
