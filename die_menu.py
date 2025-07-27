import pygame
import os
import constants as c

class DieMenu:
    def __init__(self):
        self.ok_button = pygame.image.load(os.path.join("downloads", "shop_menu", "ok_button.png"))
        self.ok_button = pygame.transform.scale(self.ok_button, (130, 65))
        self.ok_button_rect = self.ok_button.get_rect()

        self.quit_button = pygame.image.load(os.path.join("downloads", "quitbutton.png"))
        self.quit_button = pygame.transform.scale(self.quit_button, (150, 100))
        self.quit_button_rect = self.quit_button.get_rect()

        self.font = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 60)
        self.TEXT_COLOUR = (0, 0, 0)

    def draw_text(self, text, font, color, x, y, screen):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

    def draw_death_menu(self, screen:pygame.Surface, colour: tuple[int]) -> None:
        screen.fill(colour)
        screen.blit(self.ok_button, (255, 200))
        self.ok_button_rect.topleft = (255, 200)
        self.draw_text("You Died!", self.font, self.TEXT_COLOUR, 175, 100, screen) 