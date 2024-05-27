--Generates database hbtn_0d_2

--Creates HBTN
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

--Create SQL user & password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

--Grants privilages
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
