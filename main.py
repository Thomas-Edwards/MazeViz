import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 750], pygame.RESIZABLE)

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
    pygame.draw.line(screen, (0, 0, 0), (30, 30), (60, 30), width=3)
    pygame.draw.line(screen, (0, 0, 0), (30, 30), (30, 60), width=3)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()