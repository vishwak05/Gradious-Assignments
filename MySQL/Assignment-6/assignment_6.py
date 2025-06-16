# Using pandasql to perform queries on csv

from pandasql import sqldf
import pandas as pd

# Creating Pandas DataFrame (csv file in same directory)
data = pd.read_csv("transactions.csv")

# 1. Filter records for the year 2023.
print("1. Filtering records for the year of 2023:")
query1 = """
SELECT *
FROM data
WHERE transaction_date LIKE '2023-%'
"""
result1 = sqldf(query1, locals())
print(result1)

# 2. Calculate the total amount spent per customer.
print("\n2. Calculating the total amount spent per customer:")
query2 = """
SELECT customer_id, SUM(amount) AS total_spent
FROM data
WHERE customer_id IS NOT NULL
GROUP BY customer_id
"""
result2 = sqldf(query2, locals())
print(result2)

# 3. Return results sorted by total spending in descending order.
print("\n3. Printing results sorted by total spending in descending order:")
query3 = """
SELECT customer_id, SUM(amount) AS total_spent, transaction_date
FROM data
WHERE customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY total_spent DESC
"""
result3 = sqldf(query3, locals())
print(result3)

# 4. Calculate the average spending per customer for each month in the year 2023.
print("\n4. Calculating average spending per customer for each month in the year 2023:")
query4 = """
SELECT
    customer_id,
    substr(transaction_date, 1, 7) AS year_month,
    AVG(amount) AS avg_monthly_spent
FROM data
WHERE transaction_date LIKE '2023-%'
  AND customer_id IS NOT NULL
GROUP BY customer_id, year_month
ORDER BY customer_id, year_month
"""
result4 = sqldf(query4, locals())
print(result4)

# 5. Identify the customer with the highest total spending and the customer with the lowest total spending.
print("\n5. Identifying customer with highest total spending and customer with lowest total spending:")
query5a = """
SELECT customer_id, SUM(amount) as total_spent
FROM data
WHERE customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 1;
"""
query5b = """
SELECT customer_id, SUM(amount) as total_spent
FROM data
WHERE customer_id IS NOT NULL
GROUP BY customer_id
ORDER BY total_spent ASC
LIMIT 1;
"""
print("The customer with highest spending is:")
result5a = sqldf(query5a, locals())
print(result5a)

print("The customer with lowest spending is:")
result5b = sqldf(query5b, locals())
print(result5b)