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
import matplotlib.patches as mpatches
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

AGE_GROUPS = ["<20", "20s", "30s", "40s", "50s", "60+"]
COLORS     = ["#9467bd", "#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#7f7f7f"]

def fmt_mm_ss(seconds, _pos=None):
    m = int(seconds) // 60
    s = int(seconds) % 60
    return f"{m}:{s:02d}"

YEAR_COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

def plot_gender(gender, title_label):
    fig, ax = plt.subplots(figsize=(13, 6))

    all_years = sorted({r[1] for r in rows if r[2] == gender})
    n_years = len(all_years)
    box_w = 0.12
    slot  = box_w + 0.025
    group_gap = 1.1
    group_pos = {g: i * group_gap for i, g in enumerate(AGE_GROUPS)}
    year_pos  = {y: i for i, y in enumerate(all_years)}
    offsets   = [(j - (n_years - 1) / 2) * slot for j in range(n_years)]

    all_p25, all_p75 = [], []

    for yi, (year, color) in enumerate(zip(all_years, YEAR_COLORS)):
        for age_group in AGE_GROUPS:
            pts = [p for p in data[gender].get(age_group, []) if p[0] == year]
            if not pts:
                continue
            _, p25, p50, p75 = pts[0]
            cx = group_pos[age_group] + offsets[yi]
            x0 = cx - box_w / 2
            rect = mpatches.Rectangle(
                (x0, p25), box_w, p75 - p25,
                facecolor=color, edgecolor="none", alpha=0.80
            )
            ax.add_patch(rect)
            ax.plot([x0, x0 + box_w], [p50, p50], color="white", linewidth=1.8, solid_capstyle="butt")
            ax.text(cx, (p25 + p75) / 2, f"'{str(year)[2:]}",
                    ha="center", va="center", rotation=90,
                    fontsize=6.5, color="white", fontweight="bold")
            all_p25.append(p25)
            all_p75.append(p75)

    y_pad = (max(all_p75) - min(all_p25)) * 0.06
    ax.set_ylim(min(all_p25) - y_pad, max(all_p75) + y_pad)
    ax.set_xlim(-group_gap * 0.55, (len(AGE_GROUPS) - 1) * group_gap + group_gap * 0.55)

    ax.set_xticks([group_pos[g] for g in AGE_GROUPS])
    ax.set_xticklabels(AGE_GROUPS)
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_mm_ss))
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Finish Time (MM:SS)")
    ax.set_title(
        f"{race_name} — {title_label} Finish Times by Age Group\n"
        "Box = 25th–75th percentile  |  Line = median"
    )

    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    fig.tight_layout()

plot_gender("M", "Male")
plt.show()
