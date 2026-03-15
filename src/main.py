import pygame

# Init game
pygame.init()

# Surface screen config
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# Create the Clock obj for set the framerate for the While loop
clock = pygame.time.Clock()

# Create font
test_font = pygame.font.Font('src/font/Pixeltype.ttf', 70)

""" 
CREATE REGULAR SURFACES 
"""
# Images
sky_surface = pygame.image.load('src/graphics/Sky.png').convert()
ground_surface = pygame.image.load('src/graphics/ground.png').convert()
# Text
text_surface = test_font.render('Snake game!', False, 'Black')
# Snail surface
snail_surface = pygame.image.load(
    'src/graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    screen.blit(source=sky_surface, dest=(0, 0))
    screen.blit(source=ground_surface, dest=(0, 300))
    screen.blit(source=text_surface, dest=(400, 200))
    # Snail Animation
    snail_x_pos = (snail_x_pos - 5) if snail_x_pos >= -50 else 815
    screen.blit(source=snail_surface, dest=(snail_x_pos, 270))

    pygame.display.update()
    clock.tick(60)

# End pygame
pygame.quit()
