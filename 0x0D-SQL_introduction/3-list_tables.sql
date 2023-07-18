-- shows all tables of a database
USE your_database_name;

SELECT TABLE_NAME FROM information_schema.tables
WHERE TABLE_SCHEMA = 'your_database_name'
