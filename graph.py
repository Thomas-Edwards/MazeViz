from tile import Tile

class Graph:
    def __init__(self, rows, columns, tile_size, start_x, start_y):
        Tile.size = tile_size
        self.rows = rows
        self.columns = columns
        self.tiles = [[0 for i in range(self.columns)] for j in range(self.rows)]

        # Initialize each tile
        for i in range(self.rows):
            for j in range(self.columns):
                x_coord = tile_size * j + start_x
                y_coord = tile_size * i + start_y
                self.tiles[i][j] = Tile((x_coord, y_coord))

    def draw(self, screen):
        for i in range(self.rows):
            for j in range(self.columns):
                self.tiles[i][j].draw(screen)
