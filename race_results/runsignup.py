#!/usr/bin/env python3
"""
Fetches race results from the RunSignUp API for each event in silver.race_event
and writes them to bronze DuckDB tables.

Target table naming convention: bronze.race_results_{data_source_id}__{race_event_id}
Docs: https://runsignup.com/Api/race/:race_id/results/get-results/GET
"""

import requests
import pandas as pd
import duckdb
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class FetchRaceResults:
    """Pulls race results from RunSignUp and loads them into bronze DuckDB tables."""

    def __init__(self, duckdb_path: str, api_key: str, api_secret: str, aflt_token: str):
        self.duckdb_path = duckdb_path
        self.api_key     = api_key
        self.api_secret  = api_secret
        self.aflt_token  = aflt_token

    def run(self):
        """Run the full fetch: pull events from DuckDB, fetch results from API, write to bronze."""
        events = self._get_events()
        logger.info(f"Found {len(events)} event(s)")

        for event in events:
            logger.info(f"Processing {event['race_event_name']} ({event['race_event_id']})")
            results = self._fetch_results(event)
            self._save_to_bronze(event, results)

    def _get_events(self) -> list[dict]:
        """Read race event metadata from silver.race_event to build the fetch list."""
        con = duckdb.connect(self.duckdb_path, read_only=True)
        rows = con.execute("""
            SELECT
                race_event_id,
                race_event_name,
                race_event_data_source_id,
                race_event_metadata_1_key, race_event_metadata_1_value,
                race_event_metadata_2_key, race_event_metadata_2_value,
                race_event_metadata_3_key, race_event_metadata_3_value
            FROM silver.race_event
            ORDER BY race_date
        """).fetchall()
        con.close()

        events = []
        for row in rows:
            meta = {k: v for k, v in [(row[3], row[4]), (row[5], row[6]), (row[7], row[8])] if k is not None}
            # Find the result set key without assuming its name — only RACE_ID and EVENT_ID are fixed
            result_set_key = next((k for k in meta if k not in ("RACE_ID", "EVENT_ID")), None)
            events.append({
                "race_event_id":             row[0],
                "race_event_name":           row[1],
                "race_event_data_source_id": row[2],
                "race_id":                   int(meta["RACE_ID"]),
                "event_id":                  int(meta["EVENT_ID"]),
                "result_set_id":             int(meta[result_set_key]) if result_set_key else None,
            })
        return events

    def _fetch_results(self, event: dict) -> list[dict]:
        """Page through the RunSignUp results API and return all results for the event."""
        url = f"https://runsignup.com/Rest/race/{event['race_id']}/results/get-results"
        all_results = []
        page = 1

        while True:
            params = {
                "api_key":          self.api_key,
                "api_secret":       self.api_secret,
                "aflt_token":       self.aflt_token,
                "format":           "json",
                "event_id":         event["event_id"],
                "page":             page,
                "results_per_page": 250,
            }
            if event["result_set_id"]:
                params["individual_result_set_id"] = event["result_set_id"]

            resp = requests.get(url, params=params)
            resp.raise_for_status()
            data = resp.json()

            page_results = []
            for rs in data.get("individual_results_sets", []):
                page_results.extend(rs.get("results", []))

            if not page_results:
                break

            all_results.extend(page_results)
            logger.info(f"  Page {page}: {len(page_results)} results")
            page += 1

        logger.info(f"  Total: {len(all_results)} results")
        return all_results

    def _save_to_bronze(self, event: dict, results: list[dict]):
        """Write results to a bronze DuckDB table, replacing any existing data."""
        df = pd.DataFrame(results)
        df = df[[c for c in df.columns if not c.startswith("division-")]]
        df["race_event_id"]             = event["race_event_id"]
        df["race_event_data_source_id"] = event["race_event_data_source_id"]

        table = f"bronze.race_results_{event['race_event_data_source_id']}__{event['race_event_id']}"

        con = duckdb.connect(self.duckdb_path)
        try:
            con.execute("CREATE SCHEMA IF NOT EXISTS bronze")
            con.execute(f"CREATE OR REPLACE TABLE {table} AS SELECT * FROM df")
            logger.info(f"Saved to {table}")
        finally:
            con.close()


# ── Standalone execution ──────────────────────────────────────────────────────
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    DUCKDB_PATH = str(Path(r"C:\Users\Ben Sylve\Documents\git_sf\sf-pipeline\db\race_analytics.duckdb"))
    API_KEY     = "TkPIUG2GLK95zjIAONwAyv348fQQ6TtY"
    API_SECRET  = "oNsju6QeN0UEVZ1JK612wyay0dC2jLJ9"
    AFLT_TOKEN  = "uL3LJsNhaU6SFxIRWfJFjA0K24o2fddK"

    FetchRaceResults(DUCKDB_PATH, API_KEY, API_SECRET, AFLT_TOKEN).run()
