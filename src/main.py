import pygame

# Init game
pygame.init()

# Surface screen config
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')

# Colors
text_color = '#404040'
box_color = '#c0e8ec'

# Create the Clock obj for set the framerate for the While loop
clock = pygame.time.Clock()

# Create font
test_font = pygame.font.Font('src/font/Pixeltype.ttf', 50)

""" 
CREATE REGULAR SURFACES 
"""
# Images
sky_surface = pygame.image.load('src/graphics/Sky.png').convert()
ground_surface = pygame.image.load('src/graphics/ground.png').convert()
# Text
score_surface = test_font.render('Snake game!', False, text_color)
# Snail surface
snail_surface = pygame.image.load(
    'src/graphics/snail/snail1.png').convert_alpha()
# Player surface
player_surface = pygame.image.load(
    'src/graphics/player/player_walk_1.png').convert_alpha()

""" 
CREATE RECTANGLES FOR THE SURFACES
"""
# Snail rect
snail_rect = snail_surface.get_rect(midbottom=(600, 300))
# Player rect
player_rect = player_surface.get_rect(midbottom=(80, 300))
# Text rect
score_rect = score_surface.get_rect(midbottom=(400, 50))
# Ellipse rect
ellipse_rect = pygame.Rect(50, 200, 100, 100)

# Gravity
player_gravity = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_gravity = -20

    # Background images
    screen.blit(source=sky_surface, dest=(0, 0))
    screen.blit(source=ground_surface, dest=(0, 300))
    # Text
    pygame.draw.rect(screen, box_color, score_rect, 10, 10)
    screen.blit(source=score_surface, dest=score_rect)
    # Snail Animation
    snail_rect.right = (snail_rect.right -
                        5) if snail_rect.right >= -10 else 815
    screen.blit(source=snail_surface, dest=snail_rect)
    # Player
    player_gravity += 1
    player_rect.y += player_gravity

    # The player can't go below the floor (y = 300px)
    if player_rect.bottom > 300:
        player_rect.bottom = 300

    screen.blit(source=player_surface, dest=player_rect)

    pygame.display.update()
    clock.tick(60)

# End pygame
pygame.quit()
