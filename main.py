"""
============================================================
Lab: Getting Started with Databases and SQL

Course: Python with SQL
Author: Student Name

Description:
This lab demonstrates how to connect to a SQLite database
using Python and retrieve data using SQL queries and Pandas.

The database used in this lab is:
    data.sqlite

The queries below demonstrate:

1. Connecting to a database
2. Selecting specific columns
3. Reordering selected columns
4. Using SQL aliases
5. Using CASE statements
6. Using SQL string functions
7. Using SQL numeric functions
8. Working with dates

============================================================
"""

# ============================================================
# STEP 1A
# Import SQL Library and Pandas
#
# sqlite3:
#     Allows Python to communicate with SQLite databases.
#
# pandas:
#     Allows SQL query results to be loaded into DataFrames.
# ============================================================

import sqlite3
import pandas as pd


# ============================================================
# STEP 1B
# Connect to the database
#
# Create a connection object that will be used throughout
# the lab for executing SQL queries.
# ============================================================

conn = sqlite3.connect("data.sqlite")


# ============================================================
# Display all employee records
#
# This section is provided so you can inspect the data
# contained in the employees table.
# ============================================================

employee_data = pd.read_sql(
    """
    SELECT *
    FROM employees;
    """,
    conn,
)

print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")


# ============================================================
# STEP 2
#
# Retrieve only:
#   - employeeNumber
#   - lastName
#
# from the employees table.
# ============================================================

df_first_five = pd.read_sql(
    """
    SELECT
        employeeNumber,
        lastName
    FROM employees;
    """,
    conn,
)


# ============================================================
# STEP 3
#
# Retrieve the same columns as Step 2 but reverse
# their order.
# ============================================================

df_five_reverse = pd.read_sql(
    """
    SELECT
        lastName,
        employeeNumber
    FROM employees;
    """,
    conn,
)


# ============================================================
# STEP 4
#
# Rename employeeNumber using an SQL alias.
#
# employeeNumber -> ID
# ============================================================

df_alias = pd.read_sql(
    """
    SELECT
        lastName,
        employeeNumber AS ID
    FROM employees;
    """,
    conn,
)


# ============================================================
# STEP 5
#
# Categorize employees based on their job title.
#
# Executive:
#     President
#     VP Sales
#     VP Marketing
#
# Everyone else:
#     Not Executive
#
# The new column should be named:
#     role
# ============================================================

df_executive = pd.read_sql(
    """
    SELECT
        employeeNumber,
        lastName,
        jobTitle,

        CASE
            WHEN jobTitle = 'President'
                 OR jobTitle = 'VP Sales'
                 OR jobTitle = 'VP Marketing'
            THEN 'Executive'

            ELSE 'Not Executive'

        END AS role

    FROM employees;
    """,
    conn,
)


# ============================================================
# STEP 6
#
# Determine the length of every employee's last name.
#
# Return only one column named:
#     name_length
# ============================================================

df_name_length = pd.read_sql(
    """
    SELECT
        LENGTH(lastName) AS name_length
    FROM employees;
    """,
    conn,
)


# ============================================================
# STEP 7
#
# Return only the first two letters
# of every employee's job title.
#
# The new column should be named:
#     short_title
# ============================================================

df_short_title = pd.read_sql(
    """
    SELECT
        SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
    """,
    conn,
)


# ============================================================
# Display Order Details
#
# This table is used for the remaining exercises.
# ============================================================

order_details = pd.read_sql(
    """
    SELECT *
    FROM orderDetails;
    """,
    conn,
)

print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")


# ============================================================
# STEP 8
#
# Calculate:
#
# Rounded(priceEach * quantityOrdered)
#
# for every order.
#
# Then compute the grand total.
# ============================================================

sum_total_price = pd.read_sql(
    """
    SELECT
        ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderDetails;
    """,
    conn,
).sum()


## ============================================================
# STEP 9
#
# Return the original order date together with the
# day, month and year.
#
# The order date exists in the orders table, so we
# join it with orderDetails using orderNumber.
# ============================================================

df_day_month_year = pd.read_sql("""
SELECT
    orders.orderDate,

    STRFTIME('%d', orders.orderDate) AS day,

    STRFTIME('%m', orders.orderDate) AS month,

    STRFTIME('%Y', orders.orderDate) AS year

FROM orders

INNER JOIN orderDetails

ON orders.orderNumber = orderDetails.orderNumber;
""", conn)


# ============================================================
# Close the database connection
#
# Always close the connection once all SQL queries
# have completed.
# ============================================================

conn.close()