# Using Python MySQL connector to execute queries
import mysql.connector

# Creating database object
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'vishwak@05',
    database = 'customer_db'
)

# Creating cursor object
cursorObj = database.cursor()

# Executing queries as per the question and printing the result

print("1. Week-wise Sales based on Customer type")
query1 = """
SELECT year(OrderDate) AS Year, week(OrderDate) AS Week, TypeOfOrder, sum(OrderAmount) AS TotalSales 
FROM orders 
GROUP BY year(OrderDate), week(OrderDate), TypeOfOrder 
ORDER BY Year, Week, TypeOfOrder;
"""
cursorObj.execute(query1)
result1 = cursorObj.fetchall()
print("year, week, order type, total sales")
for year, week, order_type, total_sales in result1:
    print(f"{year}, {week}, {order_type}, ₹{total_sales:,}")

print("\n2. Which state/city presents the highest retail market?")
query2 = """
SELECT a.city, sum(o.OrderAmount) AS RetailSales
FROM address a
JOIN orders o ON a.customerID = o.customerID
WHERE o.TypeOfOrder = 'Retail'
GROUP BY a.city
ORDER BY RetailSales DESC
LIMIT 1;
"""
cursorObj.execute(query2)
result2 = cursorObj.fetchall()
print(f"The City with highest retail market is {result2[0][0]} with ₹{result2[0][1]}")

print("\n3. Which state/city has the lowest wholesale market?")
query3 = """
SELECT a.city, sum(o.OrderAmount) AS WholesaleSales
FROM address a
JOIN orders o ON a.customerID = o.customerID
WHERE o.TypeOfOrder = 'Wholesale'
GROUP BY a.city
ORDER BY WholesaleSales ASC
LIMIT 1;
"""
cursorObj.execute(query3)
result3 = cursorObj.fetchall()
print(f"The City with lowest wholesale market is {result3[0][0]} with ₹{result3[0][1]}")

print("\n4. The date when we did the highest business?")
query4 = """
SELECT OrderDate, sum(OrderAmount) AS TotalSales
FROM orders
GROUP BY OrderDate
ORDER BY TotalSales DESC
LIMIT 1;
"""
cursorObj.execute(query4)
result4 = cursorObj.fetchall()
print(f"The Date we did the highest business is {result4[0][0]} with ₹{result4[0][1]}")

print("\n5. List the unique customer and address along with the total order value.")
query5 = """
SELECT a.customerID, concat(a.FirstName, ' ', a.LastName) as FullName, a.Address, a.City, sum(o.OrderAmount) as TotalOrderValue
FROM address a
JOIN orders o ON a.customerID = o.customerID
GROUP BY a.customerID, FullName, a.Address, a.City;
"""
cursorObj.execute(query5)
result5 = cursorObj.fetchall()
print("Customer ID, FullName, Address, City, Total Order Value")
for cust_id, full_name, address, city, total_order_value in result5:
    print(f"{cust_id}, {full_name}, {address}, {city}, ₹{total_order_value}")

print("\n6. Has the business improved week after week?")
query6 = """
SELECT
    Year,
    Week,
    TotalSales,
    (TotalSales - LAG(TotalSales) OVER (ORDER BY Year, Week)) AS ChangeSale
FROM (
    SELECT
        YEAR(OrderDate) AS Year,
        WEEK(OrderDate) AS Week,
        sum(OrderAmount) AS TotalSales
    FROM orders
    GROUP BY YEAR(OrderDate), WEEK(OrderDate)
) t;
"""
cursorObj.execute(query6)
result6 = cursorObj.fetchall()
print("Year, Week, Total Sales, Change in Sale")
for year, week, total_sales, change_in_sale in result6:
    print(f"{year}, {week}, ₹{total_sales}, ₹{change_in_sale}")

print("\n7. Percentage change in business between each week.")
query7 = """
SELECT
    Year,
    Week,
    TotalSales,
    CASE
        WHEN LAG(TotalSales) OVER (ORDER BY Year, Week) = 0 THEN NULL
        ELSE ROUND(
        (TotalSales - LAG(TotalSales) OVER (ORDER BY Year, Week)) * 100.0 /
        LAG(TotalSales) OVER (ORDER BY Year, Week), 2)
    END AS PercentChange
FROM (
    SELECT
        YEAR(OrderDate) AS Year,
        WEEK(OrderDate) AS Week,
        sum(OrderAmount) AS TotalSales
    FROM orders
    GROUP BY YEAR(OrderDate), WEEK(OrderDate)
) t;
"""
cursorObj.execute(query7)
result7 = cursorObj.fetchall()
print("Year, Week, Total Sales, Percentage of Change")
for year, week, total_sales, percent_change in result7:
    print(f"{year}, {week}, ₹{total_sales}, {percent_change}%")

print("\n8. Percentage change in retail business between each week.")
query8 = """
SELECT
    Year,
    Week,
    RetailSales,
    CASE
        WHEN LAG(RetailSales) OVER (ORDER BY Year, Week) = 0 THEN NULL
        ELSE ROUND(
        (RetailSales - LAG(RetailSales) OVER (ORDER BY Year, Week)) * 100.0 /
        LAG(RetailSales) OVER (ORDER BY Year, Week), 2)
    END AS PercentChange
FROM (
    SELECT
        YEAR(OrderDate) AS Year,
        WEEK(OrderDate) AS Week,
        SUM(OrderAmount) AS RetailSales
    FROM orders
    WHERE TypeOfOrder = 'retail'
    GROUP BY YEAR(OrderDate), WEEK(OrderDate)
) t;
"""
cursorObj.execute(query8)
result8 = cursorObj.fetchall()
print("Year, Week, Retail Sales, Percentage of Change")
for year, week, retail_sales, percent_change in result8:
    print(f"{year}, {week}, ₹{retail_sales}, {percent_change}%")

print("\n9. Percentage change in wholesale business between each week.")
query9 = """
SELECT
    Year,
    Week,
    WholesaleSales,
    CASE
        WHEN LAG(WholesaleSales) OVER (ORDER BY Year, Week) = 0 THEN NULL
        ELSE ROUND(
        (WholesaleSales - LAG(WholesaleSales) OVER (ORDER BY Year, Week)) * 100.0 /
        LAG(WholesaleSales) OVER (ORDER BY Year, Week), 2)
    END AS PercentChange
FROM (
    SELECT
        YEAR(OrderDate) AS Year,
        WEEK(OrderDate) AS Week,
        SUM(OrderAmount) AS WholesaleSales
    FROM orders
    WHERE TypeOfOrder = 'wholesale'
    GROUP BY YEAR(OrderDate), WEEK(OrderDate)
) t;
"""
cursorObj.execute(query9)
result9 = cursorObj.fetchall()
print("Year, Week, Wholesale Sales, Percentage of Change")
for year, week, wholesale_sales, percent_change in result8:
    print(f"{year}, {week}, ₹{wholesale_sales}, {percent_change}%")

print("\n10. The date when we did the lowest business.")
query10 = """
SELECT
    OrderDate,
    SUM(OrderAmount) AS TotalSales
FROM orders
GROUP BY OrderDate
ORDER BY TotalSales ASC
LIMIT 1;
"""
cursorObj.execute(query10)
result10 = cursorObj.fetchall()
print(f"The Date we did the lowest business is {result10[0][0]} with ₹{result10[0][1]}")

# Closing the database object after execution
database.close()