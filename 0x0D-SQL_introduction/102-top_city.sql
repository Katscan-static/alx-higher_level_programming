-- get avg_temp for month of July
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month = 7
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
