import pygame
import os
import random
import constants as c

class Donut:
    def __init__(self, obstacle:pygame.Surface):
        self.plain_donut_load = pygame.image.load(os.path.join("downloads", "plain_donut.png"))
        self.plain_donut_load = pygame.transform.scale(self.plain_donut_load, c.DONUT_TILE_SIZE)

        self.chocolate_donut_load = pygame.image.load(os.path.join("downloads", "chocolate_donut.png"))
        self.chocolate_donut_load = pygame.transform.scale(self.chocolate_donut_load, c.DONUT_TILE_SIZE)

        self.pink_donut_load = pygame.image.load(os.path.join("downloads", "pink_donut.png"))
        self.pink_donut_load = pygame.transform.scale(self.pink_donut_load, (c.DONUT_TILE_SIZE[0] + 10, c.DONUT_TILE_SIZE[1] + 10))
        
        self.plain_donut = pygame.Surface((c.DONUT_TILE_SIZE[0], c.DONUT_TILE_SIZE[1]), pygame.SRCALPHA)
        self.plain_donut.blit(self.plain_donut_load, (0, 0))
        self.plain_donut_rect = self.plain_donut.get_rect()

        self.chocolate_donut = pygame.Surface((c.DONUT_TILE_SIZE[0], c.DONUT_TILE_SIZE[1]), pygame.SRCALPHA)
        self.chocolate_donut.blit(self.chocolate_donut_load, (0, 0))
        self.chocolate_donut_rect = self.chocolate_donut.get_rect()

        self.pink_donut = pygame.Surface(((c.DONUT_TILE_SIZE[0] + 10), (c.DONUT_TILE_SIZE[1] + 10)), pygame.SRCALPHA)
        self.pink_donut.blit(self.pink_donut_load, (0, 0))
        self.pink_donut_rect = self.pink_donut.get_rect()

        self.image = None
        self.rect = None
        random_num = random.randrange(0, 10)
        if random_num == 0 or random_num == 1:
            self.image = self.chocolate_donut
            self.rect = self.chocolate_donut_rect
        elif random_num == 2:
            self.image = self.pink_donut
            self.rect = self.pink_donut_rect
        else:
            self.image = self.plain_donut
            self.rect = self.plain_donut_rect
        
        self.x = c.WIDTH + (0.5 * c.OBSTACLE_TILE_SIZE[0]) + c.DONUT_TILE_SIZE[0]
        self.y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - c.DONUT_TILE_SIZE[1]
        
        if obstacle == 1 or obstacle == 3:
            self.y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - c.DONUT_TILE_SIZE[1]
        else:
            self.y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - 3 * c.OBSTACLE_TILE_SIZE[1] - c.DONUT_TILE_SIZE[1] - 30