from sys import argv
from PySide6.QtWidgets import QApplication
from window import MainWindow
import os

# Prevent Qt-logs from cluttering console
os.environ["QT_LOGGING_RULES"] = "*=false"


def main():
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()