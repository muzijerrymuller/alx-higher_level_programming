--Generates database hbtn_0d_2

--Creates HBTN
CREATE DATABASE hbtn_0d_2 IF NOT EXISTS;

--Create SQL user & password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd' PASSWORD EXPIRE;

--Grants privilages
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost'
