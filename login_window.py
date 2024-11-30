# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from models import UserDatabase as db
from chat_window import ChatWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Login')
        self.resize(300,250)

        # Create all Widgets needed in App
        self.username_title = QLabel('Username')
        self.password_title = QLabel('Password')

        self.username_field = QLineEdit()
        self.password_field = QLineEdit()

        self.login_button = QPushButton('Login')
        self.register_button = QPushButton('Register')

        # Design Layout, add widgets to the screen
        layout = QVBoxLayout()
        layout.addWidget(self.username_title)
        layout.addWidget(self.username_field)

        layout.addWidget(self.password_title)
        layout.addWidget(self.password_field)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.register_button)
        button_layout.addWidget(self.login_button)
        layout.addLayout(button_layout)

        # Set the final layout to the Main
        self.setLayout(layout)

        # Event
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)
    
    def login(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if db.verify_password(username, password):
            self.close()
            self.open_chat_window()
        else:
            QMessageBox.critical(self, 'Error', 'Could not login')
            self.password_field.clear()

    def register(self):
        username = self.username_field.text()
        password = self.password_field.text()

        if not db.register_user(username, password):
            self.password_field.clear()
            QMessageBox.critical(self, 'Error', 'Could not register user')
        else:
            self.close()
            self.open_chat_window()

    def open_chat_window(self):
        self.chat_window = ChatWindow()
        self.chat_window.show()