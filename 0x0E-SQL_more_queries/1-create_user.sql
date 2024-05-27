--Creates MYSQL server user 'user_id_1'
-- Ensure 'user_0d_1' on localhost exists with password 'user_0d_1_pwd'; create if missing.
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
-- Provide 'user_0d_1'@'localhost' full access to all databases and update privilege tables.
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'localhost'
   IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
