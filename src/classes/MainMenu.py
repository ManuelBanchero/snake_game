import pygame
from src.config.config import SCREEN_WIDTH, SCREEN_HEIGTH


class MainMenu():
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

        # Fonts
        title_font = pygame.font.Font(
            'src/assets/fonts/Jersey10-Regular.ttf', 70)
        text_font = pygame.font.Font(
            'src/assets/fonts/Jersey10-Regular.ttf', 30)

        self.title_surf = title_font.render('Snake.py', False, '#98e5a5')
        self.title_rect = self.title_surf.get_rect(midbottom=(200, 170))

        self.text_surf = text_font.render(
            'Press space to start the game', False, '#98e5a5')
        self.text_rect = self.text_surf.get_rect(midbottom=(200, 280))

        # Images
        snake_img = pygame.image.load(
            'src/assets/images/Neon_Green_Pixel_Snake_Art.png').convert_alpha()
        self.snake_surf = pygame.transform.scale(snake_img, (120, 120))
        self.snake_rect = self.snake_surf.get_rect(midbottom=(200, 140))

    def update(self):
        self.screen.fill('#0c200d')
        self.screen.blit(self.title_surf, self.title_rect)
        self.screen.blit(self.snake_surf, self.snake_rect)
        self.screen.blit(self.text_surf, self.text_rect)
