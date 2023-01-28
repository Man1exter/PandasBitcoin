from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QWidget
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        conn = sqlite3.connect('mydatabitcoins.db')
        self.df = pd.read_sql('select * from PriceBitcoins', conn)
        #df.plot()
        #plt.show()

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

        self.right_widget = QTextEdit()
        #for i in range(10):
            #right_widget.append("Linia tekstu {}".format(i+1))

        self.main_layout.addLayout(self.left_layout)
        self.main_layout.addWidget(self.right_widget)

        self.setLayout(self.main_layout)
        self.setWindowTitle("BITCOIN APPLICATION")
        self.resize(700,400)
        self.setStyleSheet("background-color: black; color: white;")
        
        self.button2.clicked.connect(self.on_button_pie)
        self.button5.clicked.connect(self.on_button_clicked)
        
        conn.close()

    def on_button_clicked(self):
        app.exit()
    
    def on_button_pie(self):
        conn = sqlite3.connect('mydatabitcoins.db')
        self.df = pd.read_sql('select * from PriceBitcoins', conn)
        self.df.plot()
        plt.show()
        conn.close()

app = QApplication()
window = MyWindow()
window.show()
app.exec_()

