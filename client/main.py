from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow
from websocket_client import WebSocketClient
import asyncio

from PyQt5.QtCore import QTimer, QEventLoop

async def main():
    app = QApplication([])

    ws_client = WebSocketClient("ws://localhost:8000/ws")

    login_window = LoginWindow()
    login_window.show()

    app.exec_()

if __name__ == "__main__":
    main()
