-- Creating database and table with constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL UNIQUE AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL
);
