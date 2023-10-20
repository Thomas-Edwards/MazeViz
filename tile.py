import pygame

class Tile:

    size = 0
    width = 3
    outline_color = (0, 0, 0)

    def __init__(self, origin):
        self.top_left = (origin[0], origin[1])
        self.top_right = (origin[0] + self.size, origin[1])
        self.bottom_left = (origin[0], origin[1] + self.size)
        self.bottom_right = (origin[0] + self.size, origin[1] + self.size)

        self.is_start = False
        self.is_end = False

        self.visited= False

        self.top_closed = True
        self.bottom_closed = True
        self.left_closed = True
        self.right_closed = True

    def draw(self, screen):
        if self.top_closed:
            pygame.draw.line(screen, self.outline_color, self.top_left, self.top_right, width=self.width)
        if self.left_closed:
            pygame.draw.line(screen, self.outline_color, self.top_left, self.bottom_left, width=self.width)
        if self.bottom_closed:
            pygame.draw.line(screen, self.outline_color, self.bottom_left, self.bottom_right, width=self.width)
        if self.right_closed:
            pygame.draw.line(screen, self.outline_color, self.top_right, self.bottom_right, width=self.width)

        if self.is_start:
            self.fill(screen, (255, 0, 0))
        elif self.is_end:
            self.fill(screen, (0, 0, 255))
        elif self.visited:
            self.fill(screen, (0, 255, 0))
    def fill(self, screen, color):
        pygame.draw.rect(screen, color, (self.top_left[0]+self.width*2, self.top_left[1]+self.width*2, self.size-self.width*4, self.size-self.width*4))
