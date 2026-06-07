import duckdb

con = duckdb.connect(r'C:\Users\Ben Sylve\Documents\git_sf\sf-pipeline\db\race_analytics.duckdb', read_only=True)

print("=== All Watermelon Races with race_active ===")
rows = con.execute("""
    SELECT r.race_id, r.race_name, r.race_active, re.race_event_id, re.race_date,
           COUNT(rr.result_id) AS finisher_count
    FROM silver.race r
    JOIN silver.race_event re ON r.race_id = re.race_id
    LEFT JOIN silver.race_results rr ON re.race_event_id = rr.race_event_id
    WHERE LOWER(r.race_name) LIKE '%watermelon%'
    GROUP BY r.race_id, r.race_name, r.race_active, re.race_event_id, re.race_date
    ORDER BY re.race_date
""").fetchall()
for row in rows:
    print(row)

print()
print("=== Do WC_2025 and FBWC_2025 share any result_ids? ===")
overlap = con.execute("""
    SELECT COUNT(*) AS overlap_count
    FROM silver.race_results rr1
    JOIN silver.race_results rr2 ON rr1.result_id = rr2.result_id
    WHERE rr1.race_event_id = 'WC_2025' AND rr2.race_event_id = 'FBWC_2025'
""").fetchone()
print("Shared result_ids:", overlap[0])

print()
print("=== Active-only finisher counts by year ===")
rows2 = con.execute("""
    SELECT
        r.race_name,
        r.race_active,
        YEAR(re.race_date) AS year,
        COUNT(rr.result_id) AS finisher_count
    FROM silver.race r
    JOIN silver.race_event re ON r.race_id = re.race_id
    LEFT JOIN silver.race_results rr ON re.race_event_id = rr.race_event_id
    WHERE LOWER(r.race_name) LIKE '%watermelon%'
      AND r.race_active = TRUE
    GROUP BY r.race_name, r.race_active, YEAR(re.race_date)
    ORDER BY YEAR(re.race_date)
""").fetchall()
for row in rows2:
    print(row)

con.close()
