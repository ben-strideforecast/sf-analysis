SELECT
    r.result_id,
    r.race_event_id,
    YEAR(e.race_date)   AS race_year,
    e.race_date::DATE   AS race_date,
    r.first_name,
    r.last_name,
    r.age,
    r.gender,
    r.bib,
    r.finish_time,
    r.finish_time_seconds,
    r.chip_time
FROM silver.race_results r
JOIN silver.race_event e ON r.race_event_id = e.race_event_id
WHERE r.race_event_id LIKE 'FBWC_%'
  AND r.is_active = true
ORDER BY e.race_date, r.finish_time_seconds
