import importlib.util
import subprocess
import sys

for package, module in [("duckdb", "duckdb"), ("matplotlib", "matplotlib")]:
    if importlib.util.find_spec(module) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

import argparse
import duckdb
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from collections import defaultdict

DB_PATH = r'C:\Users\Ben Sylve\Documents\git_sf\sf-pipeline\db\race_analytics.duckdb'

# --- default values (edit these to run without command line args) ---
RACE_ID = "FBWC_JAC_MS"
# ---

parser = argparse.ArgumentParser(description="Plot finish times by year and age group.")
parser.add_argument("race_id", nargs="?", default=RACE_ID, help="Race ID to filter by (e.g. FBWC_JAC_MS)")
args = parser.parse_args()

con = duckdb.connect(DB_PATH, read_only=True)

rows = con.execute("""
    SELECT
        r.race_name,
        YEAR(re.race_date) AS year,
        rr.gender,
        CASE
            WHEN rr.age < 20 THEN '<20'
            WHEN rr.age < 30 THEN '20s'
            WHEN rr.age < 40 THEN '30s'
            WHEN rr.age < 50 THEN '40s'
            WHEN rr.age < 60 THEN '50s'
            ELSE '60+'
        END AS age_group,
        PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY rr.finish_time_seconds) AS p25,
        PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY rr.finish_time_seconds) AS p50,
        PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY rr.finish_time_seconds) AS p75
    FROM silver.race r
    JOIN silver.race_event re ON r.race_id = re.race_id
    JOIN silver.race_results rr ON re.race_event_id = rr.race_event_id
    WHERE r.race_id = ?
      AND rr.finish_time_seconds IS NOT NULL
      AND rr.age IS NOT NULL
      AND rr.gender IN ('M', 'F')
    GROUP BY r.race_name, year, rr.gender, age_group
    ORDER BY year, rr.gender, age_group
""", [args.race_id]).fetchall()

con.close()

if not rows:
    print(f"No data found for race_id: {args.race_id}")
    exit(1)

race_name = rows[0][0]

data = defaultdict(lambda: defaultdict(list))
for _, year, gender, age_group, p25, p50, p75 in rows:
    data[gender][age_group].append((year, p25, p50, p75))

AGE_GROUPS   = ["<20", "20s", "30s", "40s", "50s", "60+"]
GENDER_COLOR = {"M": "#2a9d8f", "F": "#e76f51"}

def fmt_mm_ss(seconds, _pos=None):
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m}:{s:02d}"

def plot_gender(gender, title_label):
    all_years = sorted({r[1] for r in rows if r[2] == gender})
    color = GENDER_COLOR[gender]

    fig, axes = plt.subplots(2, 3, figsize=(13, 7), sharey=True, sharex=True)
    axes_flat = axes.flatten()

    for ax, age_group in zip(axes_flat, AGE_GROUPS):
        pts = sorted(data[gender].get(age_group, []))
        if not pts:
            ax.set_visible(False)
            continue
        years = [p[0] for p in pts]
        p25   = [p[1] for p in pts]
        p50   = [p[2] for p in pts]
        p75   = [p[3] for p in pts]

        ax.fill_between(years, p25, p75, alpha=0.20, color=color)
        ax.plot(years, p50, marker="o", linewidth=2, markersize=5, color=color)

        ax.set_title(age_group, fontweight="bold")
        ax.set_xticks(all_years)
        ax.xaxis.set_tick_params(labelsize=8, rotation=45)
        ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_mm_ss))
        for spine in ["top", "right"]:
            ax.spines[spine].set_visible(False)

    fig.supxlabel("Year", y=0.01)
    fig.supylabel("Finish Time (MM:SS)", x=0.01)
    fig.suptitle(
        f"{race_name} — {title_label} Finish Times by Age Group\n"
        "Shaded band = 25th–75th percentile  |  Line = median",
        fontsize=12
    )
    fig.tight_layout()

plot_gender("M", "Male")
plot_gender("F", "Female")
plt.show()
