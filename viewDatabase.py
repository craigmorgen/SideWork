import sqlite3
import pandas as pd


conn = sqlite3.connect('TheBats.db')
c = conn.cursor()

print(pd.read_sql_query('SELECT * FROM batquote', conn))
