from PySide import QtGui
from lu.innocence.userinterface.view.main_windows_view import MainWindowView


class MainWindowController:

    def __init__(self):
        self.view = MainWindowView()
        self.view.centerOnScreen()
        self.view.scene_canvas.init()
        self.view.show()
