---
title: Farm Bureau Watermelon Classic
---

# Race Intelligence Report

Historical performance patterns, race-day weather, and what to expect on July 4th in central Mississippi.

```sql summary
SELECT
    COUNT(*)                                                        AS total_finishers,
    ROUND(COUNT(*) * 1.0 / COUNT(DISTINCT race_year))              AS avg_per_year,
    printf('%02d:%02d',
        CAST(FLOOR(MEDIAN(finish_time_seconds) / 60) AS INTEGER),
        CAST(MEDIAN(finish_time_seconds) AS INTEGER) % 60
    )                                                               AS median_finish_time
FROM race_analytics.watermelon_results
```

```sql weather
SELECT
    ROUND(AVG(temp_f))       AS avg_temp_f,
    ROUND(AVG(feels_like_f)) AS avg_feels_like_f
FROM race_analytics.watermelon_weather
```

<BigValue
    data={summary}
    value=total_finishers
    title="Total Finishers (2021–2025)"
    comparison=avg_per_year
    comparisonTitle="avg per year"
    comparisonDelta=false
/>
<BigValue
    data={summary}
    value=median_finish_time
    title="Median Finish Time"
    comparisonTitle="All years combined"
/>
<BigValue
    data={weather}
    value=avg_temp_f
    title="Avg Race-Day Temp"
    fmt='0"°F"'
    comparisonTitle="At 7am gun time"
/>
<BigValue
    data={weather}
    value=avg_feels_like_f
    title="Avg Heat Index"
    fmt='0"°F"'
    comparisonTitle="At 7am gun time"
/>

```sql hist_male
SELECT finish_time_seconds / 60.0 AS finish_minutes
FROM race_analytics.watermelon_results
WHERE race_year = ${inputs.year.value}
  AND gender = 'M'
  AND finish_time_seconds IS NOT NULL
```

```sql hist_female
SELECT finish_time_seconds / 60.0 AS finish_minutes
FROM race_analytics.watermelon_results
WHERE race_year = ${inputs.year.value}
  AND gender = 'F'
  AND finish_time_seconds IS NOT NULL
```

<Histogram data={hist_male} x=finish_minutes title="Male Finish Times" xAxisTitle="Minutes"/>
<Histogram data={hist_female} x=finish_minutes title="Female Finish Times" xAxisTitle="Minutes"/>

```sql box_all_male
SELECT
    CASE
        WHEN age < 20 THEN 'Under 20'
        WHEN age < 30 THEN '20s'
        WHEN age < 40 THEN '30s'
        WHEN age < 50 THEN '40s'
        WHEN age < 60 THEN '50s'
        ELSE '60+'
    END                                                       AS age_group,
    CASE
        WHEN age < 20 THEN 0
        WHEN age < 30 THEN 1
        WHEN age < 40 THEN 2
        WHEN age < 50 THEN 3
        WHEN age < 60 THEN 4
        ELSE 5
    END                                                       AS sort_order,
    MIN(finish_time_seconds / 60.0)                           AS min_time,
    QUANTILE_CONT(finish_time_seconds / 60.0, 0.25)          AS q1,
    MEDIAN(finish_time_seconds / 60.0)                        AS median_time,
    QUANTILE_CONT(finish_time_seconds / 60.0, 0.75)          AS q3,
    MAX(finish_time_seconds / 60.0)                           AS max_time
FROM race_analytics.watermelon_results
WHERE gender = 'M'
  AND finish_time_seconds IS NOT NULL
GROUP BY age_group, sort_order
ORDER BY sort_order
```

```sql box_all_female
SELECT
    CASE
        WHEN age < 20 THEN 'Under 20'
        WHEN age < 30 THEN '20s'
        WHEN age < 40 THEN '30s'
        WHEN age < 50 THEN '40s'
        WHEN age < 60 THEN '50s'
        ELSE '60+'
    END                                                       AS age_group,
    CASE
        WHEN age < 20 THEN 0
        WHEN age < 30 THEN 1
        WHEN age < 40 THEN 2
        WHEN age < 50 THEN 3
        WHEN age < 60 THEN 4
        ELSE 5
    END                                                       AS sort_order,
    MIN(finish_time_seconds / 60.0)                           AS min_time,
    QUANTILE_CONT(finish_time_seconds / 60.0, 0.25)          AS q1,
    MEDIAN(finish_time_seconds / 60.0)                        AS median_time,
    QUANTILE_CONT(finish_time_seconds / 60.0, 0.75)          AS q3,
    MAX(finish_time_seconds / 60.0)                           AS max_time
FROM race_analytics.watermelon_results
WHERE gender = 'F'
  AND finish_time_seconds IS NOT NULL
GROUP BY age_group, sort_order
ORDER BY sort_order
```

<BoxPlot
    data={box_all_male}
    name=age_group
    min=min_time
    intervalBottom=q1
    midpoint=median_time
    intervalTop=q3
    max=max_time
    title="Males — All Years"
    yAxisTitle="Minutes"
/>

<BoxPlot
    data={box_all_female}
    name=age_group
    min=min_time
    intervalBottom=q1
    midpoint=median_time
    intervalTop=q3
    max=max_time
    title="Females — All Years"
    yAxisTitle="Minutes"
/>

