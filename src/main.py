import pygame
from src.classes.Game import Game

# Initialize pygame
pygame.init()

game = Game()
game.initialize()

"""
VARIABLES
"""
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    game.update()

    pygame.display.update()
    clock.tick(60)

# End pygame
pygame.quit()
