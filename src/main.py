import pygame
from classes.Game import Game
from classes.MainMenu import MainMenu

# Initialize pygame
pygame.init()

game = Game()
game.initialize()

main_menu = MainMenu()

"""
VARIABLES
"""
running = True
game_active = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_active = True

    if game_active:
        game.update()
        if game.game_lose():
            game_active = False
            game.reset()
    else:
        main_menu.update()

    pygame.display.update()
    clock.tick(60)

# End pygame
pygame.quit()
