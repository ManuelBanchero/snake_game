import pygame
from pygame.sprite import Sprite
from config.config import BOX_SIZE
from abc import ABC, abstractmethod


class BoxElement(Sprite, ABC):
    def __init__(self, color, x_pos, y_pos):
        super().__init__()
        self.size = BOX_SIZE
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(color)
        self.rect = self.image.get_rect(x=x_pos, y=y_pos)

    @abstractmethod
    def update(self, *args, **kwargs):
        pass
