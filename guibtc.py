from PySide6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QWidget
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('mydatabitcoins.db')
df = pd.read_sql('select * from PriceBitcoins', conn)
#df.plot()
#plt.show()

app = QApplication()
main_window = QWidget()
main_window.setWindowTitle("BITCOIN APPLICATION")

main_layout = QHBoxLayout()
left_layout = QVBoxLayout()
button1 = QPushButton("REFRESH")
button2 = QPushButton("Pie Chart")
button3 = QPushButton("Bar Graph")
button4 = QPushButton("Line Graph")
button5 = QPushButton("EXIT")
left_layout.addWidget(button1)
left_layout.addWidget(button2)
left_layout.addWidget(button3)
left_layout.addWidget(button4)
left_layout.addWidget(button5)

button1.setStyleSheet("background-color: red; color: white; font-weight: bold;")
button2.setStyleSheet("background-color: red; color: white; font-weight: bold;")
button3.setStyleSheet("background-color: red; color: white; font-weight: bold;")
button4.setStyleSheet("background-color: red; color: white; font-weight: bold;")
button5.setStyleSheet("background-color: red; color: white; font-weight: bold;")

right_widget = QTextEdit()
#for i in range(10):
    #right_widget.append("Linia tekstu {}".format(i+1))
    
main_layout.addLayout(left_layout)
main_layout.addWidget(right_widget)

main_window.setLayout(main_layout)
main_window.show()
main_window.resize(700,400)
main_window.setStyleSheet("background-color: black;")

conn.close()
app.exec_()
