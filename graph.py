import pygame
from random import shuffle
from time import sleep

from tile import Tile

class Graph:
    def __init__(self, rows, columns, tile_size, start_x, start_y):
        Tile.size = tile_size
        self.rows = rows
        self.columns = columns
        self.tiles = [[0 for i in range(self.columns)] for j in range(self.rows)]
        self.is_maze = False

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

    def create_kruskal_maze(self, screen, delay):
        if self.is_maze:
            return
        self.is_maze = True

        # Create list of edges
        edges = []
        for i in range(self.rows-1):
            for j in range(self.columns - 1):
                edges.append(((i, j), (i+1, j)))
                edges.append(((i, j), (i, j+1)))
        for i in range(self.rows - 1):
            edges.append(((i, self.columns-1), (i+1, self.columns-1)))
        for j in range(self.columns - 1):
            edges.append(((self.rows-1, j), (self.rows-1, j+1)))
        shuffle(edges)

        # Create a set for each node
        trees = dict()
        for i in range(self.rows):
            for j in range(self.columns):
                trees[(i, j)] = set([(i, j)])

        while len(edges) != 0:
            screen.fill((255, 255, 255))
            self.draw(screen)
            pygame.display.flip()
            pygame.time.wait(delay) # Helps us see the generation on pygame
            edge = edges.pop()
            if len(trees[edge[0]].intersection(trees[edge[1]])) != 0:
                continue

            combined = trees[edge[0]].union(trees[edge[1]])
            for member in combined:
                trees[member] = combined

            # Get rid of visual barrier
            row1, column1 = edge[0]
            row2, column2 = edge[1]

            if row2 > row1:
                self.tiles[row1][column1].bottom_closed = False
                self.tiles[row2][column2].top_closed = False
            else:
                self.tiles[row1][column1].right_closed = False
                self.tiles[row2][column2].left_closed = False


