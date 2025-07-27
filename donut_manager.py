import pygame
import constants as c
from donut import Donut

class Donut_Manager:
    def __init__(self):
        self.donut_list = []

        #CHAT GPT -------------------
        self.ADD_OBJECT_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADD_OBJECT_EVENT, 2000)
        #----------------------------

    #Chat GPT logic modified to use premade obstacles with randomized occurrences -------------------
    def create_donut(self, obstacle:pygame.Surface) -> None:
        self.donut_list.append(Donut(obstacle))

    def update_donuts(self, speed) -> None:
        for donut in self.donut_list:
            donut.x -= speed
            donut.rect.topleft = (donut.x, donut.y)
        self.donut_list = [donut for donut in self.donut_list if donut.x > -2 * c.DONUT_TILE_SIZE[0]]    
    #----------------------------

    def draw_donuts(self, screen:pygame.Surface) -> None:
        for donut in self.donut_list:
            screen.blit(donut.image, (donut.x, donut.y))
    
    def reset_donuts(self) -> None:
        self.donut_list.clear()