import pygame
from graph import Graph
from text import bfs_text, a_star_text, dfs_text
from math import log2

pygame.init()

# Set up the drawing window

SCREEN_LENGTH = 1000
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode([SCREEN_LENGTH, SCREEN_HEIGHT], pygame.RESIZABLE)

ROWS = 20
COLUMNS = 20

#SIZE = 104 - int(log2(ROWS * COLUMNS)*8.7)
#SIZE = 104 - int(log2(ROWS * COLUMNS)*log2(ROWS * COLUMNS) * log2(ROWS * COLUMNS))
SCREEN_CONSTRAINT = min(SCREEN_LENGTH, SCREEN_HEIGHT)
LENGTH_RESTRAINT = max(ROWS, COLUMNS)
SIZE = (0.8 * SCREEN_CONSTRAINT) // (LENGTH_RESTRAINT)

KRUSKAL_DELAY = 200 - (ROWS * COLUMNS)
STARTING_X = (SCREEN_LENGTH - COLUMNS * SIZE) / 2
STARTING_Y = (SCREEN_HEIGHT - ROWS * SIZE) / 2

TILE_WIDTH = 3 if ROWS * COLUMNS <= 900 else 1
# Create graph
graph = Graph(ROWS, COLUMNS, SIZE, STARTING_X, STARTING_Y, TILE_WIDTH)

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    if not graph.is_maze:
        graph.create_kruskal_maze(screen, KRUSKAL_DELAY)
    if graph.start_tile == (-1, -1):
        graph.pick_start_tile(screen)
    if graph.start_tile != (-1, -1) and graph.end_tile == (-1, -1):
        graph.pick_end_tile(screen)

    if graph.start_tile != (-1, -1) and graph.end_tile != (-1, -1):
        pygame.draw.rect(screen, (0, 0, 0), (int(SCREEN_LENGTH*2/9), int(SCREEN_HEIGHT/25), int(SCREEN_LENGTH/9), int(SCREEN_HEIGHT/25)), 2)
        screen.blit(bfs_text, (int(SCREEN_LENGTH*2.3/9), int(SCREEN_HEIGHT*1.1/25)))

        pygame.draw.rect(screen, (0, 0, 0), (int(SCREEN_LENGTH*4/9), int(SCREEN_HEIGHT/25), int(SCREEN_LENGTH/9), int(SCREEN_HEIGHT/25)), 2)
        screen.blit(a_star_text, (int(SCREEN_LENGTH*4.4/9), int(SCREEN_HEIGHT*1.1/25)))

        pygame.draw.rect(screen, (0, 0, 0), (int(SCREEN_LENGTH*6/9), int(SCREEN_HEIGHT/25), int(SCREEN_LENGTH/9), int(SCREEN_HEIGHT/25)), 2)
        screen.blit(dfs_text, (int(SCREEN_LENGTH*6.3/9), int(SCREEN_HEIGHT*1.1/25)))

    if pygame.mouse.get_pressed()[0] and int(SCREEN_HEIGHT / 25) < pygame.mouse.get_pos()[1] < int(SCREEN_HEIGHT * 2 / 25):
        if int(SCREEN_LENGTH * 2 / 9) < pygame.mouse.get_pos()[0] < int(SCREEN_LENGTH * 3 / 9):
            graph.bfs(screen)
        elif int(SCREEN_LENGTH * 4 / 9) < pygame.mouse.get_pos()[0] < int(SCREEN_LENGTH * 5 / 9):
            graph.a_star(screen)
        elif int(SCREEN_LENGTH * 6 / 9) < pygame.mouse.get_pos()[0] < int(SCREEN_LENGTH * 7 / 9):
            graph.dfs(screen)

    graph.draw(screen)
    # Flip the display
    pygame.display.flip()
    #print(pygame.mouse.get_pos())

# Done! Time to quit.
pygame.quit()