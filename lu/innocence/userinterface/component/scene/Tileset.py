from PySide import QtGui


class Tileset():

    def __init__(self, path, tile_dim):

        self.tiles = []
        self.tileset_real_width = 0
        self.tileset_real_height = 0
        self.tileset_unit_width = 0
        self.tileset_unit_height = 0

        tilesetImage = QtGui.QPixmap()

        if tilesetImage.load(path):

            self.tileset_real_width = tilesetImage.width()
            self.tileset_real_height = tilesetImage.height()
            self.tileset_unit_width = self.tileset_real_width / tile_dim
            self.tileset_unit_height = self.tileset_real_height / tile_dim

            for x in range(0, self.tileset_unit_width):
                inner_list = []
                for y in range(0, self.tileset_unit_height):
                    current_tile = QtGui.QPixmap(
                            tilesetImage.copy(x * tile_dim, y * tile_dim, tile_dim, tile_dim))
                    inner_list.append(current_tile)
                self.tiles.append(inner_list)
        else:
            print("Could not load file: " + path)

    def is_in_range(self, x, y):
        return 0 <= x and 0 <= y and \
               x < self.tileset_unit_width \
               and y < self.tileset_unit_height

    def get_tile_at(self, x, y):
        return self.tiles[x][y]
