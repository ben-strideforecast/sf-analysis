WITH ranked AS (
    SELECT
        race_event_id,
        hour,
        temp_f,
        feels_like_f,
        ROW_NUMBER() OVER (
            PARTITION BY race_event_id
            ORDER BY ABS(EPOCH(TRY_CAST(hour AS TIME)) - EPOCH(TIME '07:00:00'))
        ) AS rn
    FROM silver.race_weather_hourly
    WHERE race_event_id LIKE 'FBWC_%'
      AND is_active = true
)
SELECT
    race_event_id,
    hour,
    temp_f,
    feels_like_f
FROM ranked
WHERE rn = 1
