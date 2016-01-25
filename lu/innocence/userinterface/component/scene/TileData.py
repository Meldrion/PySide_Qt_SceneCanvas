class TileData:
    def __init__(self, tileset_x, tileset_y, tileset_index, tile_picture):
        self.tileset_x = tileset_x
        self.tileset_y = tileset_y
        self.tileset_index = tileset_index
        self.tile_picture = tile_picture

    def tilesetX(self):
        return self.tileset_x

    def tilesetY(self):
        return self.tileset_y

    def tilesetIndex(self):
        return self.tileset_index

    def tilePicture(self):
        return self.tile_picture

    def equals(self, other):
        return self.tileset_index == other.tilesetIndex() and \
               self.tileset_x == other.tilesetX() and \
               self.tileset_y == other.tilesetY()
