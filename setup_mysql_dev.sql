-- Project 3 - Script that prepares a MySQL server for project
-- with specified instructions

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creating database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- ^^^Creates database and user with specific password here
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
-- ^^^Assign all privileges to hbnb_dev only on hbnb_dev_db
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
-- ^^^Clears privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- ^^^Reassigns privileges to SELECT for hbnb_dev on performance_schema
