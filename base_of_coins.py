import requests
import time
import main
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=main.engine)
session = Session()

def add_price(Coin,Currency,Price):
    pad = main.Prices(Coin,Currency,Price)
    session.add(pad)
    session.commit()
    
while True:

   res = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()
   print(res)
   print(res['data']['base'], res['data']['currency'], res['data']['amount'])
   add_price(res['data']['base'], res['data']['currency'], res['data']['amount'])
   
   time.sleep(2)

session.close()