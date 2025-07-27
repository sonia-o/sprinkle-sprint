# pygame template

import pygame
import os
import constants as c

class Background:
    def __init__(self):
        self.floor_tile_x = 4
        self.floor_tile_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1]

        self.long_cloud_x = c.WIDTH + 20
        self.long_cloud_y = 150

        self.long_cloud_2_x = c.WIDTH + 550
        self.long_cloud_2_y = 60

        self.small_cloud_1_x = c.WIDTH + 150
        self.small_cloud_1_y = 20

        self.small_cloud_2_x = c.WIDTH + 380
        self.small_cloud_2_y = 80

        self.cake_back_prop_x = 0
        self.cake_back_prop_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - 5 * c.DISTANT_TILE_SIZE[1]

        self.trees_back_prop_x = 9 * c.DISTANT_TILE_SIZE[0]
        self.trees_back_prop_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - (7 * c.DISTANT_TILE_SIZE[1])

        self.trophy_back_prop_x = 19 * c.DISTANT_TILE_SIZE[0]
        self.trophy_back_prop_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - 6 * c.DISTANT_TILE_SIZE[1]

        self.floor_tile = pygame.image.load(os.path.join("downloads", "floor.png"))
        self.floor_tile = pygame.transform.scale(self.floor_tile, c.CLOSE_TILE_SIZE)

        self.cloud_left = pygame.image.load(os.path.join("downloads", "cloud_left.png"))
        self.cloud_left = pygame.transform.rotate(self.cloud_left, 180)
        self.cloud_left = pygame.transform.scale(self.cloud_left, c.CLOUD_TILE_SIZE)

        self.cloud_middle = pygame.image.load(os.path.join("downloads", "cloud_middle.png"))
        self.cloud_middle = pygame.transform.rotate(self.cloud_middle, 180)
        self.cloud_middle = pygame.transform.scale(self.cloud_middle, c.CLOUD_TILE_SIZE)

        self.cloud_right = pygame.image.load(os.path.join("downloads", "cloud_right.png"))
        self.cloud_right = pygame.transform.rotate(self.cloud_right, 180)
        self.cloud_right = pygame.transform.scale(self.cloud_right, c.CLOUD_TILE_SIZE)

        self.cake_left = pygame.image.load(os.path.join("downloads", "cake_left.png"))
        self.cake_left = pygame.transform.scale(self.cake_left, c.DISTANT_TILE_SIZE)

        self.cake_middle = pygame.image.load(os.path.join("downloads", "cake_middle.png"))
        self.cake_middle = pygame.transform.scale(self.cake_middle, c.DISTANT_TILE_SIZE)

        self.cake_right = pygame.image.load(os.path.join("downloads", "cake_right.png"))
        self.cake_right = pygame.transform.scale(self.cake_right, c.DISTANT_TILE_SIZE)

        self.cake_top_left = pygame.image.load(os.path.join("downloads", "cake_top_left.png"))
        self.cake_top_left = pygame.transform.scale(self.cake_top_left, c.DISTANT_TILE_SIZE)

        self.cake_top_middle = pygame.image.load(os.path.join("downloads", "cake_top_middle.png"))
        self.cake_top_middle = pygame.transform.scale(self.cake_top_middle, c.DISTANT_TILE_SIZE)

        self.cake_top_right = pygame.image.load(os.path.join("downloads", "cake_top_right.png"))
        self.cake_top_right = pygame.transform.scale(self.cake_top_right, c.DISTANT_TILE_SIZE)

        self.cake_curve_left = pygame.image.load(os.path.join("downloads", "curve_cake_left.png"))
        self.cake_curve_left = pygame.transform.scale(self.cake_curve_left, c.DISTANT_TILE_SIZE)

        self.cake_curve_right = pygame.image.load(os.path.join("downloads", "curve_cake_right.png"))
        self.cake_curve_right = pygame.transform.scale(self.cake_curve_right, c.DISTANT_TILE_SIZE)

        self.yellow_lolipop = pygame.image.load(os.path.join("downloads", "yellow_lolipop.png"))
        self.yellow_lolipop = pygame.transform.scale(self.yellow_lolipop, c.DISTANT_TILE_SIZE)

        self.red_lolipop = pygame.image.load(os.path.join("downloads", "red_lolipop.png"))
        self.red_lolipop = pygame.transform.scale(self.red_lolipop, c.DISTANT_TILE_SIZE)

        self.lolipop_stick = pygame.image.load(os.path.join("downloads", "lolipop_stick.png"))
        self.lolipop_stick = pygame.transform.scale(self.lolipop_stick, c.DISTANT_TILE_SIZE)

        self.cracker_triangle = pygame.image.load(os.path.join("downloads", "cracker_triangle.png"))
        self.cracker_triangle = pygame.transform.scale(self.cracker_triangle, c.DISTANT_TILE_SIZE)

        self.ground_left = pygame.image.load(os.path.join("downloads", "ground_left.png"))
        self.ground_left = pygame.transform.scale(self.ground_left, c.DISTANT_TILE_SIZE)

        self.ground_centre = pygame.image.load(os.path.join("downloads", "ground_centre.png"))
        self.ground_centre = pygame.transform.scale(self.ground_centre, c.DISTANT_TILE_SIZE)

        self.ground_right = pygame.image.load(os.path.join("downloads", "ground_right.png"))
        self.ground_right = pygame.transform.scale(self.ground_right, c.DISTANT_TILE_SIZE)

        self.ground_top_left = pygame.image.load(os.path.join("downloads", "ground_top_left.png"))
        self.ground_top_left = pygame.transform.scale(self.ground_top_left, c.DISTANT_TILE_SIZE)

        self.ground_top_middle = pygame.image.load(os.path.join("downloads", "ground_top_middle.png"))
        self.ground_top_middle = pygame.transform.scale(self.ground_top_middle, c.DISTANT_TILE_SIZE)

        self.ground_top_right = pygame.image.load(os.path.join("downloads", "ground_top_right.png"))
        self.ground_top_right = pygame.transform.scale(self.ground_top_right, c.DISTANT_TILE_SIZE)

        self.plain_dollop = pygame.image.load(os.path.join("downloads", "plain_dollop.png"))
        self.plain_dollop = pygame.transform.scale(self.plain_dollop, c.DISTANT_TILE_SIZE)

        self.bush = pygame.image.load(os.path.join("downloads", "bush.png"))
        self.bush = pygame.transform.scale(self.bush, c.DISTANT_TILE_SIZE)

        self.tree_top = pygame.image.load(os.path.join("downloads", "tree_top.png"))
        self.tree_top = pygame.transform.scale(self.tree_top, c.DISTANT_TILE_SIZE)

        self.tree_bottom = pygame.image.load(os.path.join("downloads", "tree_bottom.png"))
        self.tree_bottom = pygame.transform.scale(self.tree_bottom, c.DISTANT_TILE_SIZE)

        self.empty_glass = pygame.image.load(os.path.join("downloads", "empty_glass.png"))
        self.empty_glass = pygame.transform.scale(self.empty_glass, c.DISTANT_TILE_SIZE)

        self.mug = pygame.image.load(os.path.join("downloads", "mug.png"))
        self.mug = pygame.transform.scale(self.mug, c.DISTANT_TILE_SIZE)

        self.sausage_left = pygame.image.load(os.path.join("downloads", "sausage_left.png"))
        self.sausage_left = pygame.transform.scale(self.sausage_left, c.DISTANT_TILE_SIZE)

        self.sausage_middle = pygame.image.load(os.path.join("downloads", "sausage_middle.png"))
        self.sausage_middle = pygame.transform.scale(self.sausage_middle, c.DISTANT_TILE_SIZE)

        self.sausage_right = pygame.image.load(os.path.join("downloads", "sausage_right.png"))
        self.sausage_right = pygame.transform.scale(self.sausage_right, c.DISTANT_TILE_SIZE)

        self.cheese_left = pygame.image.load(os.path.join("downloads", "cheese_left.png"))
        self.cheese_left = pygame.transform.scale(self.cheese_left, c.OBSTACLE_TILE_SIZE)
        self.cheese_left_background = pygame.transform.scale(self.cheese_left, c.DISTANT_TILE_SIZE)

        self.cheese_middle = pygame.image.load(os.path.join("downloads", "cheese_middle.png"))
        self.cheese_middle = pygame.transform.scale(self.cheese_middle, c.OBSTACLE_TILE_SIZE)

        self.cheese_right = pygame.image.load(os.path.join("downloads", "cheese_right.png"))
        self.cheese_right = pygame.transform.scale(self.cheese_right, c.OBSTACLE_TILE_SIZE)
        self.cheese_right_background = pygame.transform.scale(self.cheese_right, c.DISTANT_TILE_SIZE)

