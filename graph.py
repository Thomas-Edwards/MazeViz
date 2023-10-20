import pygame
from random import shuffle
from time import sleep

from tile import Tile

class Graph:
    def __init__(self, rows, columns, tile_size, start_x, start_y, tile_width):
        Tile.size = tile_size
        Tile.width = tile_width

        self.rows = rows
        self.columns = columns
        self.start_x = start_x
        self.start_y = start_y
        self.tiles = [[0 for i in range(self.columns)] for j in range(self.rows)]

        self.is_maze = False
        self.start_tile = (-1, -1)
        self.end_tile = (-1, -1)

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

    def get_mouse_pos(self):
        x_pos, y_pos = pygame.mouse.get_pos()
        if self.start_x < x_pos < self.start_x + self.columns * Tile.size:
            if self.start_y < y_pos < self.start_y + self.rows * Tile.size:
                column = int((x_pos - self.start_x) / Tile.size)
                row = int((y_pos - self.start_y) / Tile.size)
                return (row, column)
        return (-1, -1)

    def reset_visited(self):
        for i in range(self.rows):
            for j in range(self.columns):
                self.tiles[i][j].visited = False

    def pick_start_tile(self, screen):
        row, column = self.get_mouse_pos()
        if row != -1:
            self.tiles[row][column].fill(screen, (255, 0, 0))
            if pygame.mouse.get_pressed()[0]:
                self.tiles[row][column].is_start = True
                self.start_tile = (row, column)

    def pick_end_tile(self, screen):
        row, column = self.get_mouse_pos()
        if row != -1 and (row, column) != self.start_tile:
            self.tiles[row][column].fill(screen, (0, 0, 255))
            if pygame.mouse.get_pressed()[0]:
                self.tiles[row][column].is_end = True
                self.end_tile = (row, column)
                pygame.time.wait(200)

    def bfs(self, screen):
        self.reset_visited()
        queue = [self.start_tile]
        found_end = False
        while not found_end:
            pygame.time.wait(100)  # Helps us see the generation on pygame
            screen.fill((255, 255, 255))
            self.draw(screen)
            pygame.display.flip()
            curr = queue.pop(0)
            if curr == self.end_tile:
                found_end = True
            else:
                row, column = curr
                # Color visited node
                self.tiles[row][column].visited = True
                # Get valid neighbors
                if row != 0 and not self.tiles[row][column].top_closed and not self.tiles[row-1][column].visited:
                    queue.append((row-1, column))
                if row != self.rows - 1 and not self.tiles[row][column].bottom_closed and not self.tiles[row+1][column].visited:
                    queue.append((row+1, column))
                if column != 0 and not self.tiles[row][column].left_closed and not self.tiles[row][column-1].visited:
                    queue.append((row, column-1))
                if column != self.columns-1 and not self.tiles[row][column].right_closed and not self.tiles[row][column+1].visited:
                    queue.append((row, column+1))

    def dfs(self, screen):
        print("1 2 3 LETS GO BITCH")
        self.reset_visited()
        queue = [self.start_tile]
        found_end = False
        while not found_end:
            pygame.time.wait(100)  # Helps us see the generation on pygame
            screen.fill((255, 255, 255))
            self.draw(screen)
            pygame.display.flip()
            curr = queue.pop()
            if curr == self.end_tile:
                found_end = True
            else:
                row, column = curr
                # Color visited node
                self.tiles[row][column].visited = True
                # Get valid neighbors
                if row != 0 and not self.tiles[row][column].top_closed and not self.tiles[row-1][column].visited:
                    queue.append((row-1, column))
                if row != self.rows - 1 and not self.tiles[row][column].bottom_closed and not self.tiles[row+1][column].visited:
                    queue.append((row+1, column))
                if column != 0 and not self.tiles[row][column].left_closed and not self.tiles[row][column-1].visited:
                    queue.append((row, column-1))
                if column != self.columns-1 and not self.tiles[row][column].right_closed and not self.tiles[row][column+1].visited:
                    queue.append((row, column+1))

    def a_star(self, screen):
        print("1 2 3 LETS GO BITCH")
        self.reset_visited()
        queue = [self.start_tile]
        found_end = False
        while not found_end:
            pygame.time.wait(100)  # Helps us see the generation on pygame
            screen.fill((255, 255, 255))
            self.draw(screen)
            pygame.display.flip()
            curr = queue.pop()
            if curr == self.end_tile:
                found_end = True
            else:
                row, column = curr
                # Color visited node
                self.tiles[row][column].visited = True
                # Get valid neighbors
                if row != 0 and not self.tiles[row][column].top_closed and not self.tiles[row-1][column].visited:
                    queue.append((row-1, column))
                if row != self.rows - 1 and not self.tiles[row][column].bottom_closed and not self.tiles[row+1][column].visited:
                    queue.append((row+1, column))
                if column != 0 and not self.tiles[row][column].left_closed and not self.tiles[row][column-1].visited:
                    queue.append((row, column-1))
                if column != self.columns-1 and not self.tiles[row][column].right_closed and not self.tiles[row][column+1].visited:
                    queue.append((row, column+1))
                queue = sorted(queue, key=lambda x: abs(self.end_tile[0] - x[0]) + abs(self.end_tile[1] - x[1]), reverse=True)


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
            pygame.time.wait(delay)  # Helps us see the generation on pygame
            screen.fill((255, 255, 255))
            self.draw(screen)
            pygame.display.flip()
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


