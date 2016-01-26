from PySide import QtCore, QtGui

from lu.innocence.userinterface.component.scene.tile_data import TileData


class TileItem(QtGui.QGraphicsItem):

    def __init__(self, tilesetX, tilesetY, tilesetIndex, linked_tilesets, parent=None):
        super(TileItem, self).__init__(parent)
        tile_image = linked_tilesets.at(tilesetIndex).getTileAt(tilesetX, tilesetY)
        self.tile_data = TileData(tilesetX, tilesetY, tilesetIndex, tile_image)

    def boundingRect(self):
        return QtCore.QRectF(0, 0, self.tile_data.tilePicture().width()
                             , self.tile_data.tilePicture().height())

    def paint(self, painter, option, widget):
        tile = self.tile_data.tilePicture()
        painter.drawPixmap(0, 0, tile.width(), tile.height(), tile)
