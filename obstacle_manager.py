import pygame
import constants as c
from obstacle import Obstacle

class Obstacle_Manager:
    def __init__(self):
        self.obstacles_list = []

        self.obstacle_frequency = 2000

        #CHAT GPT -------------------
        self.ADD_OBJECT_EVENT = pygame.USEREVENT + 1
        # pygame.time.set_timer(self.ADD_OBJECT_EVENT, self.obstacle_frequency)

        # self.ADD_OBJECT_EVENT_FAST = pygame.USEREVENT + 1
        # pygame.time.set_timer(self.ADD_OBJECT_EVENT_FAST, 800)

        # self.ADD_OBJECT_EVENT_EXPERT = pygame.USEREVENT + 1
        # pygame.time.set_timer(self.ADD_OBJECT_EVENT_EXPERT, 200)
        #----------------------------

    #Chat GPT logic modified to use premade obstacles with randomized occurrences -------------------
    def create_obstacle(self) -> None:
        self.obstacles_list.append(Obstacle())

    def update_obstacles(self, speed) -> None:
        for obj in self.obstacles_list:
            obj.x -= speed
            obj.rect.topleft = (obj.x, obj.y)
        self.obstacles_list = [obj for obj in self.obstacles_list if obj.x > -3 * c.OBSTACLE_TILE_SIZE[0]]
    #----------------------------

    def draw_obstacles(self, screen:pygame.Surface) -> None:
        for obj in self.obstacles_list:
            screen.blit(obj.image, (obj.x, obj.y))

    def reset_obstacles(self) -> None:
        self.obstacles_list.clear()