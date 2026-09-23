"""
Research Scope AI - SQLite & JSON Response Cache Manager
Prevents rate limits and makes live demos instant.
"""
import sqlite3
import json
import hashlib
import time
from typing import Optional, Dict, Any, List
from config import CACHE_DB_PATH, CACHE_TTL_DAYS

class CacheManager:
    def __init__(self, db_path=CACHE_DB_PATH):
        self.db_path = str(db_path)
        self._init_db()

    def _get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS api_cache (
                    query_hash TEXT PRIMARY KEY,
                    source_api TEXT NOT NULL,
                    query_params TEXT NOT NULL,
                    response_json TEXT NOT NULL,
                    item_count INTEGER DEFAULT 0,
                    created_at REAL NOT NULL,
                    expires_at REAL NOT NULL
                )
            """)
            conn.execute("""
                CREATE INDEX IF NOT EXISTS idx_source_api ON api_cache(source_api)
            """)
            conn.commit()

    @staticmethod
    def hash_key(source_api: str, params: Dict[str, Any]) -> str:
        serialized = json.dumps({"source": source_api, "params": params}, sort_keys=True)
        return hashlib.sha256(serialized.encode("utf-8")).hexdigest()

    def get(self, source_api: str, params: Dict[str, Any]) -> Optional[Any]:
        key = self.hash_key(source_api, params)
        now = time.time()
        with self._get_connection() as conn:
            cursor = conn.execute(
                "SELECT response_json, expires_at FROM api_cache WHERE query_hash = ?",
                (key,)
            )
            row = cursor.fetchone()
            if row:
                if row["expires_at"] > now:
                    try:
                        return json.loads(row["response_json"])
                    except json.JSONDecodeError:
                        return None
                else:
                    # Expired, clean up
                    conn.execute("DELETE FROM api_cache WHERE query_hash = ?", (key,))
                    conn.commit()
        return None

    def set(self, source_api: str, params: Dict[str, Any], data: Any, ttl_days: int = CACHE_TTL_DAYS):
        key = self.hash_key(source_api, params)
        now = time.time()
        expires_at = now + (ttl_days * 86400)
        json_data = json.dumps(data)
        item_count = len(data) if isinstance(data, list) else 1

        with self._get_connection() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO api_cache 
                (query_hash, source_api, query_params, response_json, item_count, created_at, expires_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (key, source_api, json.dumps(params, sort_keys=True), json_data, item_count, now, expires_at))
            conn.commit()

    def get_stats(self) -> Dict[str, Any]:
        with self._get_connection() as conn:
            cursor = conn.execute("SELECT COUNT(*), SUM(item_count) FROM api_cache")
            total_queries, total_items = cursor.fetchone()
            return {
                "cached_queries": total_queries or 0,
                "cached_papers": total_items or 0,
                "db_path": self.db_path
            }

    def clear(self):
        with self._get_connection() as conn:
            conn.execute("DELETE FROM api_cache")
            conn.commit()

# Global default instance
cache = CacheManager()
