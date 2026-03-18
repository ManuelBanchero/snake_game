import pygame
from pygame.sprite import Sprite, GroupSingle, Group
import random


class Obstacle(Sprite):
    def __init__(self, type):
        super().__init__()
        y_pos = 0
        self.frames = []
        if type == 'fly':
            fly_1 = pygame.image.load(
                'src/graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load(
                'src/graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        elif type == 'snail':
            snail_1 = pygame.image.load(
                'src/graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load(
                'src/graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(
            midbottom=(random.randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1

        if self.animation_index >= len(self.frames):
            self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]

    def move_obstacle(self):
        self.rect.x -= 5

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state()
        self.move_obstacle()
        self.destroy()


class Player(Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load(
            'src/graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load(
            'src/graphics/player/player_walk_2.png').convert_alpha()

        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load(
            'src/graphics/player/jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('src/audio/jump.mp3')
        self.jump_sound.set_volume(0.1)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        # The player can't go below the floor (y = 300px)
        if self.rect.bottom > 300:
            self.rect.bottom = 300

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1

            if self.player_index >= len(self.player_walk):
                self.player_index = 0

            self.image = self.player_walk[int(self.player_index)]

    def reestart_position(self):
        self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()


def collision():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, True):
        return True
    return False


def display_score():
    current_time = (pygame.time.get_ticks() - game_timer) // 1000
    score_surface = test_font.render(f'{current_time}', False, text_color)
    score_rect = score_surface.get_rect(midbottom=(400, 50))
    screen.blit(source=score_surface, dest=score_rect)

    return current_time


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
over_box_color = '#5e81a2'

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
# Intro Texts
game_title_surface = test_font.render('My game!', False, 'Black')
game_instructrions_surface = test_font.render(
    'Press "Space" to start the game!', False, 'Black')
""" 
CREATE RECTANGLES FOR THE SURFACES
"""
# Text
game_title_rect = game_title_surface.get_rect(center=(400, 50))
game_instructrions_rect = game_instructrions_surface.get_rect(
    center=(400, 350))

"""
CUSTOM EVENTS
"""
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

"""
VARIABLES
"""
bg_music = pygame.mixer.Sound('src/audio/music.wav')
bg_music.set_volume(0.1)
bg_music.play(loops=-1)
enemies = ['snail', 'snail', 'fly']
obstacle_rect_list = []
score = 0
player_gravity = 0
game_timer = 0
game_active = False
running = True

"""
OOP
"""
player = GroupSingle()
player.add(Player())

obstacle_group = Group()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue
        if game_active:
            if event.type == obstacle_timer:
                obstacle_type = random.choice(enemies)
                obstacle_group.add(Obstacle(obstacle_type))
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    game_timer = pygame.time.get_ticks()
                    player.sprite.reestart_position()

    if game_active:
        # Background images
        screen.blit(source=sky_surface, dest=(0, 0))
        screen.blit(source=ground_surface, dest=(0, 300))
        # Text
        score = display_score()
        # OOP
        player.draw(screen)
        player.update()
        obstacle_group.draw(screen)
        obstacle_group.update()

        # If the player collides w/snail or fly -> GAME OVER
        if collision():
            obstacle_group.empty()
            game_active = False
            continue
    else:
        screen.fill(over_box_color)
        screen.blit(game_title_surface, game_title_rect)
        game_score_surface = test_font.render(
            f'Score: {score}', False, 'Black')
        game_score_rect = game_score_surface.get_rect(center=(400, 100))
        screen.blit(game_score_surface, game_score_rect)
        screen.blit(game_instructrions_surface, game_instructrions_rect)

        # Delete enemies
        obstacle_rect_list.clear()

    pygame.display.update()
    clock.tick(60)

# End pygame
pygame.quit()
