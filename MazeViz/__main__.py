import pygame
from MazeViz.graph import Graph
from MazeViz.text import bfs_text, a_star_text, dfs_text, new_graph_text, starting_point_text, ending_point_text

SCREEN_LENGTH = 1000
SCREEN_HEIGHT = 750
ROWS = 20
COLUMNS = 20

def main():
    
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_LENGTH, SCREEN_HEIGHT], pygame.RESIZABLE)

    screen_constraint = min(SCREEN_LENGTH, SCREEN_HEIGHT)
    length_restraint = max(ROWS, COLUMNS)
    tile_size = (0.8 * screen_constraint) // length_restraint

    kruskal_delay = 200 - (ROWS * COLUMNS)
    starting_x = (SCREEN_LENGTH - COLUMNS * tile_size) / 2
    starting_y = (SCREEN_HEIGHT - ROWS * tile_size) / 2

    tile_width = 3 if ROWS * COLUMNS <= 900 else 1
    
    # Create graph
    graph = Graph(ROWS, COLUMNS, tile_size, starting_x, starting_y, tile_width)
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
            graph.create_kruskal_maze(screen, kruskal_delay)
        else:
            pygame.draw.rect(screen, (0, 0, 0), (int(SCREEN_LENGTH / 3), int(SCREEN_HEIGHT * 23 / 25), int(SCREEN_LENGTH / 3), int(SCREEN_HEIGHT / 25)), 2)
            screen.blit(new_graph_text, (int(SCREEN_LENGTH * 1.2 / 3), int(SCREEN_HEIGHT * 23.1 / 25)))
            if pygame.mouse.get_pressed()[0] and int(SCREEN_HEIGHT * 23 / 25) < pygame.mouse.get_pos()[1] < int(SCREEN_HEIGHT * 24 / 25) and int(SCREEN_LENGTH / 3) < pygame.mouse.get_pos()[0] < int(SCREEN_LENGTH*2 / 3):
                graph = Graph(ROWS, COLUMNS, tile_size, starting_x, starting_y, tile_width)

        if graph.start_tile == (-1, -1):
            screen.blit(starting_point_text, (int(SCREEN_LENGTH * 1.2 / 3), int(SCREEN_HEIGHT * 1.1 / 25)))
            graph.pick_start_tile(screen)
        if graph.start_tile != (-1, -1) and graph.end_tile == (-1, -1):
            screen.blit(ending_point_text, (int(SCREEN_LENGTH * 1.2 / 3), int(SCREEN_HEIGHT * 1.1 / 25)))
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
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
