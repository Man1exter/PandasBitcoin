from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os
import sys
import warnings

os.environ['SQLALCHEMY_WARN_20'] = 'yes'
if not sys.warnoptions:
    warnings.simplefilter("default")

Base = declarative_base()
password = 'Coins123'

try:
    engine = create_engine(f"sqlite:///mydatabitcoins.db?password={password}", echo=True)
    print("Successfully connected to the database.")
except Exception as e:
    print("An error occurred while connecting to the database:", e)


class Prices(Base):
    __tablename__ = 'Prices of Bitcoins'
    
    Coin = Column(String, primary_key = True)
    Date = Column(DateTime, primary_key = True)
    Currency = Column(String, primary_key = True)
    Price = Column(Integer)
    
    def __init__(self,Coin,Currency,Price):
        self.Coin = Coin
        self.Currency = Currency
        self.Price = Price
        self.Date = datetime.now()
    
Base.metadata.create_all(bind=engine)







#conn = sqlite3.connect('Bitcoin_price.db')
#cursor = conn.cursor()

#cursor.execute('''
#CREATE TABLE Prices_Bitcoin (
    #Coin TEXT,
    #Date DATETIME,
    #Currency TEXT,
    #Price INTEGER,
    #PRIMARY KEY (coin, date, currency)
#)
#''')

#conn.commit()
#conn.close()