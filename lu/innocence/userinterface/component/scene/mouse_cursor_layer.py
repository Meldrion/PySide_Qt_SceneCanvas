from PySide import QtGui, QtCore

from lu.innocence.userinterface.component.scene.abstract_layer import AbstractLayer
from lu.innocence.userinterface.component.scene.mouse_cursor import MouseCursor


class MouseCursorLayer(AbstractLayer):
    def __init__(self, unit_width, unit_height, unit_size, parent=None):
        super(MouseCursorLayer, self).__init__(unit_width, unit_height, parent)
        self.mouse_is_down = False
        self.current_layer_index = 0
        self.current_tileset = None
        self.current_selection_rect = None
        self.mouseCursor = MouseCursor(unit_size, self)
        self.mouse_unit_position = QtCore.QPointF(0, 0)
        self.mouseCursor.setSelectionStart(0, 10)
        self.mouseCursor.setSelectionDimension(5, 5)
        self.hide()

    def paint(painter, option, widget):
        pass

    def mouseMoveEvent(self, event):
        scenePos = event.scenePos()
        if self.boundingRect().contains(scenePos):

            self.mouseCursor.show()
            unit_pos = QtCore.QPointF(scenePos.x() / self.unit_size, scenePos.y() / self.unit_size)

            if unit_pos.x() != self.mouse_unit_position.x() or unit_pos.y() != self.mouse_unit_position.y():
                self.mouse_unit_position = QtCore.QPointF(unit_pos)
                self.mouseCursor.setPos(self.mouse_unit_position.x() * self.unit_size,
                                        self.mouse_unit_position.y() * self.unit_size)

        else:
            self.mouseCursor.hide()

    def mousePressEvent(self, event):
        self.mouse_is_down = True

    def mouseReleaseEvent(self, event):
        self.mouse_is_down = False

    def setCurrentTileset(self, tileset):
        self.current_tileset = tileset
        self.mouseCursor.setCurrentTileset(tileset)

    def setTilesetSelection(self, rect):
        self.current_selection_rect = QtCore.QRectF(rect)
        self.mouseCursor.setSelectionStart(rect.x(), rect.y())
        self.mouseCursor.setSelectionDimension(rect.width(), rect.height())
