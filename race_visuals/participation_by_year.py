import importlib.util
import subprocess
import sys

for package, module in [("duckdb", "duckdb"), ("matplotlib", "matplotlib")]:
    if importlib.util.find_spec(module) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import argparse
import duckdb
import matplotlib.pyplot as plt

DB_PATH = r'C:\Users\Ben Sylve\Documents\git_sf\sf-pipeline\db\race_analytics.duckdb'

# --- default values (edit these to run without command line args) ---
RACE_ID = "FBWC_JAC_MS"
# ---

parser = argparse.ArgumentParser(description="Plot annual participation for a race.")
parser.add_argument("race_id", nargs="?", default=RACE_ID, help="Race ID to filter by (e.g. FBWC_JAC_MS)")
args = parser.parse_args()

con = duckdb.connect(DB_PATH, read_only=True)

rows = con.execute("""
    SELECT
        r.race_name,
        YEAR(re.race_date) AS year,
        COUNT(rr.result_id) AS finishers
    FROM silver.race r
    JOIN silver.race_event re ON r.race_id = re.race_id
    LEFT JOIN silver.race_results rr ON re.race_event_id = rr.race_event_id
    WHERE r.race_id = ?
    GROUP BY r.race_name, YEAR(re.race_date)
    ORDER BY year
""", [args.race_id]).fetchall()

con.close()

if not rows:
    print(f"No data found for race_id: {args.race_id}")
    exit(1)

race_name = rows[0][0]
years = [r[1] for r in rows]
finishers = [r[2] for r in rows]

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(years, finishers, marker="o", linewidth=2, markersize=7)

for x, y in zip(years, finishers):
    ax.annotate(str(y), (x, y), textcoords="offset points", xytext=(0, 10), ha="center")

ax.set_title(f"{race_name} — Annual Runner Participation")
ax.set_xlabel("Year")
ax.set_ylabel("Participants")
ax.set_xticks(years)
data_range = max(finishers) - min(finishers)
padding = data_range * 0.25
ax.set_ylim(min(finishers) - padding, max(finishers) + padding)

for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)

plt.tight_layout()
plt.show()
