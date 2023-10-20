import pygame

pygame.font.init()
font = pygame.font.Font(None, 36)

bfs_text = font.render("BFS", True, (0, 0, 0))
a_star_text = font.render("A*", True, (0, 0, 0))
dfs_text = font.render("DFS", True, (0, 0, 0))

new_graph_text = font.render("Create New Graph", True, (0, 0, 0))

starting_point_text = font.render("Select Starting Point", True, (0, 0, 0))
ending_point_text = font.render("Select Ending Point", True, (0, 0, 0))
