import pygame

# Initialize Pygame
pygame.init()

# Setting window and color
size= 400,400
white_color = 255, 255, 255
screen = pygame.display.set_mode(size)
screen.fill(white_color)

# Set the position and size of the square
rect = pygame.Rect(100, 100,200,200)

# Draw the square
pygame.draw.rect(screen, (0, 0, 0), rect, 1)

pygame.display.flip()

# Keep the window open until it is closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()