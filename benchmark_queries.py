import time
import duckdb
import mysql.connector
import pandas as pd
import re

# MySQL connection details
MYSQL_CONFIG = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'headlines'
}
TABLE_NAME = 'headlines'
DUCKDB_FILE = 'headlines.duckdb'

# Helper for timing
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start

# 1. Number of headlines per year
QUERY_YEAR = f'''
SELECT CAST(publish_date / 10000 AS SIGNED) AS y, COUNT(*) AS headlines_number
FROM {TABLE_NAME}
GROUP BY y
ORDER BY y;
'''

# 2. Headlines containing the word 'war'
QUERY_WAR = f'''
SELECT * FROM {TABLE_NAME}
WHERE headline_text LIKE '%war%';
'''

# 3. Total number of headlines
QUERY_TOTAL = f'SELECT COUNT(*) FROM {TABLE_NAME};'

# 4. Longest headline
QUERY_LONGEST = f'''
SELECT headline_text, LENGTH(headline_text) AS len
FROM {TABLE_NAME}
ORDER BY len DESC
LIMIT 1;
'''

# Connect to DuckDB
con_duck = duckdb.connect(DUCKDB_FILE)

# Connect to MySQL
conn_mysql = mysql.connector.connect(**MYSQL_CONFIG)
cursor_mysql = conn_mysql.cursor()

def run_query_duckdb(query, desc):
    with Timer() as t:
        result = con_duck.execute(query).fetchdf()
    print(f"[DuckDB] {desc} (Time: {t.interval:.4f}s)")
    print(result.head(5))
    print()
    return result, t.interval

def run_query_mysql(query, desc):
    with Timer() as t:
        cursor_mysql.execute(query)
        result = cursor_mysql.fetchall()
        columns = cursor_mysql.column_names
        df = pd.DataFrame(result, columns=columns)
    print(f"[MySQL] {desc} (Time: {t.interval:.4f}s)")
    print(df.head(5))
    print()
    return df, t.interval

print("\n--- Number of headlines per year ---")
run_query_duckdb(QUERY_YEAR, "Headlines per year")
run_query_mysql(QUERY_YEAR, "Headlines per year")

print("\n--- Headlines containing 'war' ---")
run_query_duckdb(QUERY_WAR, "Headlines containing 'war'")
run_query_mysql(QUERY_WAR, "Headlines containing 'war'")

print("\n--- Total number of headlines ---")
run_query_duckdb(QUERY_TOTAL, "Total number of headlines")
run_query_mysql(QUERY_TOTAL, "Total number of headlines")

print("\n--- Longest headline ---")
run_query_duckdb(QUERY_LONGEST, "Longest headline")
run_query_mysql(QUERY_LONGEST, "Longest headline")

# 5. Top 10 most common words in all headlines
print("\n--- Top 10 most common words ---")
# For this, fetch all headlines and process in Python for both DBs

def get_top_words_from_df(df, text_col='headline_text', topn=10):
    words = []
    for text in df[text_col]:
        words += re.findall(r'\b\w+\b', str(text).lower())
    return pd.Series(words).value_counts().head(topn)

# DuckDB
with Timer() as t:
    headlines_duck = con_duck.execute(f"SELECT headline_text FROM {TABLE_NAME}").fetchdf()
    top_words_duck = get_top_words_from_df(headlines_duck)
print(f"[DuckDB] Top 10 words (Time: {t.interval:.4f}s)")
print(top_words_duck)
print()

# MySQL
with Timer() as t:
    cursor_mysql.execute(f"SELECT headline_text FROM {TABLE_NAME}")
    headlines_mysql = pd.DataFrame(cursor_mysql.fetchall(), columns=['headline_text'])
    top_words_mysql = get_top_words_from_df(headlines_mysql)
print(f"[MySQL] Top 10 words (Time: {t.interval:.4f}s)")
print(top_words_mysql)
print()

# Cleanup
con_duck.close()
cursor_mysql.close()
conn_mysql.close() 