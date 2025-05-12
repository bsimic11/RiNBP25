
import pymysql
import time

# Povezivanje na MySQL
conn = pymysql.connect(host="localhost", user="root", password="", database="news_data", charset="utf8mb4")
cur = conn.cursor()

def run_query(query, description):
    print(f"\n{description}")
    start = time.time()
    cur.execute(query)
    result = cur.fetchall()
    end = time.time()
    print(f"Vrijeme izvršavanja: {end - start:.4f} sekundi")
    print(f"Broj redova: {len(result)}")
    for row in result[:5]:
        print(row)

# Upiti
queries = [
    ("SELECT YEAR(publish_date) AS godina, COUNT(*) FROM headlines GROUP BY godina ORDER BY godina;",
     "Broj naslova po godini"),

    ("SELECT COUNT(*) FROM headlines WHERE headline_text LIKE '%war%';",
     "Broj naslova koji sadrže riječ 'war'"),

    ("SELECT publish_date, COUNT(*) FROM headlines GROUP BY publish_date ORDER BY publish_date LIMIT 10;",
     "Broj naslova po danu (prvih 10 dana)")
]

for query, desc in queries:
    run_query(query, desc)

cur.close()
conn.close()
