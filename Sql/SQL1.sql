-- To see all Databases
SHOW DATABASES; 

-- To create a new Database
CREATE DATABASE college;
CREATE DATABASE instagram;


-- To select Database 
USE college;
USE instagram;



-- To create table / To create schema
CREATE TABLE student(
name VARCHAR(30),
age INT,
roll_no INT UNIQUE
);

-- Insert values
INSERT INTO student
VALUES
("Aryan",21,2028),
("Nitin",22,2067),
("Sneha",20,2045);

-- To select all data from table 
SELECT * from student;

-- To see all tables
SHOW TABLES;

-- Contrains 
CREATE TABLE users(
id INT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
age INT NOT NULL,
email VARCHAR(50) UNIQUE,
followers INT DEFAULT 0,
following INT DEFAULT 0,
CONSTRAINT CHECK (age >= 18)
);

-- FOREIGN KEY AND PRIMARY KEY 
CREATE TABLE posts(
p_id INT PRIMARY KEY,
content VARCHAR(100) NOT NULL,
user_id INT NOT NULL,
FOREIGN KEY (user_id) REFERENCES users(id)
); 

-- INSERT VALUES
INSERT INTO users
(id,name,age,email,followers,following)
VALUES
(101,"Aryan",21,"aryananair@gmail.com",10,10),
(102,"Sanjay",19,"sanjay@gmail.com",100,105),
(103,"Nitin",20,"nitin@gmail.com",50,100);

INSERT INTO users
(id,name,age,email,followers,following)
VALUES
(104,"Arjan",20,"arjan@gmail.com",20,40),
(105,"Sandhya",24,"sandhya@gmail.com",130,155),
(106,"Nikesh",18,"nikesh@gmail.com",23,142);

-- Select data from table
SELECT id,name,age FROM users;

-- To select unique values from a column
SELECT DISTINCT age FROM users;

-- To select all values
SELECT * FROM users;

INSERT INTO posts
(p_id,content,user_id)
VALUES
(1,"Hello World",103),
(2,"Bye Bye",	102),
(3,"Hello aryan",103);

SELECT * FROM posts;
SELECT * FROM users;

-- CLAUSE (used to specify some conditions)
-- Where clause

SELECT * FROM users WHERE age >= 20;

-- OPERATORS
-- AND 
SELECT * FROM users WHERE id = 102 AND age = 19;

-- OR 
SELECT * FROM users WHERE id = 102 OR age = 20;

-- BETWEEN (TO SPECIFY A RANGE)
SELECT * FROM users WHERE age BETWEEN 20 AND 21;

-- IN
SELECT name, age FROM users WHERE age IN (20,21,24);

-- NOT 
SELECT name, age FROM users WHERE age NOT IN (20,24);

-- LIMIT CLAUSE (To specify limit : how many values to fetch from table)
SELECT * FROM users WHERE age >= 20 LIMIT 2; 

-- ORDER BY CLAUSE (TO SORT ascending (ASC) and decending (DESC))
SELECT * FROM users ORDER BY age ASC;
SELECT * FROM users ORDER BY age DESC;

-- Aggregate functions : predefined function which performs calculation on set of values and return a single value
SELECT MAX(age) FROM users;
SELECT MIN(age) FROM users;
SELECT COUNT(age) FROM users;
SELECT SUM(age) FROM users;
SELECT AVG(age) FROM users;

-- GROUP BY clause : which is used with a aggregate function for grouping
SELECT age , COUNT(age) FROM users GROUP BY age;
SELECT age , max(followers) FROM users GROUP BY age;

-- HAVING clause : To apply condition after grouping . Grouping is necessary
SELECT age , max(followers) FROM users GROUP BY age HAVING age > 20;

-- To prevent error of update query for the first time
SET SQL_SAFE_UPDATES = 0;

-- UPDATE (to update existing rows)
UPDATE users SET followers = 1000 WHERE age = 24;

-- DELETE (to delete existing rows)
DELETE FROM users WHERE age = 24 ;


-- ALTER QUERY (To change Schema)

-- To add column
ALTER TABLE users
ADD COLUMN city VARCHAR(30) NOT NULL DEFAULT "Delhi";

-- To drop column
ALTER TABLE users
DROP COLUMN city;

-- To rename table
ALTER TABLE users
RENAME TO users_info;

-- To change column name
ALTER TABLE users_info
CHANGE COLUMN name full_name VARCHAR(30) NOT NULL;

-- To modify column (datatype / contraint)
ALTER TABLE users_info
MODIFY followers INT DEFAULT 5;

-- TRUNCATE (to delete the data of entire table where drop deletes the complete table)
TRUNCATE TABLE users_info;
