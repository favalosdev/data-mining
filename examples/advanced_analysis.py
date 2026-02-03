#!/usr/bin/env python3
"""Advanced analysis examples using AIRE data mining algorithms."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from aire.data.accessors import DataAccessor
from aire.analysis.mining import RiskAnalyzer, SimpleRecommender, DataExporter


def main():
    """Demonstrate advanced data analysis."""
    print("=" * 60)
    print("AIRE DATA MINING - ADVANCED ANALYSIS")
    print("=" * 60)

    # Initialize
    print("\n1. Initializing data accessor and analyzer...")
    accessor = DataAccessor()
    analyzer = RiskAnalyzer(accessor)
    print("✅ Ready!")

    # Analyze incident trends
    print("\n2. Analyzing incident trends...")
    incident_trends = analyzer.analyze_incident_trends()
    print(f"\n🚨 Incident Analysis:")
    print(f"  Total Incidents: {incident_trends['total_incidents']}")
    print(f"\n  Top Risk Categories:")
    for risk, count in list(incident_trends['risk_category_distribution'].items())[:5]:
        print(f"    • {risk}: {count}")
    print(f"\n  Top Actor Origins:")
    for origin, count in list(incident_trends['top_actor_origins'].items())[:5]:
        print(f"    • {origin}: {count}")

    # Analyze benchmark coverage
    print("\n3. Analyzing benchmark coverage...")
    benchmark_coverage = analyzer.analyze_benchmark_coverage()
    print(f"\n🎯 Benchmark Analysis:")
    print(f"  Total Benchmarks: {benchmark_coverage['total_benchmarks']}")
    print(f"  Open Source: {benchmark_coverage['open_source_count']} ({benchmark_coverage['open_source_percentage']:.1f}%)")
    print(f"\n  Risk Category Coverage:")
    for risk, count in list(benchmark_coverage['risk_category_coverage'].items())[:5]:
        print(f"    • {risk}: {count}")

    # Analyze evaluation landscape
    print("\n4. Analyzing evaluation landscape...")
    eval_landscape = analyzer.analyze_evaluation_landscape()
    print(f"\n📋 Evaluation Analysis:")
    print(f"  Total Evaluations: {eval_landscape['total_evaluations']}")
    print(f"  Reviewed: {eval_landscape['reviewed_count']}")
    print(f"\n  Most Evaluated Models:")
    for model, count in list(eval_landscape['most_evaluated_models'].items())[:5]:
        print(f"    • {model}: {count}")

    # Find risk correlations
    print("\n5. Finding risk correlations...")
    correlations = analyzer.find_risk_correlations()
    print(f"\n🔗 Risk Correlations:")
    print(f"\n  Most Covered Risks:")
    for risk, data in correlations['most_covered_risks'][:5]:
        print(f"    • {risk}:")
        print(f"      Incidents: {data['incidents']}, Benchmarks: {data['benchmarks']}, Evals: {data['evaluations']}")

    if correlations['gaps']:
        print(f"\n  Coverage Gaps (high incidents, low benchmarks/evals):")
        for gap in correlations['gaps'][:5]:
            print(f"    • {gap}")

    # Identify emerging risks
    print("\n6. Identifying emerging risks...")
    emerging = analyzer.identify_emerging_risks()
    print(f"\n🆕 Emerging Risks:")
    print(f"  Recent Risk Categories:")
    for risk, count in list(emerging['recent_risk_categories'].items())[:5]:
        print(f"    • {risk}: {count} mentions")

    # Get research recommendations
    print("\n7. Generating research recommendations...")
    recommender = SimpleRecommender(analyzer)
    recommendations = recommender.recommend_research_priorities()
    print(f"\n💡 Research Priorities:")
    for priority in recommendations['research_priorities'][:3]:
        print(f"\n  • {priority['risk_category']} [{priority['priority']}]")
        print(f"    Reason: {priority['reason']}")

    # Export to markdown
    print("\n8. Generating markdown report...")
    analysis_results = {
        "incident_trends": incident_trends,
        "benchmark_coverage": benchmark_coverage,
        "evaluation_landscape": eval_landscape,
        "risk_correlations": correlations,
        "emerging_risks": emerging,
        "recommendations": recommendations
    }

    report = DataExporter.to_markdown_report(analysis_results)
    report_path = Path(__file__).parent.parent / "data" / "analysis_report.md"
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(report)
    print(f"✅ Report saved to: {report_path}")

    print("\n" + "=" * 60)
    print("✅ Advanced analysis complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
