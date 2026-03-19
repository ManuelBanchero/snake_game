import pygame
from pygame.sprite import GroupSingle, Group, spritecollide
from src.classes.enums.Direction import Direction
from src.classes.Snake import Snake
from src.config.config import SCREEN_WIDTH, SCREEN_HEIGTH
from src.classes.Apple import Apple


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

        # Box limits
        self.start_x_limit = px_diff // 2 + self.box_border
        self.start_y_limit = px_diff // 2 + self.box_border
        self.end_x_limit = box_width + self.box_border * 2
        self.end_y_limit = box_height + self.box_border * 2

        # Snake group
        self.snake_group = GroupSingle()
        # Will have the snake class after Game.initialie() method is executed
        self.snake = None

        # Tail Group
        self.tail_group = Group()

        # Apple Group
        self.apple_group = Group()

    # Use it before run the game
    def initialize(self):
        # Add snake
        self.snake_group.add(Snake())
        self.snake = self.snake_group.sprite

        # Add an apple
        self.apple_group.add(Apple())

    def set_limits(self, rect):
        if rect.get_x() < self.start_x_limit:
            rect.set_x(self.start_x_limit)
        if rect.get_x() > self.end_x_limit:
            rect.set_x(self.end_x_limit)
        if rect.get_y() < self.start_y_limit:
            rect.set_y(self.start_y_limit)
        if rect.get_y() > self.end_y_limit:
            rect.set_y(self.end_y_limit)

    def user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.snake.set_direction(Direction.DOWN)
        if keys[pygame.K_UP]:
            self.snake.set_direction(Direction.UP)
        if keys[pygame.K_LEFT]:
            self.snake.set_direction(Direction.LEFT)
        if keys[pygame.K_RIGHT]:
            self.snake.set_direction(Direction.RIGHT)

    def snake_eats_apple(self):
        if spritecollide(self.snake, self.apple_group, True):
            return True
        return False

    # Use it while running the game
    def update(self):
        # Screen styles
        self.screen.fill('#0c200d')
        # Box variables
        pygame.draw.rect(self.screen, '#98e5a5',
                         self.game_box, self.box_border)
        # User interactions
        self.user_input()

        # Apple
        self.apple_group.draw(self.screen)
        self.apple_group.update()

        # Snake
        self.snake_group.draw(self.screen)
        self.snake_group.update()
        self.set_limits(self.snake)

        if self.snake_eats_apple():
            print('Apple has been eaten')
