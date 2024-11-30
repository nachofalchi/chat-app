from PyQt5.QtWidgets import QApplication
from login_window import LoginWindow

def main():
    app = QApplication([])

    # Crear la ventana de inicio de sesión y mostrarla
    login_window = LoginWindow()
    login_window.show()

    # Ejecutar la aplicación
    app.exec_()

if __name__ == "__main__":
    main()
