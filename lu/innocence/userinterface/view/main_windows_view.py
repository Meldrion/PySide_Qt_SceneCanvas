# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Jan 25 18:32:08 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

from lu.innocence.userinterface.component.SceneCanvas import SceneCanvas


class MainWindowView(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.scene_canvas = SceneCanvas(self)
        self.scene_canvas.setObjectName("SceneCanvas")
        self.setCentralWidget(self.scene_canvas)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()

    def retranslateUi(self):
        self.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

    def centerOnScreen(self):
        self.setGeometry(
                QtGui.QStyle.alignedRect(QtCore.Qt.LeftToRight, QtCore.Qt.AlignCenter, self.size(),
                                         QtGui.qApp.desktop().availableGeometry()))
