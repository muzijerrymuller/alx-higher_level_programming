--Generates database hbtn_0d_2

-- Check if the database hbtn_0d_2 exists
SELECT IF(
    EXISTS (
        SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'hbtn_0d_2'
    ),
    'hbtn_0d_2 exists',
    'hbtn_0d_2 doesn’t exist'
) AS db_status;

-- Check if the user user_0d_2 exists
SELECT IF(
    EXISTS (
        SELECT user FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'
    ),
    'user_0d_2 exists',
    'user_0d_2 doesn’t exist'
) AS user_status;

-- Generate database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create SQL user & password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant privileges
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Output message to try to log in with user_0d_2
SELECT 'try to login with user_0d_2' AS message;
