from PySide import QtGui

from lu.innocence.userinterface.component.scene import MouseCursorLayer


class Scene(QtGui.QGraphicsScene):

    def __init__(self, parent):
        super(Scene, self).__init__(parent)
        self.layers = []
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(96, 96, 96)))

    def mouseMoveEvent(self, event):
        for current_layer in self.layers:
            current_layer.mouseMoveEvent(event)
        super(Scene,self).mouseMoveEvent(event)

    def mouseLeaveEvent(self, event):
        for current_layer in self.layers:
            if isinstance(current_layer, MouseCursorLayer):
                current_layer.hide()

    def mouseEnterEvent(self, event):
        for current_layer in self.layers:
            if isinstance(current_layer, MouseCursorLayer):
                current_layer.show()

    def changeViewport(self, start_position, zoom):
        for current_layer in self.layers:
            current_layer.setZoom(zoom)
            current_layer.setRenderingStartPosition(start_position)

