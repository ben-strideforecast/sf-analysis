"""
GOAT Index leaderboard for the Watermelon Classic 5K (FBWC_JAC_MS).

Age-grading standards come from age_grade_5k_2025.csv, extracted from the
Alan Jones 2025 Road Standards "AgeStanSec" tables
(github.com/AlanLyttonJones/Age-Grade-Tables, "2025 Files" directory).
To refresh for a future year, regenerate that CSV from the updated
maleRoad/femaleRoad xlsx files (AgeStanSec sheet, "5 km" column) and re-run
this script.
"""

from pathlib import Path

import duckdb
import pandas as pd

DB_PATH = r"C:\Users\Ben Sylve\Documents\git_sf\sf-pipeline\db\race_analytics.duckdb"
RACE_ID = "FBWC_JAC_MS"
AGE_GRADE_CSV = Path(__file__).parent / "age_grade_5k_2025.csv"
OUTPUT_CSV = {
    "M": Path(__file__).parent / "goat_leaderboard_male.csv",
    "F": Path(__file__).parent / "goat_leaderboard_female.csv",
}
GENDER_LABEL = {"M": "Male", "F": "Female"}

MIN_APPEARANCES = 2
TOTAL_YEARS = 5

SPEED_WEIGHT = 50
DOMINANCE_WEIGHT = 30
PARTICIPATION_WEIGHT = 20

# first_name/last_name are swapped in the source data, so these pairs are
# (first_name, last_name) as stored in silver.race_results. Each inner list
# is a set of spelling variants for the same runner; the variant with the
# most appearances (ties broken by most recent year) becomes canonical.
NAME_VARIANT_GROUPS = [
    [("Scoggin", "Daniel"), ("Scoggins", "Daniel")],
    [("Hallford", "Evan"), ("Halford", "Evan")],
    [("Marquez", "Armando"), ("Marquz", "Armando")],
    [("Brook", "Antoyne"), ("Brooks", "Antoyne")],
    [("Merk", "Christopher"), ("Merck", "Christopher")],
    [("Izaguiree", "Ana"), ("Izaguirre", "Ana")],
    [("Borthwich", "Jim"), ("Borthwick", "Jim")],
    [("Anderson", "Ashley"), ("Henderson", "Ashley")],
]


def load_results(db_path=DB_PATH, race_id=RACE_ID):
    """Pull one race's results with field_size and finish_position computed per gender."""
    con = duckdb.connect(db_path, read_only=True)
    df = con.execute(
        """
        SELECT
            rr.first_name, rr.last_name, rr.gender, rr.age,
            rr.finish_time_seconds,
            YEAR(re.race_date) AS year,
            re.race_event_id
        FROM silver.race_event re
        JOIN silver.race_results rr ON re.race_event_id = rr.race_event_id
        WHERE re.race_id = ?
          AND rr.finish_time_seconds IS NOT NULL
          AND rr.gender IN ('M', 'F')
          AND rr.age IS NOT NULL
        """,
        [race_id],
    ).df()
    con.close()

    group_keys = ["race_event_id", "gender"]
    df["field_size"] = df.groupby(group_keys)["race_event_id"].transform("size")
    df["finish_position"] = (
        df.groupby(group_keys)["finish_time_seconds"].rank(method="min").astype(int)
    )
    return df


def apply_name_merges(df, variant_groups=NAME_VARIANT_GROUPS):
    """Collapse known spelling variants onto the most-common (first_name, last_name)."""
    variant_to_canonical = {}
    for group in variant_groups:
        best, best_key = None, None
        for variant in group:
            mask = (df["first_name"] == variant[0]) & (df["last_name"] == variant[1])
            n = int(mask.sum())
            last_year = int(df.loc[mask, "year"].max()) if n else -1
            key = (n, last_year)
            if best_key is None or key > best_key:
                best, best_key = variant, key
        for variant in group:
            variant_to_canonical[variant] = best

    keys = list(zip(df["first_name"], df["last_name"]))
    canon = [variant_to_canonical.get(k, k) for k in keys]
    df = df.copy()
    df["first_name"], df["last_name"] = zip(*canon)
    return df


def add_display_name(df):
    """Source first_name/last_name are swapped; build a natural "First Last" name."""
    df = df.copy()
    df["name"] = (df["last_name"] + " " + df["first_name"]).str.strip()
    return df


def load_age_grade_table(path=AGE_GRADE_CSV):
    return pd.read_csv(path)


def add_age_graded_pct(df, age_grade_table):
    table = age_grade_table.rename(columns={"age": "age_lookup"})
    age_min, age_max = table["age_lookup"].min(), table["age_lookup"].max()

    df = df.copy()
    df["age_lookup"] = df["age"].clip(lower=age_min, upper=age_max)
    df = df.merge(table, on=["gender", "age_lookup"], how="left")
    df["age_graded_pct"] = df["standard_seconds_5k"] / df["finish_time_seconds"] * 100
    return df.drop(columns=["age_lookup", "standard_seconds_5k"])


