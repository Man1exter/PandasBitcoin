from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QWidget
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import requests
import time
import main
from sqlalchemy.orm import sessionmaker


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.main_layout = QHBoxLayout()
        self.left_layout = QVBoxLayout()
        self.button1 = QPushButton("REFRESH")
        self.button2 = QPushButton("Pie Chart")
        self.button3 = QPushButton("Bar Graph")
        self.button4 = QPushButton("Line Graph")
        self.button5 = QPushButton("EXIT")
        self.left_layout.addWidget(self.button1)
        self.left_layout.addWidget(self.button2)
        self.left_layout.addWidget(self.button3)
        self.left_layout.addWidget(self.button4)
        self.left_layout.addWidget(self.button5)

        self.button1.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        self.button2.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        self.button3.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        self.button4.setStyleSheet("background-color: red; color: white; font-weight: bold;")
        self.button5.setStyleSheet("background-color: red; color: white; font-weight: bold;")

        self.conn = sqlite3.connect('mydatabitcoins.db')
        self.df = pd.read_sql('select * from PriceBitcoins', self.conn)
    
        self.right_widget = QTextEdit()
        
        self.conn = sqlite3.connect('mydatabitcoins.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('SELECT * FROM PriceBitcoins')
        self.results = self.cursor.fetchall()
        
        for result in self.results:
           self.right_widget.append(result[1])
        
        self.conn.close()

        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addWidget(self.right_widget)

        self.setLayout(self.main_layout)
        self.setWindowTitle("BITCOIN APPLICATION")
        self.resize(700,400)
        self.setStyleSheet("background-color: black; color: white;")
        
        self.button1.clicked.connect(self.news_right_wind)
        self.button2.clicked.connect(self.on_button_pie)
        self.button3.clicked.connect(self.on_button_bar)
        self.button4.clicked.connect(self.on_button_line)
        self.button5.clicked.connect(self.on_button_clicked)
        
        self.Session = sessionmaker(bind=main.engine)
        self.session = self.Session()
        
    def add_price(self, Coin, Currency, Price):
          self.pad = main.Prices(Coin, Currency, Price)
          self.session.add(self.pad)
          self.session.commit()
          
    def news_right_wind(self):
          self.counter = 0
          while True:
            if self.counter < 10:
              res = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD").json()
              Coin = res['data']['base']
              Currency = res['data']['currency']
              Price = res['data']['amount']
              self.add_price(Coin, Currency, Price)
              time.sleep(2)
              self.counter += 1
            else:
              break
            
            self.session.close()
        
    def on_button_clicked(self):
        app.exit()
    
    def on_button_pie(self):
        conn = sqlite3.connect('mydatabitcoins.db')
        self.df = pd.read_sql('select * from PriceBitcoins', conn)
        self.df = self.df.head(50)
        self.df.plot()
        plt.show()
        conn.close()
        
    def on_button_line(self):
        conn = sqlite3.connect('mydatabitcoins.db')
        self.df = pd.read_sql('select * from PriceBitcoins', conn)
        self.df = self.df['Price'].value_counts().nlargest(30)
        self.df.plot.bar(x='Price', y='Date')
        plt.show()
        conn.close()
    
    def on_button_bar(self):
        conn = sqlite3.connect('mydatabitcoins.db')
        self.df = pd.read_sql('select * from PriceBitcoins', conn)
        self.df = self.df['Price'].value_counts().nlargest(20)
        self.df.plot.pie(y='Price', autopct='%1.1f%%')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()
        conn.close()
        

app = QApplication()
window = MyWindow()
window.show()
app.exec_()

