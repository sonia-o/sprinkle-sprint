import pygame
import os
import random
import constants as c

class Obstacle:
    def __init__(self):
        self.cheese_left = pygame.image.load(os.path.join("downloads", "cheese_left.png"))
        self.cheese_left = pygame.transform.scale(self.cheese_left, c.OBSTACLE_TILE_SIZE)

        self.cheese_middle = pygame.image.load(os.path.join("downloads", "cheese_middle.png"))
        self.cheese_middle = pygame.transform.scale(self.cheese_middle, c.OBSTACLE_TILE_SIZE)

        self.cheese_right = pygame.image.load(os.path.join("downloads", "cheese_right.png"))
        self.cheese_right = pygame.transform.scale(self.cheese_right, c.OBSTACLE_TILE_SIZE)

        self.candy_cane_stick = pygame.image.load(os.path.join("downloads", "candy_cane_stick.png"))
        self.candy_cane_stick = pygame.transform.scale(self.candy_cane_stick, c.OBSTACLE_TILE_SIZE)

        self.candy_cane_top = pygame.image.load(os.path.join("downloads", "candy_cane_top.png"))
        self.candy_cane_top = pygame.transform.scale(self.candy_cane_top, c.OBSTACLE_TILE_SIZE)

        self.cracker_left = pygame.image.load(os.path.join("downloads", "cracker_left.png")).convert_alpha()
        self.cracker_left = pygame.transform.scale(self.cracker_left, c.OBSTACLE_TILE_SIZE)

        self.cracker_right = pygame.image.load(os.path.join("downloads", "cracker_right.png")).convert_alpha()
        self.cracker_right = pygame.transform.scale(self.cracker_right, c.OBSTACLE_TILE_SIZE)

        self.plain_sausage_bite = pygame.image.load(os.path.join("downloads", "plain_sausage_bite.png"))
        self.plain_sausage_bite = pygame.transform.scale(self.plain_sausage_bite, c.OBSTACLE_TILE_SIZE)

        self.plain_sausage_left = pygame.image.load(os.path.join("downloads", "plain_sausage_left.png"))
        self.plain_sausage_left = pygame.transform.scale(self.plain_sausage_left, c.OBSTACLE_TILE_SIZE)

        self.plain_sausage_middle = pygame.image.load(os.path.join("downloads", "plain_sausage_middle.png"))
        self.plain_sausage_middle = pygame.transform.scale(self.plain_sausage_middle, c.OBSTACLE_TILE_SIZE)

        self.plain_sausage_right = pygame.image.load(os.path.join("downloads", "plain_sausage_right.png"))
        self.plain_sausage_right = pygame.transform.scale(self.plain_sausage_right, c.OBSTACLE_TILE_SIZE)

        self.small_biscuit = pygame.image.load(os.path.join("downloads", "small_biscuit.png"))
        self.small_biscuit = pygame.transform.scale(self.small_biscuit, c.OBSTACLE_TILE_SIZE)
    

        self.candy_cane = pygame.Surface((c.OBSTACLE_TILE_SIZE[0], 2 * c.OBSTACLE_TILE_SIZE[1]), pygame.SRCALPHA)
        self.candy_cane.blit(self.candy_cane_top, (0, 0))
        self.candy_cane.blit(self.candy_cane_stick, (0, c.OBSTACLE_TILE_SIZE[1]))
        self.candy_cane_rect = self.candy_cane.get_rect()

        self.cheese = pygame.Surface((3 * c.OBSTACLE_TILE_SIZE[0], c.OBSTACLE_TILE_SIZE[1]), pygame.SRCALPHA)
        self.cheese.blit(self.cheese_left, (0, 0))
        self.cheese.blit(self.cheese_middle, (c.OBSTACLE_TILE_SIZE[0], 0))
        self.cheese.blit(self.cheese_right, (2 * c.OBSTACLE_TILE_SIZE[0], 0))
        self.cheese_rect = self.cheese.get_rect()

        self.sausage = pygame.Surface((3 * c.OBSTACLE_TILE_SIZE[0], c.OBSTACLE_TILE_SIZE[1]), pygame.SRCALPHA)
        self.sausage.blit(self.plain_sausage_left, (0, 0))
        self.sausage.blit(self.plain_sausage_middle, (c.OBSTACLE_TILE_SIZE[0], 0))
        self.sausage.blit(self.plain_sausage_right, (2 * c.OBSTACLE_TILE_SIZE[0], 0))
        self.sausage_rect = self.sausage.get_rect()

        self.biscuit = pygame.Surface((c.OBSTACLE_TILE_SIZE[0], c.OBSTACLE_TILE_SIZE[1]), pygame.SRCALPHA)
        self.biscuit.blit(self.small_biscuit, (0, 0))
        self.biscuit_rect = self.biscuit.get_rect()

        self.image = None
        self.rect = None
        self.x_shift = None
        self.y_shift = None
        self.random_num = random.randrange(0, 4)
        if self.random_num == 0:
            self.image = self.candy_cane
            self.rect = self.candy_cane_rect
            self.x_shift = 1
            self.y_shift = 2
        elif self.random_num == 1:
            self.image = self.cheese
            self.rect = self.cheese_rect
            self.x_shift = 0
            self.y_shift = 2
        elif self.random_num == 2 :
            self.image = self.biscuit
            self.rect = self.biscuit_rect
            self.x_shift = 1
            self.y_shift = 1
        else:
            self.image = self.sausage
            self.rect = self.sausage_rect
            self.x_shift = 0
            self.y_shift = 2
        self.x = c.WIDTH + self.x_shift * c.OBSTACLE_TILE_SIZE[0]
        self.y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - self.y_shift * c.OBSTACLE_TILE_SIZE[1]