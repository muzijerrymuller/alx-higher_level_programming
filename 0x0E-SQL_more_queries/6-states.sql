-- if it doesnt exist it generates database hbtn_0d_usa.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use database hbtn_0d_usa.
USE hbtn_0d_usa;

-- Generates table.
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert data.
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');
