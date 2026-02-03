"""Database storage using Supabase client for AIRE data mining."""

from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()


class SupabaseDB:
    """Supabase database client for AIRE data mining repository."""

    def __init__(self):
        """Initialize Supabase client."""
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")

        if not self.url or not self.key:
            raise ValueError("Missing SUPABASE_URL or SUPABASE_KEY environment variables")

        self.client: Client = create_client(self.url, self.key)

    @property
    def incidents(self):
        """Access incidents table."""
        return self.client.table("incidents")

    @property
    def benchmarks(self):
        """Access benchmarks table."""
        return self.client.table("benchmarks")

    @property
    def evals(self):
        """Access evals table."""
        return self.client.table("evals")

    @property
    def versions(self):
        """Access versions table."""
        return self.client.table("versions")

    @property
    def epoch_models(self):
        """Access epoch_models table."""
        return self.client.table("epoch_models")
