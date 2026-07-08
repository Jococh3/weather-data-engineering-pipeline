-- Show all rows loaded into the DataFrame.

SELECT *
FROM weather_daily;

-- Count forecast rows by city
SELECT
    city,
    COUNT(*) AS forecast_days
FROM weather_daily
GROUP BY city;

-- Average forecasted tempoerature by city.
SELECT
    city,
    round(AVG(max_temp_f), 1) AS avg_max_temp_f,
    round(AVG(min_temp_f), 1) AS avg_min_temp_f
FROM weather_daily
GROUP BY city
ORDER by avg_max_temp_f DESC;

-- Warmest forecasted day across all cities.
SELECT
    city,
    weather_date,
    max_temp_f
FROM weather_daily
ORDER BY max_temp_f DESC
LIMIT 1;

-- Total precipitation forecasted by city.
SELECT
    city,
    round(SUM(precipitation_mm), 2) AS total_precipitation_mm
FROM weather_daily
GROUP BY city
ORDER BY total_precipitation_mm DESC;