```sql weather_trend
SELECT
    CAST(SPLIT_PART(race_event_id, '_', 2) AS INTEGER) AS race_year,
    temp_f,
    feels_like_f
FROM race_analytics.watermelon_weather
WHERE temp_f IS NOT NULL
ORDER BY race_year
```

<LineChart
    data={weather_trend}
    x=race_year
    y=temp_f
    title="Race-Day Temperature at Gun Time (7am)"
    labels=true
    yMin=70
    yGridlines=false
    yAxisLabels=false
/>

---

```sql yearly_stats
SELECT
    race_year,
    COUNT(*)                                               AS finishers,
    COUNT(CASE WHEN gender = 'M' THEN 1 END)              AS males,
    COUNT(CASE WHEN gender = 'F' THEN 1 END)              AS females,
    MIN(finish_time)                                       AS fastest_time,
    MIN(CASE WHEN gender = 'M' THEN finish_time END)      AS fastest_male,
    MIN(CASE WHEN gender = 'F' THEN finish_time END)      AS fastest_female
FROM race_analytics.watermelon_results
GROUP BY race_year
ORDER BY race_year
```

<Dropdown name=year defaultValue=2025>
    <DropdownOption value=2021/>
    <DropdownOption value=2022/>
    <DropdownOption value=2023/>
    <DropdownOption value=2024/>
    <DropdownOption value=2025/>
</Dropdown>

```sql selected_year
SELECT
    COUNT(*)                                               AS finishers,
    COUNT(CASE WHEN gender = 'M' THEN 1 END)              AS males,
    COUNT(CASE WHEN gender = 'F' THEN 1 END)              AS females,
    MIN(finish_time)                                       AS winner,
    MIN(CASE WHEN gender = 'M' THEN finish_time END)      AS top_male,
    MIN(CASE WHEN gender = 'F' THEN finish_time END)      AS top_female
FROM race_analytics.watermelon_results
WHERE race_year = ${inputs.year.value}
```

```sql box_male
SELECT
    CASE
        WHEN age < 20 THEN 'Under 20'
        WHEN age < 30 THEN '20s'
        WHEN age < 40 THEN '30s'
        WHEN age < 50 THEN '40s'
        WHEN age < 60 THEN '50s'
        ELSE '60+'
    END                                                       AS age_group,
    CASE
        WHEN age < 20 THEN 0
        WHEN age < 30 THEN 1
        WHEN age < 40 THEN 2
        WHEN age < 50 THEN 3
        WHEN age < 60 THEN 4
        ELSE 5
    END                                                       AS sort_order,
    MIN(finish_time_seconds / 60.0)                           AS min_time,
    QUANTILE_CONT(finish_time_seconds / 60.0, 0.25)          AS q1,
    MEDIAN(finish_time_seconds / 60.0)                        AS median_time,
    QUANTILE_CONT(finish_time_seconds / 60.0, 0.75)          AS q3,
    MAX(finish_time_seconds / 60.0)                           AS max_time
FROM race_analytics.watermelon_results
WHERE race_year = ${inputs.year.value}
  AND gender = 'M'
  AND finish_time_seconds IS NOT NULL
GROUP BY age_group, sort_order
ORDER BY sort_order
```

```sql box_female
SELECT
    CASE
        WHEN age < 20 THEN 'Under 20'
        WHEN age < 30 THEN '20s'
        WHEN age < 40 THEN '30s'
        WHEN age < 50 THEN '40s'
        WHEN age < 60 THEN '50s'
        ELSE '60+'
    END                                                       AS age_group,
    CASE
        WHEN age < 20 THEN 0
        WHEN age < 30 THEN 1
        WHEN age < 40 THEN 2
        WHEN age < 50 THEN 3
        WHEN age < 60 THEN 4
        ELSE 5
    END                                                       AS sort_order,
    MIN(finish_time_seconds / 60.0)                           AS min_time,
    QUANTILE_CONT(finish_time_seconds / 60.0, 0.25)          AS q1,
    MEDIAN(finish_time_seconds / 60.0)                        AS median_time,
    QUANTILE_CONT(finish_time_seconds / 60.0, 0.75)          AS q3,
    MAX(finish_time_seconds / 60.0)                           AS max_time
FROM race_analytics.watermelon_results
WHERE race_year = ${inputs.year.value}
  AND gender = 'F'
  AND finish_time_seconds IS NOT NULL
GROUP BY age_group, sort_order
ORDER BY sort_order
```

<BigValue data={selected_year} value=finishers   title="Finishers"/>
<BigValue data={selected_year} value=winner       title="Overall Winner"/>
<BigValue data={selected_year} value=top_male     title="Top Male"/>
<BigValue data={selected_year} value=top_female   title="Top Female"/>

## Finishers by Year

<BarChart
    data={yearly_stats}
    x=race_year
    y={['males', 'females']}
    title="Finishers by Gender"
    type=stacked
/>

## Finish Times by Age Group — {inputs.year.value}

<BoxPlot
    data={box_male}
    name=age_group
    min=min_time
    intervalBottom=q1
    midpoint=median_time
    intervalTop=q3
    max=max_time
    title="Males"
    yAxisTitle="Minutes"
/>

<BoxPlot
    data={box_female}
    name=age_group
    min=min_time
    intervalBottom=q1
    midpoint=median_time
    intervalTop=q3
    max=max_time
    title="Females"
    yAxisTitle="Minutes"
/>
