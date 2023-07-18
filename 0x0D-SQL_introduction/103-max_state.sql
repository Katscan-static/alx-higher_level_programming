-- select max values value 
SELECT state, MAX(value) AS max_temp
From temperatures
ORDER BY state;
