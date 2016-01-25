from PySide import QtGui

from lu.innocence.userinterface.controller.main_window_controller import MainWindowController

if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)
    main_window = MainWindowController()
    sys.exit(app.exec_())
