from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow

from CONSTANTS import ZOOM, CORDS_DEFAULT, MAP_MODE
from UI.ui_main import Ui_MainWindow
from yandex_maps_api.geocoder import get_address_info


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.set_map_picture()
        self.zoom = ZOOM
        self.ll = CORDS_DEFAULT
        self.map_mode = MAP_MODE
        self.marker_on_map = False
        self.marker_coords = [None, None]
        self.connect_btns()

    def connect_btns(self):
        self.btn_search.clicked.connect(self.search)
        self.btn_reset.clicked.connect(self.reset)

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
        self.lineEdit.setText("")
        self.set_address("")
        self.marker_on_map = False
        self.marker_coords = [None, None]

    def change_map_style(self, style):
        pass
    
    def search(self):
        address = self.lineEdit.text()
        try:
            ans = get_address_info(address)
        except RuntimeError as e:
            self.statusbar.showMessage("Ошибка выполнения запроса", 10000)
            return
        coords = ans[0]
        full_address = ans[1]
        postal_code = ans[2]
        if ans[0] is not None:
            self.ll = coords
            self.marker_on_map = True
            self.marker_coords = coords
            self.update_map()
            if self.cb_post.isChecked():
                self.set_address(f"{full_address}\nПочтовый адрес: {postal_code}")
            else:
                self.set_address(full_address)
        else:
            self.statusbar.showMessage("Объект не найден", 10000)

    def set_map_picture(self, file_name='resources/map.png', img=None):
        if img is None:
            pixmap = QPixmap(file_name)
        else:
            pixmap = QPixmap.fromImage(img)
        pixmap = QPixmap(file_name)

        self.map.setPixmap(pixmap)
        self.map.resize(pixmap.width(), pixmap.height())
        self.resize(pixmap.width(), pixmap.height())
    
    def set_address(self, address):
        self.object_data.setText(address)