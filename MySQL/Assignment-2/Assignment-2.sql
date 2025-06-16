-- 1. Write a query to calculate the total number of products in the database.
SELECT count(productCode) as TotalProducts
FROM products;

-- 2. Write a query to find the average buy price of all products.
SELECT avg(buyPrice) as AvgProductPrice
FROM products;

-- 3. Write a query to determine the maximum quantity in stock across all products.
SELECT max(quantityInStock) as MaxStockQuantity
FROM products;

-- 4. Write a query to calculate the total sales revenue for each product line.
SELECT p.productLine, sum(od.quantityOrdered * od.priceEach) as totalSalesRevenue
FROM products p
JOIN orderdetails od
ON p.productCode = od.productCode
GROUP BY p.productLine;

-- 5. Write a query to determine the average credit limit for all customers.
SELECT avg(creditLimit) as AvgCreditLimit
FROM customers;

-- 6. Write a query to find the highest payment amount made by a customer.
SELECT max(amount) as MaxPaymentAmount
FROM payments;

-- 7. Write a query to calculate the total quantity ordered for each product.
SELECT productCode, sum(quantityOrdered) as totalQuantityOrders
FROM orderdetails
GROUP BY productCode;

-- 8. Write a query to determine the number of employees in each office.
SELECT officeCode, count(employeeNumber) as employees
FROM employees
GROUP BY officeCode;

-- 9. Write a query to calculate the average price for each order.
SELECT orderNumber, sum(quantityOrdered * priceEach) / sum(quantityOrdered) as avgPrice
FROM orderdetails
GROUP BY orderNumber;

-- 10. Write a query to determine the total sales revenue for each country.
SELECT c.country, sum(od.quantityOrdered * od.priceEach) as totalRevenue
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
GROUP BY c.country;

-- 11. Write a query to calculate the average quantity in stock for each product line.
SELECT productLine, avg(quantityInStock) as avgStock
FROM products
GROUP BY productLine;

-- 12. Write a query to determine the total number of orders placed by each customer.
SELECT customerNumber, count(orderNumber) as totalOrders
FROM orders
GROUP BY customerNumber;

-- 13. Write a query to find the maximum credit limit among all customers.
SELECT max(creditLimit) as maxCreditLimit
FROM customers;

-- 14. Write a query to count the number of offices in each country.
SELECT country, count(officeCode) as totalOffices
FROM offices
GROUP BY country;

-- 15. Write a query to calculate the average payment amount for each customer.
SELECT customerNumber, avg(amount) as avgPayment
FROM payments
GROUP BY customerNumber;

-- 16. Write a query to determine the number of products in each product line.
SELECT productLine, count(productCode) as totalProducts
FROM products
GROUP BY productLine;

-- 17. Write a query to count the number of customers in each state.
SELECT state, count(customerNumber)
FROM customers
WHERE state IS NOT NULL
GROUP BY state;

-- 18. Write a query to find the minimum payment amount among all customers.
SELECT min(amount) as minPaymentAmount
FROM payments;

-- 19. Write a query to calculate the average sales revenue per order.
SELECT avg(orderTotal) as avgRevenuePerOrder
FROM (
	SELECT orderNumber, sum(quantityOrdered * priceEach) as orderTotal
    FROM orderdetails
    GROUP BY orderNumber
) as orderTotals;

-- 20. Write a query to determine the total quantity ordered for each product line.
SELECT p.productLine, sum(od.quantityOrdered) as totalOrders
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
GROUP BY p.productLine;