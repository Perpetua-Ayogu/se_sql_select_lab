
# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd


# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")

employee_data = pd.read_sql(
    "SELECT * FROM employees;",
    conn
)


# STEP 2
# Select employee number and last name
df_first_five = pd.read_sql_query(
    """
    SELECT employeeNumber, lastName
    FROM employees;
    """,
    conn
)


# STEP 3
# Select last name before employee number
df_five_reverse = pd.read_sql_query(
    """
    SELECT lastName, employeeNumber
    FROM employees;
    """,
    conn
)


# STEP 4
# Rename employeeNumber to ID
df_alias = pd.read_sql_query(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees;
    """,
    conn
)


# STEP 5
# Classify employees as executives or not
df_executive = pd.read_sql_query(
    """
    SELECT *,
        CASE
            WHEN jobTitle IN (
                'President',
                'VP Sales',
                'VP Marketing'
            )
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees;
    """,
    conn
)


# STEP 6
# Find the length of each employee's last name
df_name_length = pd.read_sql_query(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees;
    """,
    conn
)


# STEP 7
# Extract the first two characters of each job title
df_short_title = pd.read_sql_query(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
    """,
    conn
)


# STEP 8
# Calculate the sum of rounded order totals
order_details = pd.read_sql(
    "SELECT * FROM orderDetails;",
    conn
)

sum_total_price = pd.read_sql_query(
    """
    SELECT ROUND(priceEach * quantityOrdered, 0) AS total_price
    FROM orderDetails;
    """,
    conn
).sum()


# STEP 9
# Extract day, month and year from the order date
df_day_month_year = pd.read_sql_query(
    """
    SELECT
        orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders;
    """,
    conn
)


# Display results
print("STEP 2:")
print(df_first_five.head())

print("\nSTEP 3:")
print(df_five_reverse.head())

print("\nSTEP 4:")
print(df_alias.head())

print("\nSTEP 5:")
print(df_executive.head())

print("\nSTEP 6:")
print(df_name_length.head())

print("\nSTEP 7:")
print(df_short_title.head())

print("\nSTEP 8:")
print(sum_total_price)

print("\nSTEP 9:")
print(df_day_month_year.head())


# Close the database connection
conn.close()
