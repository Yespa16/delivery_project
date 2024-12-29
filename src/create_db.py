import psycopg2
from psycopg2 import sql
import json

with open('db_config.json', 'r') as f:
    db_config = json.load(f)

# Extract values from the config dictionary
host = db_config['host']
port = db_config['port']
user = db_config['user']
password = db_config['password']
dbname = db_config['dbname']
# Connect to the PostgreSQL server (default database is 'postgres')
conn = psycopg2.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    dbname=dbname
)
conn.autocommit = True  # Enable autocommit to create the database

# Create a cursor object
cur = conn.cursor()

# SQL query to create a new database
new_db_name = "delivery"
# try:
#   cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name)))
# except:
#   print("HEY!")
# else:
#   print(f"Database '{new_db_name}' created successfully!")

# Close the cursor and connection
cur.close()
conn.close()
