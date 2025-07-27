# pygame template

import pygame
import os
import constants as c

class Sprite:
    def __init__(self):
        self.x_pos = 30
        self.y_pos = 300
        self.current_pos = 2  ## 1 for up, 2 for normal, 3 for down
        self.down = False     ## Tracks if the sprite has reached the top and is now falling down

        self.sprite_height = 70
        self.sprite_width = 40
        
        self.character_type = 0
        self.sprite = pygame.image.load(os.path.join("downloads/shop_menu", c.CHARACTER[self.character_type]))
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite_width, self.sprite_height))
        self.sprite_rect = self.sprite.get_rect()
        self.sprite_down = pygame.transform.rotate(self.sprite, 270)
        self.sprite_down_rect = self.sprite_down.get_rect()
        
        self.draw_image = self.sprite

        # self.max = c.HEIGHT - c.CLOSE_TILE_SIZE[1]
        # # self.max = 300
        # self.min = 150
        # self.default = 320

        self.min = c.HEIGHT - c.CLOSE_TILE_SIZE[1]- (self.sprite_height * 3.5)
        self.default = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - self.sprite_height
        self.sprite_down_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - self.sprite_width
        print(self.down)

# ----------------------------------------------------
# functions
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.current_pos = 3
            self.draw_image = self.sprite_down
            self.y_pos = self.sprite_down_y
            self.current_pos = 2

        if keys[pygame.K_UP]:
            self.current_pos = 1

    def draw_up(self, screen:pygame) -> pygame.Surface: 
        screen.blit(self.draw_image, (self.x_pos, self.y_pos))
        self.sprite_rect.topleft = (self.x_pos, self.y_pos)

    def sprite_update(self, current_sprite):
        self.sprite = pygame.image.load(os.path.join("downloads/shop_menu", c.CHARACTER[current_sprite]))
        self.sprite = pygame.transform.scale(self.sprite, (self.sprite_width, self.sprite_height))
        self.sprite_down = pygame.transform.rotate(self.sprite, 270)
        self.draw_image = self.sprite
        fall_rate = 1
        rise_rate = 1
        if self.current_pos == 1:
            if self.y_pos > self.min and self.down == False:
                rise_rate = rise_rate*15
                self.y_pos -= rise_rate
                if self.y_pos <= self.min:
                    self.down = True ## If the sprite reach the top, then it will be set as true
            if self.down:
                if self.y_pos < self.default:
                    fall_rate = fall_rate*8
                    self.y_pos += fall_rate
                elif self.y_pos >= self.default:
                    self.down = False
                    self.current_pos = 2
                    self.sprite_update(current_sprite) # replaced continue
        else:
            self.move()

    def before_draw(self, screen):
        self.draw_up(screen)
        if self.current_pos == 2:
            self.y_pos = self.default
            # self.y_pos = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - sprite_size