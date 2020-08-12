-- Project 3 - Script that prepares a MySQL server for project
-- with specified instructions - TEST
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- ^^^Creates database and user with specific password here
GRANT ALL PRIVILEGES IN hbnb_test_db . * TO 'hbnb_test'@'localhost';
-- ^^^Assign all privileges to hbnb_test only on hbnb_test_db
FLUSH PRIVILEGES;
-- ^^^Clears privileges
GRANT SELECT ON performance_schema . * TO 'hbnb_test'@'localhost';
-- ^^^Reassigns privileges to SELECT for hbnb_test on performance_schema
