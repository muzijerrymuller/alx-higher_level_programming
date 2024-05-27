-- Creation of table on mysql server
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);

-- Input record values.
INSERT INTO id_not_null (id, name) VALUES (89, 'Best School');

-- Insert record.
INSERT INTO id_not_null (name) VALUES ('Best');
