from PySide import QtGui, QtCore
import math

from lu.innocence.userinterface.component.scene import TileRenderer
from lu.innocence.userinterface.component.scene.AbstractLayer import AbstractLayer


class TileLayer(AbstractLayer):
    def __init__(self, unit_width, unit_height, unit_size, parent=None):
        super(TileLayer, self).__init__(unit_width, unit_height, unit_size, parent)
        self.elements = []
        self.startPosition = QtCore.QPointF(0, 0)
        self.zoom = 1.0
        self.init()

    def init(self):

        self.elements.clear()
        for i in range(0, self.unit_width):
            inner_list = []
            for j in range(0, self.unit_height):
                inner_list.append(None)
            self.elements.append(inner_list)

    def paint(self, painter, option, widget):

        tile_dim = self.unit_size * self.zoom
        width = math.ceil(widget.width() / tile_dim)
        height = math.ceil(widget.height() / tile_dim)

        start_x = max(self.startPosition.x() / tile_dim, 0)
        start_y = max(self.startPosition.y() / tile_dim, 0)
        end_x = min(start_x + width, self.unit_width - 1)
        end_y = min(start_y + height, self.unit_height - 1)

        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                tile = self.elements[i][j]
                if tile is not None:
                    TileRenderer.instance().render(painter, tile, i, j)
