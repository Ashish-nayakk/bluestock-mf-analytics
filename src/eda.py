import sqlite3
import pandas as pd

conn = sqlite3.connect("data/mutual_funds.db")

df = pd.read_sql_query("SELECT * FROM mutual_funds", conn)

print(df.head())
print(df.shape)

conn.close()