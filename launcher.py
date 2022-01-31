import sys
from PyQt5.QtWidgets import QApplication
from widgets.mainwindow import MainWindow


def lauch():
    app = QApplication(sys.argv)
    app.mainwindow = MainWindow(app)
    app.mainwindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    lauch()
