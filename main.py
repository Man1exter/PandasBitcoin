import pandas as pd
import numpy as np
import matplotlib as mtp
import sqlite3

conn = sqlite3.connect('Bitcoin_price.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE Prices_Bitcoin (
    Coin TEXT,
    Date DATETIME,
    Currency TEXT,
    Price INTEGER,
    PRIMARY KEY (coin, date, currency)
)
''')

conn.commit()
conn.close()