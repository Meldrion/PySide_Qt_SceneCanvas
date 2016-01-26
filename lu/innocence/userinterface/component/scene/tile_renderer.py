from PySide import QtCore, QtGui


class TileRenderer:
    __instance = None

    def __init__(self):
        self.current_tile = None
        self.fragments = []

    @staticmethod
    def instance():
        if not TileRenderer.__instance:
            TileRenderer.__instance = TileRenderer()
        return TileRenderer.__instance

    def render(self, painter, tile, x, y):
        if tile is None:
            return

        if self.current_tile is not None and not self.current_tile.equals(tile):
            self.flush(painter)
        self.current_tile = tile

        w = tile.tilePicture().width()
        h = tile.tilePicture().height()

        fragment = QtGui.QPainter.PixmapFragment()
        fragment.x = x * w + w / 2
        fragment.y = y * h + h / 2
        fragment.width = tile.tilePicture().width()
        fragment.height = tile.tilePicture().height()
        fragment.scaleX = 1
        fragment.scaleY = 1
        fragment.rotation = 0
        fragment.opacity = 1
        self.fragments.append(fragment)

    def flush(self, painter):

        fragment_count = len(self.fragments)

        if self.current_tile is None or fragment_count <= 0:
            return

        painter.drawPixmapFragments(self.fragments[0],
                                    fragment_count,
                                    self.current_tile.tilePicture())

        self.current_tile = None
        self.fragments = []