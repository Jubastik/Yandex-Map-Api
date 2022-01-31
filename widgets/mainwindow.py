from PyQt5.QtWidgets import QMainWindow
from ui.mainwindow import Ui_MainWindow as Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
    
    def keyPressEvent(self, event):
        '''Обработка нажатий'''
        pass

    def pgup_pressed(self):
        pass

    def pgdown_pressed(self):
        pass
    
    def search_on_click(self):
        pass

    def reset(self):
        pass

    def change_map_style(self, style):
        pass