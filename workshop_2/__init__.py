from PySide6.QtWidgets import QApplication
from workshop2.window import Window
import sys

def main() -> None:
    print("Hello from workshop!")
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())