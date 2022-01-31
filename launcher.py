import sys
from PyQt5.QtWidgets import QApplication
from widgets.mainwindow import MainWindow


def lauch():
    app = QApplication(sys.argv)
    app.mainwindow = MainWindow(app)
    app.mainwindow.show()
    sys.exit(app.exec())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook
    lauch()
