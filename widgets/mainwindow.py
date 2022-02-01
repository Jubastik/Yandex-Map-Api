from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt

from CONSTANTS import ZOOM, CORDS_DEFAULT, MAP_MODE
from UI.main_ui import Ui_MainWindow
from yandex_maps_api.geocoder import get_address_info
from yandex_maps_api.make_params import make_params
from yandex_maps_api.save_map_picture import save_map_picture


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.set_map_picture(file_name="resources/map_cache.png")
        self.zoom = ZOOM
        self.ll = CORDS_DEFAULT
        self.map_mode = MAP_MODE
        self.marker_on_map = False
        self.marker_coords = [None, None]
        self.update_map()
        self.connect_btns()

    def connect_btns(self):
        self.btn_search.clicked.connect(self.on_click_search)
        self.btn_reset.clicked.connect(self.reset)
        self.btn_hybrid.clicked.connect(self.hybrid_clicked)
        self.btn_scheme.clicked.connect(self.scheme_clicked)
        self.btn_satellite.clicked.connect(self.sattelite_clicked)

    def hybrid_clicked(self):
        self.map_mode = "sat,skl"
        self.update_map()

    def scheme_clicked(self):
        self.map_mode = "map"
        self.update_map()

    def sattelite_clicked(self):
        self.map_mode = "sat"
        self.update_map()

    def update_map(self):
        if self.marker_on_map:
            params = make_params(self.ll, self.map_mode, self.zoom, pt=True, pt_cords=self.marker_coords)
        else:
            params = make_params(self.ll, self.map_mode, self.zoom)
        save_map_picture(params)
        self.set_map_picture(file_name="resources/map_cache.png")

    def keyPressEvent(self, event):
        """Обработка нажатий"""
        if event.key() == Qt.Key_PageUp:
            self.zoom = max(self.zoom / 2, 0.00015625)
            self.update_map()
        elif event.key() == Qt.Key_PageDown:
            self.zoom = min(self.zoom * 2, 81.92)
            self.update_map()
        elif event.key() == Qt.Key_Down:
            self.ll = [self.ll[0], str(float(self.ll[1]) - 0.5 * self.zoom)]
            self.update_map()
        elif event.key() == Qt.Key_Up:
            self.ll = [self.ll[0], str(float(self.ll[1]) + 0.5 * self.zoom)]
            self.update_map()
        elif event.key() == Qt.Key_Right:
            self.ll = [str(float(self.ll[0]) + 0.5 * self.zoom), self.ll[1]]
            self.update_map()
        elif event.key() == Qt.Key_Left:
            self.ll = [str(float(self.ll[0]) - 0.5 * self.zoom), self.ll[1]]
            self.update_map()

    def mousePressEvent(self, event):
        # k = zoom / 450  // коэфициент для 1 пикселя (перевод из пикселей в координаты)
        # ll(local) = (225; 225) | (225 * k; 225 * k)  // локальные координаты относительно левого верхнего угла
        # zero(global) = ll(global) - ll(local)  // глобальные координаты левого верхний угла
        # t1(local) = (x; y) | (x * k; y * k)
        # t1(global) = t1(local) + zero(global)

        # X1 x Y1 ; X2  x  Y2 ; W   x   H
        # 9  x 39 ; 459 x 489 ; 450 x 450
        if event.button() == Qt.RightButton:
            pos = (event.x(), event.y())
            if 9 <= pos[0] <= 459 and 39 <= pos[1] <= 489:
                # pos = (pos[0] - 9, pos[1] - 39)
                # k = self.zoom // 450
                # ll_local = [225 * k, 225 * k]
                # zero_global = [self.ll[0] - ll_local[0], self.ll[1] - ll_local[1]]
                # t1_local = [pos[0] * k, pos[1] * k]
                # t1_global = [t1_local[0] + zero_global[0], t1_local[1] + zero_global[1]]
                # cords = ','.join(t1_global)
                # self.search(cords)
                pass
        elif event.button() == Qt.LeftButton:
            pos = (event.x(), event.y())
            if 9 <= pos[0] <= 459 and 39 <= pos[1] <= 489:
                pos = (pos[0] - 9, pos[1] - 39)
                k = self.zoom / 450
                ll_local = [225 * k, 225 * k]
                zero_global = [
                    float(self.ll[0]) - ll_local[0],
                    float(self.ll[1]) - ll_local[1],
                ]
                t1_local = [pos[0] * k, pos[1] * k]
                t1_global = [t1_local[0] + zero_global[0], t1_local[1] + zero_global[1]]
                cords = ",".join(list(map(str, t1_global)))
                self.search(cords, map_cords_update=False)

    def reset(self):
        self.lineEdit.setText("")
        self.set_address("")
        self.marker_on_map = False
        self.marker_coords = [None, None]

    def on_click_search(self):
        address = self.lineEdit.text()
        self.search(address)

    def search(self, address, map_cords_update=True):
        try:
            ans = get_address_info(address)
        except RuntimeError as e:
            self.statusbar.showMessage("Ошибка выполнения запроса", 10000)
            return
        coords = ans[0]
        full_address = ans[1]
        postal_code = ans[2]
        if ans[0] is not None:
            if map_cords_update:
                self.ll = list(map(str, coords))
            self.marker_on_map = True
            self.marker_coords = coords
            self.update_map()
            if self.cb_post.isChecked():
                self.set_address(f"{full_address}\nПочтовый адрес: {postal_code}")
            else:
                self.set_address(full_address)
        else:
            self.statusbar.showMessage("Объект не найден", 10000)

    def set_map_picture(self, file_name="resources/map.png", img=None):
        if img is None:
            pixmap = QPixmap(file_name)
        else:
            pixmap = QPixmap.fromImage(img)

        self.map.setPixmap(pixmap)
        self.map.resize(pixmap.width(), pixmap.height())
        self.resize(pixmap.width(), pixmap.height())

    def set_address(self, address):
        self.object_data.setText(address)
