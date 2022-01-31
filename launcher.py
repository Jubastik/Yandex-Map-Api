import sys
import PyQt5
from PyQt5.QtWidgets import QApplication
from widgets.mainwindow import MainWindow


def lauch():
    app = QApplication(sys.argv)
    app.mainwindow = MainWindow(app)
    sys.exit(app.exec())
