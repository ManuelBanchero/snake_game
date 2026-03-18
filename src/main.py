import pygame
from pygame.sprite import Sprite, GroupSingle

SCREEN_WIDTH = 400
SCREEN_HEIGTH = 400


class Game():
    def __init__(self):
        # Screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
        # Box
        px_diff = 70
        box_width = SCREEN_WIDTH - px_diff
        box_height = SCREEN_HEIGTH - px_diff
        self.game_box_surf = pygame.Surface((box_width, box_height))
        self.game_box = self.game_box_surf.get_rect(
            topleft=(px_diff // 2, px_diff // 2))
        self.box_border = 5
        # Box limits (the 5 value comes from the box with)
        self.start_x_limit = px_diff // 2 + self.box_border
        self.start_y_limit = px_diff // 2 + self.box_border
        self.end_x_limit = box_width + self.box_border * 2
        self.end_y_limit = box_height + self.box_border * 2
        # Snake group
        self.snake_group = GroupSingle()
        # Will have the snake class after Game.initialie() method is executed
        self.snake = None

    # Use it before run the game
    def initialize(self):
        # Add snake
        self.snake_group.add(Snake())
        self.snake = self.snake_group.sprite

    def set_limits(self, rect):
        if rect.get_x() < self.start_x_limit:
            rect.set_x(self.start_x_limit)
        if rect.get_x() > self.end_x_limit:
            rect.set_x(self.end_x_limit)
        if rect.get_y() < self.start_y_limit:
            rect.set_y(self.start_y_limit)
        if rect.get_y() > self.end_y_limit:
            rect.set_y(self.end_y_limit)

    # Use it while running the game
    def update(self):
        # Screen styles
        self.screen.fill('#0c200d')
        # Box variables
        pygame.draw.rect(self.screen, '#98e5a5',
                         self.game_box, self.box_border)
        # Snake
        self.snake_group.draw(self.screen)
        self.snake_group.update()
        self.set_limits(self.snake)


class Snake(Sprite):
    def __init__(self):
        super().__init__()

        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill('#389844')
        self.rect = self.image.get_rect(x=20, y=20)

    def user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.go_down()
        if keys[pygame.K_UP]:
            self.go_up()
        if keys[pygame.K_RIGHT]:
            self.go_right()
        if keys[pygame.K_LEFT]:
            self.go_left()

    def go_down(self):
        self.rect.y += 20

    def go_up(self):
        self.rect.y -= 20

    def go_left(self):
        self.rect.x -= 20

    def go_right(self):
        self.rect.x += 20

    def get_x(self):
        return self.rect.x

    def get_y(self):
        return self.rect.y

    def set_x(self, x):
        self.rect.x = x

    def set_y(self, y):
        self.rect.y = y

    def update(self):
        self.user_input()


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
