import pandas as pd
import duckdb
import mysql.connector
from mysql.connector import errorcode

# MySQL connection details
MYSQL_CONFIG = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost'
}
DB_NAME = 'headlines'
TABLE_NAME = 'headlines'
CSV_FILE = 'abcnews-date-text.csv'

# 1. Load CSV into pandas DataFrame
print('Loading CSV...')
df = pd.read_csv(CSV_FILE)
# Ensure correct column names
df = df.rename(columns={'publish_date': 'publish_date', 'headline_text': 'headline_text'})

# 2. Load into DuckDB
duckdb_file = 'headlines.duckdb'
print('Loading into DuckDB...')
con_duck = duckdb.connect(duckdb_file)
con_duck.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
con_duck.execute(f"CREATE TABLE {TABLE_NAME} (publish_date INTEGER, headline_text TEXT)")
con_duck.execute(f"INSERT INTO {TABLE_NAME} SELECT * FROM df")
con_duck.close()
print('DuckDB load complete.')

# 3. Load into MySQL
print('Connecting to MySQL...')
conn = mysql.connector.connect(**MYSQL_CONFIG)
cursor = conn.cursor()

# Create database if not exists
try:
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    print(f"Database '{DB_NAME}' ensured.")
except mysql.connector.Error as err:
    print(f"Failed creating database: {err}")
    exit(1)

# Use the database
cursor.execute(f"USE {DB_NAME}")

# Drop and create table
cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
cursor.execute(f"""
    CREATE TABLE {TABLE_NAME} (
        publish_date INT,
        headline_text TEXT
    )
""")
print(f"Table '{TABLE_NAME}' created.")

# Insert data in batches
print('Inserting data into MySQL (this may take a while)...')
BATCH_SIZE = 1000
rows = list(df.itertuples(index=False, name=None))
for i in range(0, len(rows), BATCH_SIZE):
    batch = rows[i:i+BATCH_SIZE]
    cursor.executemany(
        f"INSERT INTO {TABLE_NAME} (publish_date, headline_text) VALUES (%s, %s)",
        batch
    )
    conn.commit()
    print(f"Inserted {i+len(batch)} / {len(rows)} rows", end='\r')

print(f"\nMySQL load complete.")
cursor.close()
conn.close()
print('All done!') 