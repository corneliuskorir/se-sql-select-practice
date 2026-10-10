import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")

# return all products in product table
product_data = pd.read_sql(
    """
SELECT *
  FROM products;
""",
    conn,
).columns
# print(product_data)

# return name and code columns
prod_name_and_code = pd.read_sql(
    """ SELECT productCode, productName 
    FROM products;""",
    conn,
).tail(5)

# print(prod_name_and_code)
## switch order
prod_name_and_code = pd.read_sql(
    """ SELECT productName, productCode 
    FROM products;""",
    conn,
).tail(5)

# print(prod_name_and_code)

# select and use case
planes = pd.read_sql(
    """
SELECT productName, productLine ,
  CASE productLine
    WHEN "Planes" THEN "Planes"
    ELSE "Not Planes"
    END AS planes
FROM products;""",
    conn,
)
# print(planes)

# length of product description of each product

disc_len = pd.read_sql(
    """
SELECT length(productDescription) AS description_length
FROM products;""",
    conn,
).head(5)
# print(disc_len)

# change product vendor to all caps

caps_vendor = pd.read_sql(
    """
SELECT upper(productVendor) AS caps_vendor 
FROM products;""",
    conn,
).head(5)

# print(caps_vendor)

# product name to lower
lower_name = pd.read_sql(
    """
SELECT lower(productName) AS lower_name 
FROM products;""",
    conn,
).head(5)

# print(lower_name)

scales = pd.read_sql(
    """
SELECT substr(productScale,3,3) AS scales 
FROM products;""",
    conn,
)

# print(scales)

# full name column

full_name = pd.read_sql(
    """
SELECT productVendor || " " || productName AS fullName 
FROM products;""",
    conn,
)

# print(full_name)

round_diff = pd.read_sql(
    """
SELECT CAST(round(MSRP - buyPrice) AS INTEGER) AS round_diff 
FROM products;""",
    conn,
)

print(round_diff)

conn.close()
