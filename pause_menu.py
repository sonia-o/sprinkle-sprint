import pygame
import os
import constants as c

class PauseMenu:
    def __init__(self):
        # Define fonts
        self.font = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 25)
        # Define colors
        self.TEXT_COLOUR = (0, 0, 0)
        # Load button images
        self.play_img = pygame.image.load(os.path.join("downloads", "pause_menu", "play_button.png")).convert_alpha()
        self.play_img = pygame.transform.scale(self.play_img, (80, 80))
        self.play_rect = self.play_img.get_rect()
        
        self.quit_img = pygame.image.load(os.path.join("downloads", "pause_menu", "quit_button.png")).convert_alpha()
        self.quit_img = pygame.transform.scale(self.quit_img, (80, 80))
        self.quit_rect = self.quit_img.get_rect()

    def load_buttons(self):
       button_info = [("play_button.png", "Resume"), ("quit_button.png", "Quit")]
       for img_name, text in button_info:
           img = pygame.image.load(os.path.join("downloads", "pause_menu", img_name)).convert_alpha()
           img = pygame.transform.scale(img, (80, 80))
           rect = img.get_rect()
           self.buttons.append((img, rect, text))
    def draw_text(self, text, font, color, x, y, screen):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

    def draw_pause_menu(self, screen, colour_index):
        pygame.display.set_caption("Pause Menu")
        screen.fill(c.COLOURS[colour_index])
        screen.blit(self.play_img, (200, 100))
        self.play_rect.topleft = (200, 100)
        self.draw_text(" Resume", self.font, self.TEXT_COLOUR, 300, 120, screen)

        screen.blit(self.quit_img, (200, 200))
        self.quit_rect.topleft = (200, 200)
        self.draw_text(" Quit", self.font, self.TEXT_COLOUR, 300, 220, screen)
        