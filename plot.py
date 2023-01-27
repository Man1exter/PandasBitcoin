import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('mydatabitcoins.db')
df = pd.read_sql('select * from PriceBitcoins', conn)
df.plot()
plt.show()

#print(df)

# print(df.tail(1)[['Date']]) -> last download line from db

#first_row = conn.execute("SELECT * FROM `PriceBitcoins` ORDER BY date LIMIT 1;").fetchone()
#last_row = conn.execute("SELECT * FROM `PriceBitcoins` ORDER BY date DESC LIMIT 1;").fetchone()
#print("First row:", first_row)
#print("Last row:", last_row)
#conn.close()
