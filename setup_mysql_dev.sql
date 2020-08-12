-- Project 3 - Script that prepares a MySQL server for project
-- with specified instructions
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- ^^^Creates database and user with specific password here
GRANT ALL PRIVILEGES IN hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
-- ^^^Assign all privileges to hbnb_dev only on hbnb_dev_db
FLUSH PRIVILEGES;
-- ^^^Clears privileges
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
-- ^^^Reassigns privileges to SELECT for hbnb_dev on performance_schema
