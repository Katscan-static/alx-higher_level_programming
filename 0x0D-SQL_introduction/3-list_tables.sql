-- shows all tables of a database
USE mysql;

SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE'
    AND TABLE_SCHEMA = DATABASE();
