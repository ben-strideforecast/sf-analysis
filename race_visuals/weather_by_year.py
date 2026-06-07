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

parser = argparse.ArgumentParser(description="Plot race-start temperature and humidity by year.")
parser.add_argument("race_id", nargs="?", default=RACE_ID, help="Race ID to filter by (e.g. FBWC_JAC_MS)")
args = parser.parse_args()

con = duckdb.connect(DB_PATH, read_only=True)

rows = con.execute("""
    SELECT
        r.race_name,
        YEAR(re.race_date) AS year,
        w.temp_f,
        w.humidity_pct
    FROM silver.race r
    JOIN silver.race_event re ON r.race_id = re.race_id
    JOIN silver.race_weather_hourly w ON re.race_event_id = w.race_event_id
        AND w.hour = LEFT(re.race_start_hour, 2) || ':00:00'
    WHERE r.race_id = ?
    ORDER BY year
""", [args.race_id]).fetchall()

con.close()

if not rows:
    print(f"No data found for race_id: {args.race_id}")
    exit(1)

race_name = rows[0][0]
years = [r[1] for r in rows]
temps = [r[2] for r in rows]
humidities = [r[3] for r in rows]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharey=False)

color_temp = "#d62728"
color_hum = "#1f77b4"

ax1.plot(years, temps, marker="o", linewidth=2, markersize=7, color=color_temp)
for x, y in zip(years, temps):
    ax1.annotate(f"{y:.0f}°", (x, y), textcoords="offset points", xytext=(0, 10), ha="center", color=color_temp)
ax1.set_ylabel("Temperature (°F)")
ax1.set_xlabel("Year")
ax1.set_xticks(years)
temp_range = max(temps) - min(temps)
temp_pad = max(temp_range * 0.3, 3)
ax1.set_ylim(min(temps) - temp_pad, max(temps) + temp_pad)
ax1.set_title("Temperature (°F)")
for spine in ["top", "right"]:
    ax1.spines[spine].set_visible(False)

ax2.plot(years, humidities, marker="s", linewidth=2, markersize=7, color=color_hum)
for x, y in zip(years, humidities):
    ax2.annotate(f"{y:.0f}%", (x, y), textcoords="offset points", xytext=(0, 10), ha="center", color=color_hum)
ax2.set_ylabel("Humidity (%)")
ax2.set_xlabel("Year")
ax2.set_xticks(years)
hum_range = max(humidities) - min(humidities)
hum_pad = max(hum_range * 0.3, 3)
ax2.set_ylim(min(humidities) - hum_pad, max(humidities) + hum_pad)
ax2.set_title("Humidity (%)")
for spine in ["top", "right"]:
    ax2.spines[spine].set_visible(False)

fig.suptitle(f"{race_name} — Race-Start Weather by Year")

plt.tight_layout()
plt.show()
