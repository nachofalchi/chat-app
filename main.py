# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

from random import choice

# Main App Objects and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Random Word Maker')
main_window.resize(300,200)

# Create all Widgets needed in App
title = QLabel('Random keywords')

text1 = QLabel('Keyword 1')
text2 = QLabel('Keyword 2')
text3 = QLabel('Keyword 3')

button1 = QPushButton('Click me')
button2 = QPushButton('Click me')
button3 = QPushButton('Click me')

my_words = ['hello', 'bye', 'good', 'bad', 'happy', 'sad', 'love', 'hate', 'python', 'java']

# Design Layout, add widgets to the screen

master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)

row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

# Set the final layout to the Main 
main_window.setLayout(master_layout)

# Create a functions
def random_word1():
    word = choice(my_words)
    text1.setText(word)

def random_word2():
    word = choice(my_words)
    text2.setText(word)

def random_word3():
    word = choice(my_words)
    text3.setText(word)

# Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)

# Show/Run our App
main_window.show()
app.exec_()