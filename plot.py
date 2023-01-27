import pandas as pd
import sqlite3

conn = sqlite3.connect('mydatabitcoins.db')
df = pd.read_sql('select * from PriceBitcoins', conn)
df.plot()