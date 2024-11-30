# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTextEdit, QVBoxLayout, QLabel, QPushButton

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chat')
        self.resize(300,250)

        # Create all Widgets needed in App
        self.message_title = QLabel('Message')
        self.message_field = QTextEdit()
        self.message_send = QPushButton('Send')

        # Design Layout, add widgets to the screen
        layout = QVBoxLayout()
        layout.addWidget(self.message_title)
        layout.addWidget(self.message_field)
        layout.addWidget(self.message_send)

        # Set the final layout to the Main
        self.setLayout(layout)