-- shows all tables of a database
SET @database_name := 'mysql';

USE @database_name;

SELECT TABLE_NAME FROM information_schema.tables
WHERE TABLE_SCHEMA = @database_name;
