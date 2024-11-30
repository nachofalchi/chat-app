# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from server.db.users import UserDatabase as db
from chat_window import ChatWindow

class ChatlistWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Chatlist')
        self.resize(300,250)

        # Create all Widgets needed in App


        # Design Layout, add widgets to the screen

        # Set the final layout to the Main

        # Event
    