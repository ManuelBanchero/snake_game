import pygame
from pygame.sprite import GroupSingle, Group, spritecollide
from src.classes.enums.Direction import Direction
from src.classes.Snake import Snake
from src.classes.Apple import Apple
from src.classes.Tail import Tail
from src.config.config import SCREEN_WIDTH, SCREEN_HEIGTH
from random import randint


class Game():
    def __init__(self):
        # Screen
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

        # Box
        px_diff = 40
        box_width = SCREEN_WIDTH - px_diff
        box_height = SCREEN_HEIGTH - px_diff
        self.game_box_surf = pygame.Surface((box_width, box_height))
        self.game_box = self.game_box_surf.get_rect(
            topleft=(px_diff // 2, px_diff // 2))
        self.box_border = 20

        # Box limits
        self.start_x_limit = px_diff // 2 + self.box_border
        self.start_y_limit = px_diff // 2 + self.box_border
        self.end_x_limit = box_width - self.box_border
        self.end_y_limit = box_height - self.box_border

        # Snake group
        self.snake_group = GroupSingle()
        # Will have the snake class after Game.initialie() method is executed
        self.snake = None
        self.snake_positions = [(0, 0)]

        # Tail Group
        self.tail_group = Group()

        # Apple Group
        self.apple_group = Group()

        # Score (or amount of apple eaten)
        self.score = 0

    # Use it before run the game
    def initialize(self):
        # Add snake
        self.snake_group.add(Snake())
        self.snake = self.snake_group.sprite

        # Add an apple
        x, y = self.get_random_pos()
        self.apple_group.add(Apple(x, y))

    def snake_hit_limits(self):
        if self.snake.get_x() < self.start_x_limit:
            return True
        if self.snake.get_x() > self.end_x_limit:
            return True
        if self.snake.get_y() < self.start_y_limit:
            return True
        if self.snake.get_y() > self.end_y_limit:
            return True

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

    def snake_hits_tail(self):
        if spritecollide(self.snake, self.tail_group, False):
            return True
        return False

    def get_random_pos(self):
        return self.get_valid_pos()

    def get_valid_pos(self):
        # This gives me the amount of grids I have in x and y (ex: (340px - 40px) // 20px)
        grids_x = ((self.end_x_limit - self.start_x_limit) //
                   self.snake.size) - 1
        grids_y = ((self.end_y_limit - self.start_y_limit) //
                   self.snake.size) - 1

        while True:
            random_index_x = randint(0, grids_x)
            random_index_y = randint(0, grids_y)

            random_grid_x = self.start_x_limit + \
                (random_index_x * self.snake.size)
            random_grid_y = self.start_y_limit + \
                (random_index_y * self.snake.size)

            if (random_grid_x, random_grid_y) not in self.snake_positions:
                return random_grid_x, random_grid_y

    def reset(self):
        # Clear tails
        self.tail_group.empty()
        # Set snake to start position
        self.snake.set_x(80)
        self.snake.set_y(80)
        # Set snake direction to down
        self.snake.set_direction(Direction.DOWN)
        # Empty snake positions
        self.snake_positions.clear()
        self.snake_positions.append((80, 80))
        self.snake.px_count = 0
        # Clear apple
        self.apple_group.empty()
        # Set apple to a new position
        x, y = self.get_random_pos()
        self.apple_group.add(Apple(x, y))
        # Reset score
        self.score = 0

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

        # Tail
        self.tail_group.draw(self.screen)
        self.tail_group.update()

        # Snake
        self.snake_group.draw(self.screen)
        self.snake_group.update()

        # Move snake and set position
        x_pos, y_pos = self.snake.move()
        if x_pos != -1 and y_pos != -1:
            self.snake_positions.append((x_pos, y_pos))
            # The list always needs to be one more than the score
            if len(self.snake_positions) > self.score + 1:
                # Delete the extra item (the first element of the array)
                del self.snake_positions[:1]

            for i, tail in enumerate(self.tail_group):
                # If is the last element -> is the curren snake position (we don't wanna use it)
                if i == len(self.snake_positions) - 1:
                    continue

                # Update tail pos
                tail_x, tail_y = self.snake_positions[i]
                tail.set_pos(tail_x, tail_y)

        # Snake an apple collision
        if self.snake_eats_apple():
            x, y = self.get_random_pos()
            self.apple_group.add(Apple(x, y))
            self.score += 1

            # Create a new Tail
            self.tail_group.add(Tail(-200, -200))
