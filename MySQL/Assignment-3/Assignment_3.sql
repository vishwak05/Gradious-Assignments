-- 1. Write a query to retrieve the product details for order 10103.
SELECT p.*
FROM orderdetails od
JOIN products p ON od.productCode = p.productCode
WHERE od.orderNumber = 10103;

-- 2. Write a query to get the customer information for order 10127
SELECT c.*
FROM orders o
JOIN customers c ON o.customerNumber = c.customerNumber
WHERE o.orderNumber = 10127;

-- 3. Write a query to retrieve the employee information for customer 166
SELECT e.*
FROM employees e
JOIN customers c ON c.salesRepEmployeeNumber = e.employeeNumber
WHERE c.customerNumber = 166;

-- 4. Write a query to get the official information for office code 4
SELECT *
FROM offices o
WHERE o.officeCode = 4;

-- 5. Write a query to retrieve the product line for each product in an order.
SELECT od.*, p.productLine
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode;

-- 6. Write a query to get the customer information and order status for all orders that contain products belonging to the 'Classic Cars' product line.
SELECT c.*, o.status
FROM products p
JOIN orderdetails od ON p.productCode = od.productCode
JOIN orders o ON od.orderNumber = o.orderNumber
JOIN customers c ON o.customerNumber = c.customerNumber
WHERE p.productLine = 'Classic Cars';

-- 7. Write a query to retrieve the payment details and customer details of customer number 103
SELECT c.*, p.*
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
WHERE c.customerNumber = 103;

-- 8. Write a query to get the orders and their corresponding payments to the same customer.
SELECT o.*, p.checkNumber, p.paymentDate, p.amount
FROM orders o
JOIN payments p ON o.customerNumber = p.customerNumber;

-- 9. Write a query to retrieve the customers and their associated orders.
SELECT *
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber;

-- 10. Write a query to get the products and their corresponding product lines.
SELECT *
FROM products p
JOIN productLines pl ON p.productLine = pl.productLine;

-- 11. Write a query to retrieve the employees and their respective managers.
SELECT *
FROM employees e
JOIN employees es ON e.reportsTo = es.employeeNumber;

-- 12. Write a query to retrieve the customers, their orders, and the corresponding product details.
SELECT *
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode;

-- 13. Write a query to get the payment details, order details, and the associated products.
SELECT *
FROM orders o
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode
JOIN payments py ON o.customerNumber = py.customerNumber;

-- 14. Write a query to retrieve the payment details and the customer information for the check number JM555205
SELECT *
FROM payments p
JOIN customers c ON p.customerNumber = c.customerNumber
WHERE p.checkNumber = 'JM555205';

-- 15. Write a query to retrieve the orders and their corresponding customer and employee information for a canceled status.
SELECT *
FROM orders o
JOIN customers c ON o.customerNumber = c.customerNumber
JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
WHERE o.status = 'Cancelled';

-- 16. Write a query to get the payments, order details, and associated product information for the pavment date 2004-12-17.
SELECT *
FROM payments py
JOIN orders o ON py.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode
WHERE py.paymentDate = '2004-12-17';

-- 17. Write a query to retrieve the products, order details, and corresponding customer information for customer 112
SELECT *
FROM orders o
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode
WHERE o.customerNumber = 112;

-- 18. Write a query to retrieve the customers, their orders, and the associated product line information for the customers who are all from Boston,
SELECT c.*, o.*, od.*, p.productLine
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode
WHERE c.city = 'Boston';

-- 19. Write a query to get the employees, their respective managers, and the corresponding office details of the Sales Rep.
SELECT *
FROM employees e
JOIN employees es ON e.reportsTo = es.employeeNumber
JOIN offices o ON e.officeCode = o.officeCode
WHERE e.jobTitle = 'Sales Rep';

-- 20. Write a query to retrieve the product lines, products, and the corresponding customer information for Vintage Cars.
SELECT *
FROM customers c
JOIN orders o ON c.customerNumber = o.customerNumber
JOIN orderdetails od ON o.orderNumber = od.orderNumber
JOIN products p ON od.productCode = p.productCode
WHERE p.productLine = 'Vintage Cars';