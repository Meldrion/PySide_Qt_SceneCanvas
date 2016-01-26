from PySide import QtGui, QtCore
import math

from lu.innocence.userinterface.component.scene.tile_renderer import TileRenderer
from lu.innocence.userinterface.component.scene.abstract_layer import AbstractLayer
from lu.innocence.userinterface.component.scene.tile_data import TileData


class TileLayer(AbstractLayer):
    def __init__(self, unit_width, unit_height, unit_size, parent=None):
        super(TileLayer, self).__init__(unit_width, unit_height, unit_size, parent)
        self.linked_tilesets = []
        self.elements = []
        self.startPosition = QtCore.QPointF(0, 0)
        self.zoom = 1.0
        self.init()

    def init(self):

        self.elements = []
        for i in range(0, self.unit_width):
            inner_list = []
            for j in range(0, self.unit_height):
                inner_list.append(None)
            self.elements.append(inner_list)

    def paint(self, painter, option, widget):

        tile_dim = self.unit_size * self.zoom
        width = math.ceil(widget.width() / tile_dim)
        height = math.ceil(widget.height() / tile_dim)

        start_x = int(max(self.startPosition.x() / tile_dim, 0))
        start_y = int(max(self.startPosition.y() / tile_dim, 0))
        end_x = int(min(start_x + width, self.unit_width - 1))
        end_y = int(min(start_y + height, self.unit_height - 1))

        for i in range(start_x, end_x):
            for j in range(start_y, end_y):
                tile = self.elements[i][j]
                if tile is not None:
                    TileRenderer.instance().render(painter, tile, i, j)
        TileRenderer.instance().flush(painter)

    def addTileAt(self, x, y, tilesetIndex, tilesetX, tilesetY):
        data = TileData(tilesetX, tilesetY, tilesetIndex,
                        self.linked_tilesets[tilesetIndex].get_tile_at(tilesetX, tilesetY))
        self.elements[x][y] = data

    def deleteTileAt(self, x, y):
        self.elements[x][y] = None

    def addTileset(self, tileset):
        self.linked_tilesets.append(tileset)