def add_dominance(df):
    df = df.copy()
    df["dominance"] = 1 - (df["finish_position"] - 1) / (df["field_size"] - 1)
    return df


def aggregate_runner_stats(df, min_appearances=MIN_APPEARANCES):
    stats = df.groupby("name").agg(
        appearances=("year", "nunique"),
        avg_age_graded_pct=("age_graded_pct", "mean"),
        avg_finish_position=("finish_position", "mean"),
        avg_finish_time_seconds=("finish_time_seconds", "mean"),
        avg_dominance=("dominance", "mean"),
        std_age_graded_pct=("age_graded_pct", "std"),
        best_age_graded_pct=("age_graded_pct", "max"),
    ).reset_index()

    stats = stats[stats["appearances"] >= min_appearances].copy()
    stats["std_age_graded_pct"] = stats["std_age_graded_pct"].fillna(0)
    return stats


def compute_scores(stats, total_years=TOTAL_YEARS):
    stats = stats.copy()

    top_avg_agp = stats["avg_age_graded_pct"].max()
    stats["speed_score"] = stats["avg_age_graded_pct"] / top_avg_agp * SPEED_WEIGHT

    stats["dominance_score"] = stats["avg_dominance"] * DOMINANCE_WEIGHT

    stats["participation_score"] = (stats["appearances"] / total_years) * PARTICIPATION_WEIGHT

    stats["goat_index"] = (
        stats["speed_score"] + stats["dominance_score"] + stats["participation_score"]
    )
    return stats


def rank_leaderboard(stats):
    return stats.sort_values(
        by=["goat_index", "appearances", "best_age_graded_pct"],
        ascending=[False, False, False],
    ).reset_index(drop=True)


def find_highlights(per_row_df, stats):
    per_row_df = per_row_df.copy()
    per_row_df["dominance_score_single"] = per_row_df["dominance"] * DOMINANCE_WEIGHT

    most_dominant = per_row_df.loc[per_row_df["dominance_score_single"].idxmax()]
    best_single = per_row_df.loc[per_row_df["age_graded_pct"].idxmax()]

    consistent_pool = stats[stats["appearances"] >= 3]
    most_consistent = (
        consistent_pool.loc[consistent_pool["std_age_graded_pct"].idxmin()]
        if not consistent_pool.empty
        else None
    )
    return most_dominant, most_consistent, best_single


OUTPUT_COLS = [
    "name", "appearances", "avg_age_graded_pct", "avg_finish_position",
    "avg_finish_time_seconds", "speed_score", "dominance_score",
    "participation_score", "goat_index",
]


def report_gender(gender, raw_gender):
    label = GENDER_LABEL[gender]

    stats = aggregate_runner_stats(raw_gender)
    stats = compute_scores(stats)
    leaderboard = rank_leaderboard(stats)

    out_path = OUTPUT_CSV[gender]
    leaderboard[OUTPUT_COLS].to_csv(out_path, index=False)
    print(f"Saved {len(leaderboard)} runners to {out_path}\n")

    print(f"=== {label} Top 10 GOAT Index ===")
    print(leaderboard[OUTPUT_COLS].head(10).to_string(index=False, float_format=lambda x: f"{x:.2f}"))

    most_dominant, most_consistent, best_single = find_highlights(raw_gender, stats)
    print(f"\n=== {label} Highlights ===")
    print(
        f"Most Dominant Single Year: {most_dominant['name']} ({most_dominant['year']}) "
        f"- dominance score {most_dominant['dominance_score_single']:.2f}/{DOMINANCE_WEIGHT} "
        f"(finished {most_dominant['finish_position']}/{most_dominant['field_size']})"
    )
    if most_consistent is not None:
        print(
            f"Most Consistent: {most_consistent['name']} "
            f"- stdev age-graded% = {most_consistent['std_age_graded_pct']:.2f} "
            f"over {most_consistent['appearances']} appearances"
        )
    print(
        f"Best Single Age-Graded Performance: {best_single['name']} ({best_single['year']}) "
        f"- {best_single['age_graded_pct']:.2f}%"
    )


def main():
    raw = load_results()
    raw = apply_name_merges(raw)
    raw = add_display_name(raw)

    age_grade_table = load_age_grade_table()
    raw = add_age_graded_pct(raw, age_grade_table)
    raw = add_dominance(raw)

    for gender in ("M", "F"):
        report_gender(gender, raw[raw["gender"] == gender])
        print()


if __name__ == "__main__":
    main()
