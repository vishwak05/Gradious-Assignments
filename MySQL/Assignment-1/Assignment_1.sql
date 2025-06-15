-- 1. Write the query to get only the product Code and product name from the products table.
SELECT productCode, productName 
FROM products;

-- 2. Write the query to arrange the customer details based on the country name in descending order.
SELECT *
FROM customers
ORDER BY country DESC;

-- 3. Write the query to find the order number, order date, and status for the customers having comments about shipment.
SELECT orderNumber, orderDate, status
FROM orders
WHERE comments IS NOT NULL;

-- 4. Write the query to find the customer who has made the highest payment along with the payment date.
SELECT *
FROM payments
ORDER BY amount DESC
LIMIT 1;

-- 5. I have a list of the top five customers who made the highest payment and write a query to find the next top five customers who made the highest payment.
SELECT *
FROM payments
ORDER BY amount DESC
LIMIT 5 OFFSET 5;

-- 6. Write the query to find the customer details whose credit limit is between 10,000 to 1,00,000.
SELECT *
FROM customers
WHERE creditLimit BETWEEN 10000 AND 100000;

-- 7. Write the query to get the Employee number, lastname, and first name from the employees' table whose last name starts with 'B'.
SELECT employeeNumber, lastName, firstName
FROM employees
WHERE lastName LIKE "B%";

-- 8. write a query to select the order whose total amount is greater than 50,000.
SELECT o.*
FROM orders o
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY o.orderNumber
HAVING SUM(od.quantityOrdered * od.priceEach) > 50000;


-- 9. Write the query to find the productcode, product name & text description from the tables products and product lines.
SELECT p.productCode, p.productName, pl.textDescription
FROM products p JOIN productlines pl
ON p.productLine = pl.productLine;

-- 10. Write the query to get the customer number, customer name, order number, status from the tables order, payments, and customers who have no order.
SELECT c.customerNumber, c.customerName, o.orderNumber, o.status
FROM customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber
WHERE o.orderNumber IS NULL;