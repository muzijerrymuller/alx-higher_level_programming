-- This creates a table on the my mysql server

-- Create force_name table if it's not already created
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

-- Insert a record into force_name table without providing a name value
INSERT INTO force_name (id) VALUES (333);
