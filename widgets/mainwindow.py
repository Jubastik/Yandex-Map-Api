from PyQt5.QtWidgets import QMainWindow
from UI.ui_main import Ui_MainWindow
from PyQt5.QtGui import QPixmap
from CONSTANTS import ZOOM, CORDS_DEFAULT, MAP_MODE

from yandex_maps_api.geocoder import get_coordinates

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.set_map_picture()
        self.zoom = ZOOM
        self.ll = CORDS_DEFAULT
        self.map_mode = MAP_MODE
        self.connect_btns()

    def connect_btns(self):
        self.btn_search.clicked.connect(self.search)

    def update_map(self):
        pass

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

    def set_map_picture(self, file_name="resources/map.png"):
        pass
    
    def search(self):
        address = self.lineEdit.text()
        coords = get_coordinates(address)
        if coords[0] is not None:
            self.ll = list(coords)
            self.update_map()
        else:
            self.statusbar.showMessage("Объект не найден", 10000)

    def set_map_picture(self, file_name='resources/map.png'):
        pixmap = QPixmap(file_name)

        self.map.setPixmap(pixmap)
        self.map.resize(pixmap.width(), pixmap.height())

        self.resize(pixmap.width(), pixmap.height())
