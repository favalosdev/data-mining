#!/usr/bin/env python3
"""Examples of specific queries you can run on the AIRE database."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aire.data.accessors import DataAccessor


def main():
    """Demonstrate specific query patterns."""
    print("=" * 60)
    print("AIRE DATA MINING - QUERY EXAMPLES")
    print("=" * 60)

    accessor = DataAccessor()

    # Example 1: Find all manipulation incidents
    print("\n1. Finding manipulation-related incidents...")
    manipulation_incidents = accessor.incidents.get_by_risk_category("Manipulation")
    print(f"   Found {len(manipulation_incidents)} manipulation incidents")
    if manipulation_incidents:
        example = manipulation_incidents[0]
        print(f"   Example: {example['headline'][:80]}...")

    # Example 2: Search for AI-related content
    print("\n2. Searching for 'deepfake' in incidents...")
    deepfake_incidents = accessor.incidents.search_by_keyword("deepfake")
    print(f"   Found {len(deepfake_incidents)} incidents mentioning deepfakes")

    # Example 3: Get open source benchmarks
    print("\n3. Finding open source benchmarks...")
    open_benchmarks = accessor.benchmarks.get_open_source()
    print(f"   Found {len(open_benchmarks)} open source benchmarks")
    for bench in open_benchmarks[:3]:
        print(f"   • {bench['benchmark']}: {bench.get('dataset_link', 'No link')}")

    # Example 4: Get evaluations from specific organization
    print("\n4. Finding Anthropic evaluations...")
    anthropic_evals = accessor.evals.get_by_organization("Anthropic")
    print(f"   Found {len(anthropic_evals)} Anthropic evaluations")
    for eval_item in anthropic_evals:
        print(f"   • {eval_item['publication']}")

    # Example 5: Search model versions
    print("\n5. Searching for GPT models...")
    gpt_versions = accessor.versions.search_by_name("gpt")
    print(f"   Found {len(gpt_versions)} GPT model versions")
    for version in gpt_versions[:5]:
        print(f"   • {version['name']}")

    # Example 6: Get biological risk benchmarks
    print("\n6. Finding biological risk benchmarks...")
    bio_benchmarks = accessor.benchmarks.get_by_risk_category("Biological Risk")
    print(f"   Found {len(bio_benchmarks)} biological risk benchmarks")
    for bench in bio_benchmarks:
        print(f"   • {bench['benchmark']}: {bench['publication'][:60]}...")

    # Example 7: Get evaluations for Claude models
    print("\n7. Finding Claude model evaluations...")
    claude_evals = accessor.evals.get_by_model("Claude Sonnet 4.5")
    print(f"   Found {len(claude_evals)} evaluations for Claude Sonnet 4.5")

    # Example 8: Find Russia-related incidents
    print("\n8. Finding incidents with Russian actors...")
    russia_incidents = accessor.incidents.get_by_actor_origin("Russia")
    print(f"   Found {len(russia_incidents)} incidents with Russian actors")

    # Example 9: Get recent Q4 2025 incidents
    print("\n9. Finding Q4 2025 incidents...")
    q4_incidents = accessor.incidents.get_by_quarter("Q4 2025")
    print(f"   Found {len(q4_incidents)} incidents in Q4 2025")

    # Example 10: Get loss of control evaluations
    print("\n10. Finding loss of control evaluations...")
    loc_evals = accessor.evals.get_by_risk_category("Loss of Control")
    print(f"   Found {len(loc_evals)} loss of control evaluations")
    for eval_item in loc_evals[:3]:
        print(f"   • {eval_item['publication'][:60]}...")

    print("\n" + "=" * 60)
    print("✅ Query examples complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
