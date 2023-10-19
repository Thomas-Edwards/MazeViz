import pygame
from graph import Graph

pygame.init()

# Set up the drawing window

SCREEN_LENGTH = 1000
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode([SCREEN_LENGTH, SCREEN_HEIGHT], pygame.RESIZABLE)

ROWS = 15
COLUMNS = 15
SIZE = 40
KRUSKAL_DELAY = 10
STARTING_X = (SCREEN_LENGTH - COLUMNS * SIZE) / 2
STARTING_Y = (SCREEN_HEIGHT - ROWS * SIZE) / 2

# Create graph
graph = Graph(ROWS, COLUMNS, SIZE, STARTING_X, STARTING_Y)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    graph.create_kruskal_maze(screen, KRUSKAL_DELAY)
    graph.draw(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()