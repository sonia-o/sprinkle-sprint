import pygame
import button
import os
import constants as c

class Menu:
    def __init__(self):
        pygame.display.set_caption("Menu")
        self.clock = pygame.time.Clock()
        self.running = True
        self.size = c.WIDTH, c.HEIGHT
        # Game variables
        self.menu_state = "menu"
        # Define fonts
        self.font = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 25)
        # Define colors
        self.TEXT_COLOUR = (0, 0, 0)
        # Load button images
        self.pause_img = pygame.image.load(os.path.join("downloads", "pause_menu", "pause.png")).convert_alpha()
        self.play_img = pygame.image.load(os.path.join("downloads", "pause_menu", "play_button.png")).convert_alpha()
        self.quit_img = pygame.image.load(os.path.join("downloads", "pause_menu", "quit_button.png")).convert_alpha()
        self.volumeoff_img = pygame.image.load(os.path.join("downloads", "pause_menu", "volume_off.png")).convert_alpha()
        self.volumeon_img = pygame.image.load(os.path.join("downloads", "pause_menu", "volume_on.png")).convert_alpha()

        # Create button instances
        self.pause_button = button.Button(50, 0, self.pause_img, 0.1)
        self.play_button = button.Button(50, 70, self.play_img, 0.1)
        self.quit_button = button.Button(50, 140, self.quit_img, 0.1)
        self.volumeon_button = button.Button(50, 210, self.volumeon_img, 0.1)
        self.volumeoff_button = button.Button(50, 280, self.volumeoff_img, 0.1)
        self.surface = pygame.Surface((640, 400))

        # Variable to control game pause state
        self.game_paused = False

        # Variable to control main loop
        self.running = True

    def draw_text(self, text, font, color, x, y, screen):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

    def draw(self, screen):
        screen.fill((255, 192, 203))

        if self.menu_state == "menu":
            # Draw pause screen buttons
            if self.play_button.draw(screen):
                self.game_paused = False
            else:
                self.draw_text(" Resume", self.font, self.TEXT_COLOUR, 100, 70, screen)
            if self.quit_button.draw(screen):
                self.running = False  # Set running to False to exit the loop
            else:
                self.draw_text(" Quit", self.font, self.TEXT_COLOUR, 100, 140, screen)
            # Check if the menu is open
            # Draw the different menu buttons
            if self.volumeoff_button.draw(screen):
                print("volume Settings")
            else:
                self.draw_text(" ON", self.font, self.TEXT_COLOUR, 100, 210, screen)
            if self.volumeon_button.draw(screen):
                print("volume Settings")
            else:
                self.draw_text(" OFF", self.font, self.TEXT_COLOUR, 100, 280, screen)
        else:
            self.draw_text("Press SPACE to pause", self.font, self.TEXT_COLOUR, 180, 190, screen)

    def run_menu(self, screen):
        while self.running:  # Use self.running to control the loop
            self.draw(screen)

            # Event handler
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_paused = True
                elif event.type == pygame.QUIT:
                    self.handle_quit_button()  # Call the quit button handler method