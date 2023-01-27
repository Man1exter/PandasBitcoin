import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('mydatabitcoins.db')
df = pd.read_sql('select * from PriceBitcoins', conn)
df.plot()
plt.show()

#print(df)