from src.classes.enums.Direction import Direction
import pygame
from pygame.sprite import Sprite


class Snake(Sprite):
    def __init__(self):
        super().__init__()

        self.size = 20
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill('#389844')
        self.rect = self.image.get_rect(x=20, y=20)
        self.current_direction = Direction
        self.current_direction = Direction.DOWN
        self.px_count = 0

    def set_direction(self, direction):
        match direction:
            case Direction.UP:
                if self.current_direction != Direction.DOWN:
                    self.current_direction = Direction.UP
            case Direction.DOWN:
                if self.current_direction != Direction.UP:
                    self.current_direction = Direction.DOWN
            case Direction.LEFT:
                if self.current_direction != Direction.RIGHT:
                    self.current_direction = Direction.LEFT
            case Direction.RIGHT:
                if self.current_direction != Direction.LEFT:
                    self.current_direction = Direction.RIGHT

    def move(self):
        """
            The game has 60 frames per second -> If we increase Each frame by:
                - 0.1 px_count -> 0.1 * 60 = 6px in 1 second
                - 0.2 px_count -> 0.2 * 60 = 12px in 1 second
                - 0.3 px_count -> 0.3 * 60 = 18px in 1 second
                - 0.4 px_count -> 0.4 * 60 = 24px in 1 second
                And so on
            And we just increase the value when the px_count variable hits 20px or more
        """
        self.px_count += 0.6
        if self.px_count <= 20:
            return

        # Reestar px_count
        self.px_count -= 20
        # Move snake
        match self.current_direction:
            case Direction.UP:
                self.go_up()
            case Direction.DOWN:
                self.go_down()
            case Direction.LEFT:
                self.go_left()
            case Direction.RIGHT:
                self.go_right()

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
        self.move()
