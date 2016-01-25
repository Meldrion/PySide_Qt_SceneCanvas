from PySide import QtGui

from lu.innocence.userinterface.component.scene import MouseCursorLayer


class Scene(QtGui.QGraphicsScene):
    def __init__(self, parent=None):
        super(Scene, self).__init__(parent)
        self.layers = []
        self.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(96, 96, 96)))

    def mouseMoveEvent(self, event):
        for current_layer in self.layers:
            current_layer.mouseMoveEvent(event)
        super(Scene, self).mouseMoveEvent(event)

    def mouse_leave_event(self):
        for current_layer in self.layers:
            if isinstance(current_layer, MouseCursorLayer):
                current_layer.hide()

    def mouse_enter_event(self):
        for current_layer in self.layers:
            if isinstance(current_layer, MouseCursorLayer):
                current_layer.show()

    def change_viewport(self, start_position, zoom):
        for current_layer in self.layers:
            current_layer.setZoom(zoom)
            current_layer.setRenderingStartPosition(start_position)

    def add_layer(self, layer):
        if layer not in self.layers:
            self.layers.append(layer)
            self.addItem(layer)
