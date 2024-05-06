-- This script lists all records of second table that have a name



SELECT score, name FROM second_table
HAVING NAME IS NOT NULL
ORDER BY score DESC;
