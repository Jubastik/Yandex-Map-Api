# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(518, 393)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.btn_reset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_reset.setObjectName("btn_reset")
        self.horizontalLayout.addWidget(self.btn_reset)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.map = QtWidgets.QLabel(self.centralwidget)
        self.map.setStyleSheet("background-color: rgb(167, 170, 155);")
        self.map.setText("")
        self.map.setObjectName("map")
        self.verticalLayout_4.addWidget(self.map)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_scheme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_scheme.setObjectName("btn_scheme")
        self.verticalLayout.addWidget(self.btn_scheme)
        self.btn_satellite = QtWidgets.QPushButton(self.centralwidget)
        self.btn_satellite.setObjectName("btn_satellite")
        self.verticalLayout.addWidget(self.btn_satellite)
        self.btn_hybrid = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hybrid.setObjectName("btn_hybrid")
        self.verticalLayout.addWidget(self.btn_hybrid)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_post = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_post.setObjectName("cb_post")
        self.verticalLayout_2.addWidget(self.cb_post)
        self.object_data = QtWidgets.QTextEdit(self.centralwidget)
        self.object_data.setReadOnly(True)
        self.object_data.setObjectName("object_data")
        self.verticalLayout_2.addWidget(self.object_data)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Free map"))
        self.btn_search.setText(_translate("MainWindow", "Искать"))
        self.btn_reset.setText(_translate("MainWindow", "Сброс"))
        self.btn_scheme.setText(_translate("MainWindow", "Схема"))
        self.btn_satellite.setText(_translate("MainWindow", "Спутник"))
        self.btn_hybrid.setText(_translate("MainWindow", "Гибрид"))
        self.cb_post.setText(_translate("MainWindow", "Почтовый адрес"))
