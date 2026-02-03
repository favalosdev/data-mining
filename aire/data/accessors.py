"""Data accessor classes for querying Supabase tables."""

from typing import List, Dict, Any, Optional
from datetime import datetime
from .storage.database import SupabaseDB


class IncidentAccessor:
    """Accessor for AI incidents data."""

    def __init__(self, db: SupabaseDB):
        self.db = db

    def get_all(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get all incidents."""
        query = self.db.incidents.select("*")
        if limit:
            query = query.limit(limit)
        return query.execute().data

    def get_by_id(self, incident_id: str) -> Optional[Dict[str, Any]]:
        """Get incident by ID."""
        result = self.db.incidents.select("*").eq("id", incident_id).execute()
        return result.data[0] if result.data else None

    def get_by_risk_category(self, risk_cat: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get incidents by risk category (e.g., 'Manipulation', 'Cyber Offense')."""
        query = self.db.incidents.select("*").contains("risk_cats", [risk_cat])
        if limit:
            query = query.limit(limit)
        return query.execute().data

    def get_by_quarter(self, quarter: str) -> List[Dict[str, Any]]:
        """Get incidents by quarter (e.g., 'Q3 2025')."""
        return self.db.incidents.select("*").eq("quarter", quarter).execute().data

    def get_by_actor_origin(self, origin: str) -> List[Dict[str, Any]]:
        """Get incidents by actor origin country."""
        return self.db.incidents.select("*").contains("actors_origin", [origin]).execute().data

    def search_by_keyword(self, keyword: str) -> List[Dict[str, Any]]:
        """Search incidents by keyword in headline or description."""
        return self.db.incidents.select("*").or_(
            f"headline.ilike.%{keyword}%,description.ilike.%{keyword}%"
        ).execute().data

    def get_recent(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most recent incidents by reporting date."""
        return self.db.incidents.select("*").order("reporting_date", desc=True).limit(limit).execute().data


class BenchmarkAccessor:
    """Accessor for AI risk benchmarks."""

    def __init__(self, db: SupabaseDB):
        self.db = db

    def get_all(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get all benchmarks."""
        query = self.db.benchmarks.select("*")
        if limit:
            query = query.limit(limit)
        return query.execute().data

    def get_by_id(self, benchmark_id: str) -> Optional[Dict[str, Any]]:
        """Get benchmark by ID."""
        result = self.db.benchmarks.select("*").eq("id", benchmark_id).execute()
        return result.data[0] if result.data else None

    def get_by_name(self, benchmark_name: str) -> Optional[Dict[str, Any]]:
        """Get benchmark by name (e.g., 'VCT', 'AttackSeqBench')."""
        result = self.db.benchmarks.select("*").eq("benchmark", benchmark_name).execute()
        return result.data[0] if result.data else None

    def get_by_risk_category(self, risk_cat: str) -> List[Dict[str, Any]]:
        """Get benchmarks by risk category."""
        return self.db.benchmarks.select("*").contains("risk_cats", [risk_cat]).execute().data

    def get_recent(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most recent benchmarks by publication date."""
        return self.db.benchmarks.select("*").order("date", desc=True).limit(limit).execute().data

    def get_open_source(self) -> List[Dict[str, Any]]:
        """Get all open-source benchmarks."""
        return self.db.benchmarks.select("*").eq("availability", "Open").execute().data


class EvalAccessor:
    """Accessor for AI safety evaluations."""

    def __init__(self, db: SupabaseDB):
        self.db = db

    def get_all(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get all evaluations."""
        query = self.db.evals.select("*")
        if limit:
            query = query.limit(limit)
        return query.execute().data

    def get_by_id(self, eval_id: str) -> Optional[Dict[str, Any]]:
        """Get evaluation by ID."""
        result = self.db.evals.select("*").eq("id", eval_id).execute()
        return result.data[0] if result.data else None

    def get_by_public_id(self, public_id: str) -> Optional[Dict[str, Any]]:
        """Get evaluation by public ID (e.g., 'card_claude4.5')."""
        result = self.db.evals.select("*").eq("public_id", public_id).execute()
        return result.data[0] if result.data else None

    def get_by_organization(self, org_name: str) -> List[Dict[str, Any]]:
        """Get evaluations by organization."""
        return self.db.evals.select("*").contains("organizations", [org_name]).execute().data

    def get_by_model(self, model_name: str) -> List[Dict[str, Any]]:
        """Get evaluations for a specific model."""
        return self.db.evals.select("*").contains("models", [model_name]).execute().data

    def get_by_risk_category(self, risk_cat: str) -> List[Dict[str, Any]]:
        """Get evaluations by risk category."""
        return self.db.evals.select("*").contains("risk_cats", [risk_cat]).execute().data

    def get_recent(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most recent evaluations by release date."""
        return self.db.evals.select("*").order("release_date", desc=True).limit(limit).execute().data

    def get_reviewed(self) -> List[Dict[str, Any]]:
        """Get all reviewed evaluations."""
        return self.db.evals.select("*").eq("reviewed", True).execute().data


class VersionAccessor:
    """Accessor for model versions."""

    def __init__(self, db: SupabaseDB):
        self.db = db

    def get_all(self) -> List[Dict[str, Any]]:
        """Get all model versions."""
        return self.db.versions.select("*").execute().data

    def get_by_id(self, version_id: str) -> Optional[Dict[str, Any]]:
        """Get version by ID."""
        result = self.db.versions.select("*").eq("id", version_id).execute()
        return result.data[0] if result.data else None

    def get_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Get version by exact name."""
        result = self.db.versions.select("*").eq("name", name).execute()
        return result.data[0] if result.data else None

    def search_by_name(self, keyword: str) -> List[Dict[str, Any]]:
        """Search versions by keyword in name."""
        return self.db.versions.select("*").ilike("name", f"%{keyword}%").execute().data


class EpochModelsAccessor:
    """Accessor for Epoch AI models data."""

    def __init__(self, db: SupabaseDB):
        self.db = db

    def get_all(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Get all epoch models."""
        query = self.db.epoch_models.select("*")
        if limit:
            query = query.limit(limit)
        return query.execute().data

    def get_by_id(self, model_id: str) -> Optional[Dict[str, Any]]:
        """Get model by ID."""
        result = self.db.epoch_models.select("*").eq("id", model_id).execute()
        return result.data[0] if result.data else None


class DataAccessor:
    """Unified accessor providing access to all AIRE data."""

    def __init__(self, db: Optional[SupabaseDB] = None):
        """Initialize with database connection."""
        self.db = db if db else SupabaseDB()
        self.incidents = IncidentAccessor(self.db)
        self.benchmarks = BenchmarkAccessor(self.db)
        self.evals = EvalAccessor(self.db)
        self.versions = VersionAccessor(self.db)
        self.epoch_models = EpochModelsAccessor(self.db)

    def get_summary(self) -> Dict[str, Any]:
        """Get summary statistics for all data types."""
        return {
            "incidents": {
                "total": len(self.incidents.get_all()),
                "recent": self.incidents.get_recent(5)
            },
            "benchmarks": {
                "total": len(self.benchmarks.get_all()),
                "recent": self.benchmarks.get_recent(5)
            },
            "evals": {
                "total": len(self.evals.get_all()),
                "recent": self.evals.get_recent(5)
            },
            "versions": {
                "total": len(self.versions.get_all())
            },
            "epoch_models": {
                "total": len(self.epoch_models.get_all())
            }
        }
