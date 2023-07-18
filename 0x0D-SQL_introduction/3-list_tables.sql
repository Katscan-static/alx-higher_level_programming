-- shows all tables of a database
USE mysql;

SELECT TABLE_NAME FROM information_schema.tables
WHERE TABLE_SCHEMA = 'mysql';