# ---------------------------

    def draw_row(self, left_tile:pygame.Surface, middle_tile:pygame.Surface, right_tile:pygame.Surface, num_of_tiles:int, tile_size:list) -> pygame.Surface:
        row = pygame.Surface((num_of_tiles * tile_size[0], tile_size[1]), pygame.SRCALPHA)
        row.blit(left_tile, (0, 0))
        if middle_tile != None:
            for i in range(1, num_of_tiles - 1):
                row.blit(middle_tile, (i * tile_size[0], 0))
        row.blit(right_tile, ((num_of_tiles-1)*tile_size[0], 0))
        return row

    def draw_tree(self, top_tile:pygame.Surface, extra_layer:pygame.Surface, height:int,) -> pygame.Surface:
        tree = pygame.Surface((c.DISTANT_TILE_SIZE[0], height * c.DISTANT_TILE_SIZE[1]), pygame.SRCALPHA)
        if extra_layer == None:
            for i in range(1, height):
                tree.blit(self.lolipop_stick, (0, (i * c.DISTANT_TILE_SIZE[1])))
            tree.blit(top_tile, (0, 0))
        else:
            for i in range(1, height):
                tree.blit(self.lolipop_stick, (0, (i * c.DISTANT_TILE_SIZE[1])))
            tree.blit(top_tile, (0, c.DISTANT_TILE_SIZE[1]))
            tree.blit(extra_layer, (0, 0))
        return tree

    def draw_background_cake_prop(self) -> pygame.Surface:
        cake_prop = pygame.Surface((7 * c.DISTANT_TILE_SIZE[0], 5 * c.DISTANT_TILE_SIZE[1]), pygame.SRCALPHA)
        cake_prop.blit(self.draw_row(self.ground_top_left, self.ground_top_middle, self.ground_top_right, 7, c.DISTANT_TILE_SIZE), (0, (4 * c.DISTANT_TILE_SIZE[1])))
        cake_prop.blit(self.draw_row(self.cake_left, self.cake_middle, self.cake_right, 4, c.DISTANT_TILE_SIZE), ((c.DISTANT_TILE_SIZE[0]*1.5), (3 * c.DISTANT_TILE_SIZE[1])))
        cake_prop.blit(self.draw_row(self.cake_top_left, self.cake_top_middle, self.cake_top_right, 4, c.DISTANT_TILE_SIZE), ((c.DISTANT_TILE_SIZE[0]*1.5), (2 * c.DISTANT_TILE_SIZE[1])))
        cake_prop.blit(self.draw_row(self.cake_curve_left, self.cake_top_middle, self.cake_curve_right, 3, c.DISTANT_TILE_SIZE), ((c.DISTANT_TILE_SIZE[0]*2), (c.DISTANT_TILE_SIZE[1])))
        cake_prop.blit(self.plain_dollop, ((c.DISTANT_TILE_SIZE[0]*3), 0))
        return cake_prop

    def draw_background_trees_prop(self) -> pygame.Surface:
        trees_prop = pygame.Surface((7 * c.DISTANT_TILE_SIZE[0], 7 * c.DISTANT_TILE_SIZE[1]), pygame.SRCALPHA)

        for i in range(1, 6):
            trees_prop.blit(self.draw_row(self.ground_left, self.ground_centre, self.ground_right, 5, c.DISTANT_TILE_SIZE), (c.DISTANT_TILE_SIZE[0], (1 + i) * c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.draw_row(self.ground_top_left, self.ground_top_middle, self.ground_top_right, 5, c.DISTANT_TILE_SIZE), (c.DISTANT_TILE_SIZE[0], c.DISTANT_TILE_SIZE[1]))

        for i in range(1, 3):
            trees_prop.blit(self.draw_row(self.ground_left, None, self.ground_right, 2, c.DISTANT_TILE_SIZE), (0, (4 + i) * c.DISTANT_TILE_SIZE[1]))
            if i == 2:
                trees_prop.blit(self.draw_row(self.cracker_triangle, None, self.cracker_triangle, 2, c.DISTANT_TILE_SIZE), (0, 6 * c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.draw_row(self.ground_top_left, self.ground_top_middle, self.ground_top_right, 2, c.DISTANT_TILE_SIZE), (0, 4 * c.DISTANT_TILE_SIZE[1]))

        for i in range(1, 4):
            trees_prop.blit(self.draw_row(self.ground_left, self.ground_centre, self.ground_right, 3, c.DISTANT_TILE_SIZE), (4 * c.DISTANT_TILE_SIZE[0], (3 + i) * c.DISTANT_TILE_SIZE[1]))
            if i == 3:
                trees_prop.blit(self.draw_row(self.cracker_triangle, self.cracker_triangle, self.cracker_triangle, 3, c.DISTANT_TILE_SIZE), (4 * c.DISTANT_TILE_SIZE[0], (3 + i) * c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.draw_row(self.ground_top_left, self.ground_top_middle, self.ground_top_right, 3, c.DISTANT_TILE_SIZE), ((4 * c.DISTANT_TILE_SIZE[0]), (3 * c.DISTANT_TILE_SIZE[1])))

        trees_prop.blit(self.draw_tree(self.tree_bottom, self.tree_top, 3), (0, (c.DISTANT_TILE_SIZE[1])))
        trees_prop.blit(self.bush, (0.8 * c.DISTANT_TILE_SIZE[0], 3 * c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.draw_tree(self.red_lolipop, None, 4), (2 * c.DISTANT_TILE_SIZE[0], 3 * c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.draw_tree(self.tree_bottom, self.tree_top, 5), (3 * c.DISTANT_TILE_SIZE[0], 2 * c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.draw_tree(self.bush, None, 1), (2.5 * c.DISTANT_TILE_SIZE[0], 6 * c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.draw_tree(self.red_lolipop, None, 1), (4 * c.DISTANT_TILE_SIZE[0], 2 * c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.draw_tree(self.yellow_lolipop, None, 2), (5 *c.DISTANT_TILE_SIZE[0], c.DISTANT_TILE_SIZE[1]))
        trees_prop.blit(self.mug, (6 * c.DISTANT_TILE_SIZE[0], 2 * c.DISTANT_TILE_SIZE[1]))

        trees_prop.blit(self.draw_row(self.sausage_left, self.sausage_middle, self.sausage_right, 3, c.DISTANT_TILE_SIZE), (c.DISTANT_TILE_SIZE[0], 0))
        trees_prop.blit(self.draw_row(self.cheese_left_background, None, self.cheese_right_background, 2, c.DISTANT_TILE_SIZE), (4.5 * c.DISTANT_TILE_SIZE[0], 4 * c.DISTANT_TILE_SIZE[1]))

        return trees_prop

    def draw_background_trophy_prop(self) -> pygame.Surface:
        trophy_prop = pygame.Surface((4 * c.DISTANT_TILE_SIZE[0], 6 * c.DISTANT_TILE_SIZE[1]), pygame.SRCALPHA)
        trophy_prop.blit(self.draw_row(self.ground_left, self.ground_centre, self.ground_right, 4, c.DISTANT_TILE_SIZE), (0, 5 * c.DISTANT_TILE_SIZE[0]))
        trophy_prop.blit(self.draw_row(self.ground_top_left, self.ground_top_middle, self.ground_top_right, 4, c.DISTANT_TILE_SIZE), (0, 4 * c.DISTANT_TILE_SIZE[1]))
        trophy_prop.blit(self.draw_row(self.cake_left, self.cake_middle, self.cake_right, 3, c.DISTANT_TILE_SIZE), (0.5 * c.DISTANT_TILE_SIZE[0], 3 * c.DISTANT_TILE_SIZE[1]))
        trophy_prop.blit(self.draw_row(self.cake_top_left, self.cake_top_middle, self.cake_top_right, 3, c.DISTANT_TILE_SIZE), (0.5 * c.DISTANT_TILE_SIZE[0], 2 * c.DISTANT_TILE_SIZE[1]))
        trophy_prop.blit(self.draw_row(self.cake_top_left, self.cake_top_middle, self.cake_top_right, 2, c.DISTANT_TILE_SIZE), (c.DISTANT_TILE_SIZE[0], c.DISTANT_TILE_SIZE[1]))
        trophy_prop.blit(self.empty_glass, ((1.5 * c.DISTANT_TILE_SIZE[0]), 0))
        return trophy_prop
    
    def draw_background(self, screen:pygame.Surface, colour:tuple[int]) -> pygame.Surface:
        screen.fill(colour)

        for i in range(10):
            screen.blit(self.floor_tile, (self.floor_tile_x + i * 80, self.floor_tile_y))

        screen.blit(self.draw_background_cake_prop(), (self.cake_back_prop_x, self.cake_back_prop_y))

        screen.blit(self.draw_background_trees_prop(), (self.trees_back_prop_x, self.trees_back_prop_y))

        screen.blit(self.draw_background_trophy_prop(), (self.trophy_back_prop_x, self.trophy_back_prop_y))

        screen.blit(self.draw_row(self.cloud_left, self.cloud_middle, self.cloud_right, 3, c.CLOUD_TILE_SIZE), (self.long_cloud_x, self.long_cloud_y))
        screen.blit(self.draw_row(self.cloud_left, self.cloud_middle, self.cloud_right, 2, c.CLOUD_TILE_SIZE), (self.small_cloud_1_x, self.small_cloud_1_y))
        screen.blit(self.draw_row(self.cloud_left, self.cloud_middle, self.cloud_right, 2, c.CLOUD_TILE_SIZE), (self.small_cloud_2_x, self.small_cloud_2_y))
        screen.blit(self.draw_row(self.cloud_left, self.cloud_middle, self.cloud_right, 3, c.CLOUD_TILE_SIZE), (self.long_cloud_2_x, self.long_cloud_2_y))

    def update_background(self, speed) -> None:
        self.floor_tile_x -= speed
        if self.floor_tile_x <= -c.CLOSE_TILE_SIZE[0]:
            self.floor_tile_x = 0

        self.long_cloud_x -= 0.8
        if self.long_cloud_x <= -150:
            self.long_cloud_x = 640

        self.small_cloud_1_x -= 0.75
        if self.small_cloud_1_x <= -100:
            self.small_cloud_1_x = 640

        self.small_cloud_2_x -= 0.8
        if self.small_cloud_2_x <= -100:
            self.small_cloud_2_x = 640

        self.long_cloud_2_x -= 0.7
        if self.long_cloud_2_x <= -150:
            self.long_cloud_2_x = 640

        self.cake_back_prop_x -= c.BACKGROUND_SPEED
        if self.trophy_back_prop_x == (10 * c.DISTANT_TILE_SIZE[0]):
            self.cake_back_prop_x = c.WIDTH

        self.trees_back_prop_x -= c.BACKGROUND_SPEED
        if self.cake_back_prop_x == (7 * c.DISTANT_TILE_SIZE[0]):
            self.trees_back_prop_x = c.WIDTH

        self.trophy_back_prop_x -= c.BACKGROUND_SPEED
        if self.trees_back_prop_x == (7 * c.DISTANT_TILE_SIZE[0]):
            self.trophy_back_prop_x = c.WIDTH

    def update_background_main_menu(self, screen, colour) -> None:
        self.draw_background(screen, colour)

    def reset_background(self) -> None:
        self.floor_tile_x = 4
        self.floor_tile_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1]

        self.long_cloud_x = c.WIDTH + 20
        self.long_cloud_y = 150

        self.long_cloud_2_x = c.WIDTH + 550
        self.long_cloud_2_y = 60

        self.small_cloud_1_x = c.WIDTH + 150
        self.small_cloud_1_y = 20

        self.small_cloud_2_x = c.WIDTH + 380
        self.small_cloud_2_y = 80

        self.cake_back_prop_x = 0
        self.cake_back_prop_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - 5 * c.DISTANT_TILE_SIZE[1]

        self.trees_back_prop_x = 9 * c.DISTANT_TILE_SIZE[0]
        self.trees_back_prop_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - (7 * c.DISTANT_TILE_SIZE[1])

        self.trophy_back_prop_x = 19 * c.DISTANT_TILE_SIZE[0]
        self.trophy_back_prop_y = c.HEIGHT - c.CLOSE_TILE_SIZE[1] - 6 * c.DISTANT_TILE_SIZE[1]