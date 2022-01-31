from PyQt5.QtWidgets import QMainWindow
from UI.ui_main import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from yandex_maps_api.geocoder import get_coordinates

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.set_map_picture()
        self.connect_btns()

    def connect_btns(self):
        self.btn_search.clicked.connect(self.search)

    def keyPressEvent(self, event):
        """Обработка нажатий"""
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

    def search(self):
        address = self.lineEdit.text()

    def set_map_picture(self, file_name='resources/map.png'):
        pixmap = QPixmap(file_name)

        self.map.setPixmap(pixmap)
        self.map.resize(pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())
