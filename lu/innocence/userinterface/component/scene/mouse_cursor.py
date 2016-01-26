from PySide import QtCore, QtGui


class MouseCursor(QtGui.QGraphicsItem):
    def __init__(self, unit_size, parent=None):
        super(MouseCursor, self).__init__(parent)
        self.unit_start_x = 0
        self.unit_start_y = 0
        self.unit_selection_width = 0
        self.unit_selection_height = 0
        self.current_tileset = None

    def boundingRect(self):
        return QtCore.QRectF(0, 0,
                             self.unit_selection_width * self.unit_size,
                             self.unit_selection_height * self.unit_size)

    def paint(self, painter, option, widget):

        rect = self.boundingRect()
        if self.current_tileset is not None:
            painter.setOpacity(0.45);

            for i in range(self.unit_start_X, self.unit_start_X + self.unit_selection_width):
                for j in range(self.unit_start_Y, self.unit_start_Y + self.unit_selection_width):

                    if self.m_current_tileset.isInRange(i, j):
                        painter.drawPixmap((i - self.unit_start_X) * self.unit_size,
                                           (j - self.unit_start_Y) * self.unit_size,
                                           self.unit_size, self.unit_size,
                                           self.current_tileset.getTileAt(i, j))

        painter.fillRect(rect, QtGui.QBrush(self.rect_color))

    def setSelectionStart(self, selection_start_x, selection_start_y):
        self.unit_start_x = selection_start_x
        self.unit_start_y = selection_start_y

    def setSelectionDimension(self, unit_selection_width, unit_selection_height):
        self.unit_selection_width = unit_selection_width
        self.unit_selection_height = unit_selection_height

    def setCurrentTileset(self, tileset):
        self.current_tileset = tileset
