#!/usr/bin/env python3
"""Basic usage examples for AIRE data mining."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from aire.data.accessors import DataAccessor


def main():
    """Demonstrate basic data access."""
    print("=" * 60)
    print("AIRE DATA MINING - BASIC USAGE")
    print("=" * 60)

    # Initialize data accessor
    print("\n1. Initializing data accessor...")
    accessor = DataAccessor()
    print("✅ Connected to Supabase!")

    # Get summary statistics
    print("\n2. Getting summary statistics...")
    summary = accessor.get_summary()
    print(f"\n📊 Data Summary:")
    print(f"  • Incidents: {summary['incidents']['total']}")
    print(f"  • Benchmarks: {summary['benchmarks']['total']}")
    print(f"  • Evaluations: {summary['evals']['total']}")
    print(f"  • Model Versions: {summary['versions']['total']}")
    print(f"  • Epoch Models: {summary['epoch_models']['total']}")

    # Get recent incidents
    print("\n3. Fetching recent incidents...")
    recent_incidents = accessor.incidents.get_recent(limit=3)
    print(f"\n🚨 Recent Incidents:")
    for incident in recent_incidents:
        print(f"\n  • {incident['headline']}")
        print(f"    Date: {incident['reporting_date']}")
        print(f"    Risks: {', '.join(incident.get('risk_cats', []))}")

    # Get benchmarks by risk category
    print("\n4. Finding cyber offense benchmarks...")
    cyber_benchmarks = accessor.benchmarks.get_by_risk_category("Cyber Offense")
    print(f"\n🎯 Cyber Offense Benchmarks ({len(cyber_benchmarks)}):")
    for bench in cyber_benchmarks[:3]:
        print(f"\n  • {bench['benchmark']}")
        print(f"    Publication: {bench['publication']}")
        print(f"    Availability: {bench.get('availability', 'Unknown')}")

    # Get evaluations for a specific model
    print("\n5. Finding evaluations...")
    recent_evals = accessor.evals.get_recent(limit=3)
    print(f"\n📋 Recent Evaluations:")
    for eval_item in recent_evals:
        print(f"\n  • {eval_item['publication']}")
        print(f"    Organization: {', '.join(eval_item.get('organizations', []))}")
        print(f"    Models: {', '.join(eval_item.get('models', [])[:3])}")

    print("\n" + "=" * 60)
    print("✅ Basic usage demonstration complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
