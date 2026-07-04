-- TO CHECK THE STATE OF AUTOCOMMIT
SELECT @@autocommit;

-- TO DISABLE AUTOCOMMIT
SET autocommit = 0;

-- TO ENABLE AUTOCOMMIT
SET autocommit = 1;

-- CREATING DATABASE FOR TRANSACTION

CREATE DATABASE bank;
USE bank;

CREATE TABLE accounts(
id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
balance DECIMAL(10,2)
);

INSERT INTO accounts
(name,balance)
VALUES
("aryan",10000.00),
("sneha",12000.00),
("nitin",10000.00);


SELECT * FROM accounts;

-- TO DO A TRANSACTION (SET OF OPERATIONS)

START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;

COMMIT;


-- ROLLBACK (UNDO ONLY UNCOMMITED CHANGES)

START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;

ROLLBACK;

-- COMMITED CHANGES ARE NOT UNDO 

START TRANSACTION;

UPDATE accounts SET balance = balance - 500 WHERE id = 1;
COMMIT;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;
ROLLBACK;


-- SAVEPOINT 

START TRANSACTION;

UPDATE accounts SET balance = balance + 1000 WHERE id = 1;
SAVEPOINT after_wallet_topup;

UPDATE accounts SET balance = balance + 10 WHERE id = 1;
ROLLBACK TO after_wallet_topup;

COMMIT;


-- JOINS IN SQL

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);

INSERT INTO customers VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount INT
);

INSERT INTO orders VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700); 


SELECT * FROM customers;
SELECT * FROM orders;

-- INNER JOIN
SELECT *
FROM customers c 
INNER JOIN orders o
ON c.customer_id = o.customer_id;


-- OUTER JOIN
 
-- LEFT JOIN
SELECT * 
FROM customers c 
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

-- RIGHT JOIN
SELECT *
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id;


-- OUTER JOIN
SELECT * 
FROM customers c 
LEFT JOIN orders o
ON c.customer_id = o.customer_id
UNION
SELECT *
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id;

-- CROSS JOIN
SELECT * 
FROM customers
CROSS JOIN orders;

-- SELF JOIN
SELECT *
FROM customers AS A
JOIN customers AS B
ON A.customer_id = B.customer_id;


-- LEFT EXCLUSIVE JOIN
SELECT * 
FROM customers AS A
LEFT JOIN orders AS B
ON A.customer_id = B.customer_id
WHERE B.customer_id IS NULL;

-- RIGHT EXCLUSIVE JOIN 
SELECT * 
FROM customers AS A
RIGHT JOIN orders AS B
ON A.customer_id = B.customer_id
WHERE A.customer_id IS NULL;