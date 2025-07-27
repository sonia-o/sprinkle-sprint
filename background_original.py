# pygame template

import pygame
import os

pygame.init()

WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE, pygame.SRCALPHA)
clock = pygame.time.Clock()
#----------------------------


# ---------------------------
# Initialize global variables

CLOSE_TILE_SIZE = (80,80)
CLOUD_TILE_SIZE = (50,50)
DISTANT_TILE_SIZE = (40,40)
OBSTACLE_TILE_SIZE = (45, 45)

BACKGROUND_SPEED = 0.25
FOREGROUND_SPEED = 5

floor_tile_x = 4
floor_tile_y = HEIGHT - CLOSE_TILE_SIZE[1]

long_cloud_x = 20
long_cloud_y = 150

long_cloud_2_x = 550
long_cloud_2_y = 60

small_cloud_1_x = 150
small_cloud_1_y = 20

small_cloud_2_x = 380
small_cloud_2_y = 80

cake_back_prop_x = 0
cake_back_prop_y = HEIGHT - CLOSE_TILE_SIZE[1] - 5 * DISTANT_TILE_SIZE[1]

trees_back_prop_x = 9 * DISTANT_TILE_SIZE[0]
trees_back_prop_y = HEIGHT - CLOSE_TILE_SIZE[1] - 7 * DISTANT_TILE_SIZE[1]

trophy_back_prop_x = 19 * DISTANT_TILE_SIZE[0]
trophy_back_prop_y = HEIGHT - CLOSE_TILE_SIZE[1] - 6 * DISTANT_TILE_SIZE[1]



floor_tile = pygame.image.load(os.path.join("downloads", "floor.png"))
floor_tile = pygame.transform.scale(floor_tile, CLOSE_TILE_SIZE)

cloud_left = pygame.image.load(os.path.join("downloads", "cloud_left.png"))
cloud_left = pygame.transform.rotate(cloud_left, 180)
cloud_left = pygame.transform.scale(cloud_left, CLOUD_TILE_SIZE)

cloud_middle = pygame.image.load(os.path.join("downloads", "cloud_middle.png"))
cloud_middle = pygame.transform.rotate(cloud_middle, 180)
cloud_middle = pygame.transform.scale(cloud_middle, CLOUD_TILE_SIZE)

cloud_right = pygame.image.load(os.path.join("downloads", "cloud_right.png"))
cloud_right = pygame.transform.rotate(cloud_right, 180)
cloud_right = pygame.transform.scale(cloud_right, CLOUD_TILE_SIZE)

cake_left = pygame.image.load(os.path.join("downloads", "cake_left.png"))
cake_left = pygame.transform.scale(cake_left, DISTANT_TILE_SIZE)

cake_middle = pygame.image.load(os.path.join("downloads", "cake_middle.png"))
cake_middle = pygame.transform.scale(cake_middle, DISTANT_TILE_SIZE)

cake_right = pygame.image.load(os.path.join("downloads", "cake_right.png"))
cake_right = pygame.transform.scale(cake_right, DISTANT_TILE_SIZE)

cake_top_left = pygame.image.load(os.path.join("downloads", "cake_top_left.png"))
cake_top_left = pygame.transform.scale(cake_top_left, DISTANT_TILE_SIZE)

cake_top_middle = pygame.image.load(os.path.join("downloads", "cake_top_middle.png"))
cake_top_middle = pygame.transform.scale(cake_top_middle, DISTANT_TILE_SIZE)

cake_top_right = pygame.image.load(os.path.join("downloads", "cake_top_right.png"))
cake_top_right = pygame.transform.scale(cake_top_right, DISTANT_TILE_SIZE)

cake_curve_left = pygame.image.load(os.path.join("downloads", "curve_cake_left.png"))
cake_curve_left = pygame.transform.scale(cake_curve_left, DISTANT_TILE_SIZE)

cake_curve_right = pygame.image.load(os.path.join("downloads", "curve_cake_right.png"))
cake_curve_right = pygame.transform.scale(cake_curve_right, DISTANT_TILE_SIZE)

yellow_lolipop = pygame.image.load(os.path.join("downloads", "yellow_lolipop.png"))
yellow_lolipop = pygame.transform.scale(yellow_lolipop, DISTANT_TILE_SIZE)

red_lolipop = pygame.image.load(os.path.join("downloads", "red_lolipop.png"))
red_lolipop = pygame.transform.scale(red_lolipop, DISTANT_TILE_SIZE)

lolipop_stick = pygame.image.load(os.path.join("downloads", "lolipop_stick.png"))
lolipop_stick = pygame.transform.scale(lolipop_stick, DISTANT_TILE_SIZE)

cracker_triangle = pygame.image.load(os.path.join("downloads", "cracker_triangle.png"))
cracker_triangle = pygame.transform.scale(cracker_triangle, DISTANT_TILE_SIZE)

ground_left = pygame.image.load(os.path.join("downloads", "ground_left.png"))
ground_left = pygame.transform.scale(ground_left, DISTANT_TILE_SIZE)

ground_centre = pygame.image.load(os.path.join("downloads", "ground_centre.png"))
ground_centre = pygame.transform.scale(ground_centre, DISTANT_TILE_SIZE)

ground_right = pygame.image.load(os.path.join("downloads", "ground_right.png"))
ground_right = pygame.transform.scale(ground_right, DISTANT_TILE_SIZE)

ground_top_left = pygame.image.load(os.path.join("downloads", "ground_top_left.png"))
ground_top_left = pygame.transform.scale(ground_top_left, DISTANT_TILE_SIZE)

ground_top_middle = pygame.image.load(os.path.join("downloads", "ground_top_middle.png"))
ground_top_middle = pygame.transform.scale(ground_top_middle, DISTANT_TILE_SIZE)

ground_top_right = pygame.image.load(os.path.join("downloads", "ground_top_right.png"))
ground_top_right = pygame.transform.scale(ground_top_right, DISTANT_TILE_SIZE)

plain_dollop = pygame.image.load(os.path.join("downloads", "plain_dollop.png"))
plain_dollop = pygame.transform.scale(plain_dollop, DISTANT_TILE_SIZE)

bush = pygame.image.load(os.path.join("downloads", "bush.png"))
bush = pygame.transform.scale(bush, DISTANT_TILE_SIZE)

bush = pygame.image.load(os.path.join("downloads", "bush.png"))
bush = pygame.transform.scale(bush, DISTANT_TILE_SIZE)

tree_top = pygame.image.load(os.path.join("downloads", "tree_top.png"))
tree_top = pygame.transform.scale(tree_top, DISTANT_TILE_SIZE)

tree_bottom = pygame.image.load(os.path.join("downloads", "tree_bottom.png"))
tree_bottom = pygame.transform.scale(tree_bottom, DISTANT_TILE_SIZE)

empty_glass = pygame.image.load(os.path.join("downloads", "empty_glass.png"))
empty_glass = pygame.transform.scale(empty_glass, DISTANT_TILE_SIZE)

mug = pygame.image.load(os.path.join("downloads", "mug.png"))
mug = pygame.transform.scale(mug, DISTANT_TILE_SIZE)

sausage_left = pygame.image.load(os.path.join("downloads", "sausage_left.png"))
sausage_left = pygame.transform.scale(sausage_left, DISTANT_TILE_SIZE)

sausage_middle = pygame.image.load(os.path.join("downloads", "sausage_middle.png"))
sausage_middle = pygame.transform.scale(sausage_middle, DISTANT_TILE_SIZE)

sausage_right = pygame.image.load(os.path.join("downloads", "sausage_right.png"))
sausage_right = pygame.transform.scale(sausage_right, DISTANT_TILE_SIZE)

cheese_left = pygame.image.load(os.path.join("downloads", "cheese_left.png"))
cheese_left = pygame.transform.scale(cheese_left, OBSTACLE_TILE_SIZE)
cheese_left_background = pygame.transform.scale(cheese_left, DISTANT_TILE_SIZE)

cheese_middle = pygame.image.load(os.path.join("downloads", "cheese_middle.png"))
cheese_middle = pygame.transform.scale(cheese_middle, OBSTACLE_TILE_SIZE)

cheese_right = pygame.image.load(os.path.join("downloads", "cheese_right.png"))
cheese_right = pygame.transform.scale(cheese_right, OBSTACLE_TILE_SIZE)
cheese_right_background = pygame.transform.scale(cheese_right, DISTANT_TILE_SIZE)

candy_cane_stick = pygame.image.load(os.path.join("downloads", "candy_cane_stick.png"))
candy_cane_stick = pygame.transform.scale(candy_cane_stick, OBSTACLE_TILE_SIZE)

candy_cane_top = pygame.image.load(os.path.join("downloads", "candy_cane_top.png"))
candy_cane_top = pygame.transform.scale(candy_cane_top, OBSTACLE_TILE_SIZE)

cracker_left = pygame.image.load(os.path.join("downloads", "cracker_left.png")).convert_alpha()
cracker_left = pygame.transform.scale(cracker_left, OBSTACLE_TILE_SIZE)

cracker_right = pygame.image.load(os.path.join("downloads", "cracker_right.png")).convert_alpha()
cracker_right = pygame.transform.scale(cracker_right, OBSTACLE_TILE_SIZE)

plain_sausage_left = pygame.image.load(os.path.join("downloads", "plain_sausage_left.png"))
plain_sausage_left = pygame.transform.scale(plain_sausage_left, OBSTACLE_TILE_SIZE)

plain_sausage_middle = pygame.image.load(os.path.join("downloads", "plain_sausage_middle.png"))
plain_sausage_middle = pygame.transform.scale(plain_sausage_middle, OBSTACLE_TILE_SIZE)

plain_sausage_right = pygame.image.load(os.path.join("downloads", "plain_sausage_right.png"))
plain_sausage_right = pygame.transform.scale(plain_sausage_right, OBSTACLE_TILE_SIZE)

small_biscuit = pygame.image.load(os.path.join("downloads", "small_biscuit.png"))
small_biscuit = pygame.transform.scale(small_biscuit, OBSTACLE_TILE_SIZE)

# ---------------------------
# Define functions

def draw_row(left_tile:pygame.Surface, middle_tile:pygame.Surface, right_tile:pygame.Surface, num_of_tiles:int, tile_size:list) -> pygame.Surface:
    row = pygame.Surface((num_of_tiles * tile_size[0], tile_size[1]), pygame.SRCALPHA)
    row.blit(left_tile, (0, 0))
    if middle_tile != None:
        for i in range(1, num_of_tiles - 1):
            row.blit(middle_tile, (i * tile_size[0], 0))
    row.blit(right_tile, ((num_of_tiles-1)*tile_size[0], 0))
    return row

def draw_tree(top_tile:pygame.Surface, extra_layer:pygame.Surface, height:int,) -> pygame.Surface:
    tree = pygame.Surface((DISTANT_TILE_SIZE[0], height * DISTANT_TILE_SIZE[1]), pygame.SRCALPHA)
    if extra_layer == None:
        for i in range(1, height):
            tree.blit(lolipop_stick, (0, (i * DISTANT_TILE_SIZE[1])))
        tree.blit(top_tile, (0, 0))
    else:
        for i in range(1, height):
            tree.blit(lolipop_stick, (0, (i * DISTANT_TILE_SIZE[1])))
        tree.blit(top_tile, (0, DISTANT_TILE_SIZE[1]))
        tree.blit(extra_layer, (0, 0))
    return tree

def draw_background_cake_prop() -> pygame.Surface:
    cake_prop = pygame.Surface((7 * DISTANT_TILE_SIZE[0], 5 * DISTANT_TILE_SIZE[1]), pygame.SRCALPHA)
    cake_prop.blit(draw_row(ground_top_left, ground_top_middle, ground_top_right, 7, DISTANT_TILE_SIZE), (0, (4 * DISTANT_TILE_SIZE[1])))
    cake_prop.blit(draw_row(cake_left, cake_middle, cake_right, 4, DISTANT_TILE_SIZE), ((DISTANT_TILE_SIZE[0]*1.5), (3 * DISTANT_TILE_SIZE[1])))
    cake_prop.blit(draw_row(cake_top_left, cake_top_middle, cake_top_right, 4, DISTANT_TILE_SIZE), ((DISTANT_TILE_SIZE[0]*1.5), (2 * DISTANT_TILE_SIZE[1])))
    cake_prop.blit(draw_row(cake_curve_left, cake_top_middle, cake_curve_right, 3, DISTANT_TILE_SIZE), ((DISTANT_TILE_SIZE[0]*2), (DISTANT_TILE_SIZE[1])))
    cake_prop.blit(plain_dollop, ((DISTANT_TILE_SIZE[0]*3), 0))
    return cake_prop

def draw_background_trees_prop() -> pygame.Surface:
    trees_prop = pygame.Surface((7 * DISTANT_TILE_SIZE[0], 7 * DISTANT_TILE_SIZE[1]), pygame.SRCALPHA)
    for i in range(1, 6):
        trees_prop.blit(draw_row(ground_left, ground_centre, ground_right, 5, DISTANT_TILE_SIZE), (DISTANT_TILE_SIZE[0], (1 + i) * DISTANT_TILE_SIZE[1]))
    trees_prop.blit(draw_row(ground_top_left, ground_top_middle, ground_top_right, 5, DISTANT_TILE_SIZE), (DISTANT_TILE_SIZE[0], DISTANT_TILE_SIZE[1]))
    
    for i in range(1, 3):
        trees_prop.blit(draw_row(ground_left, None, ground_right, 2, DISTANT_TILE_SIZE), (0, (4 + i) * DISTANT_TILE_SIZE[1]))
        if i == 2:
            trees_prop.blit(draw_row(cracker_triangle, None, cracker_triangle, 2, DISTANT_TILE_SIZE), (0, 6 * DISTANT_TILE_SIZE[1]))
    trees_prop.blit(draw_row(ground_top_left, ground_top_middle, ground_top_right, 2, DISTANT_TILE_SIZE), (0, 4 * DISTANT_TILE_SIZE[1]))
    
    for i in range(1, 4):
        trees_prop.blit(draw_row(ground_left, ground_centre, ground_right, 3, DISTANT_TILE_SIZE), (4 * DISTANT_TILE_SIZE[0], (3 + i) * DISTANT_TILE_SIZE[1]))
        if i == 3:
            trees_prop.blit(draw_row(cracker_triangle, cracker_triangle, cracker_triangle, 3, DISTANT_TILE_SIZE), (4 * DISTANT_TILE_SIZE[0], (3 + i) * DISTANT_TILE_SIZE[1]))
    trees_prop.blit(draw_row(ground_top_left, ground_top_middle, ground_top_right, 3, DISTANT_TILE_SIZE), ((4 * DISTANT_TILE_SIZE[0]), (3 * DISTANT_TILE_SIZE[1])))
    
    trees_prop.blit(draw_tree(tree_bottom, tree_top, 3), (0, (DISTANT_TILE_SIZE[1])))
    trees_prop.blit(bush, (0.8 * DISTANT_TILE_SIZE[0], 3*DISTANT_TILE_SIZE[1]))
    trees_prop.blit(draw_tree(red_lolipop, None, 4), (2 * DISTANT_TILE_SIZE[0], 3 * DISTANT_TILE_SIZE[1]))
    trees_prop.blit(draw_tree(tree_bottom, tree_top, 5), (3 * DISTANT_TILE_SIZE[0], 2 * DISTANT_TILE_SIZE[1]))
    trees_prop.blit(draw_tree(bush, None, 1), (2.5*DISTANT_TILE_SIZE[0], 6 * DISTANT_TILE_SIZE[1]))
    trees_prop.blit(draw_tree(red_lolipop, None, 1), (4 * DISTANT_TILE_SIZE[0], 2 * DISTANT_TILE_SIZE[1]))
    trees_prop.blit(draw_tree(yellow_lolipop, None, 2), (5 * DISTANT_TILE_SIZE[0], DISTANT_TILE_SIZE[1]))
    trees_prop.blit(mug, (6*DISTANT_TILE_SIZE[0], 2 * DISTANT_TILE_SIZE[1]))

    trees_prop.blit(draw_row(sausage_left, sausage_middle, sausage_right, 3, DISTANT_TILE_SIZE), (DISTANT_TILE_SIZE[0], 0))
    trees_prop.blit(draw_row(cheese_left_background, None, cheese_right_background, 2, DISTANT_TILE_SIZE), (4.5*DISTANT_TILE_SIZE[0], 4*DISTANT_TILE_SIZE[1]))

    return trees_prop

def draw_background_trophy_prop() -> pygame.Surface:
    trophy_prop = pygame.Surface((4 * DISTANT_TILE_SIZE[0], 6 * DISTANT_TILE_SIZE[1]), pygame.SRCALPHA)
    trophy_prop.blit(draw_row(ground_left, ground_centre, ground_right, 4, DISTANT_TILE_SIZE), (0, 5 * DISTANT_TILE_SIZE[0]))
    trophy_prop.blit(draw_row(ground_top_left, ground_top_middle, ground_top_right, 4, DISTANT_TILE_SIZE), (0, 4 * DISTANT_TILE_SIZE[1]))
    trophy_prop.blit(draw_row(cake_left, cake_middle, cake_right, 3, DISTANT_TILE_SIZE), (0.5 * DISTANT_TILE_SIZE[0], 3 * DISTANT_TILE_SIZE[1]))
    trophy_prop.blit(draw_row(cake_top_left, cake_top_middle, cake_top_right, 3, DISTANT_TILE_SIZE), (0.5 * DISTANT_TILE_SIZE[0], 2 * DISTANT_TILE_SIZE[1]))
    trophy_prop.blit(draw_row(cake_top_left, cake_top_middle, cake_top_right, 2, DISTANT_TILE_SIZE), (DISTANT_TILE_SIZE[0], DISTANT_TILE_SIZE[1]))
    trophy_prop.blit(empty_glass, ((1.5 * DISTANT_TILE_SIZE[0]), 0))
    return trophy_prop

#----------------------------
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # GAME STATE UPDATES
    # All game math and comparisons happen here
    floor_tile_x -= FOREGROUND_SPEED
    if floor_tile_x <= -CLOSE_TILE_SIZE[0]:
        floor_tile_x = 0

    long_cloud_x -= 0.8
    if long_cloud_x <= -150:
        long_cloud_x = 640

    small_cloud_1_x -= 0.75
    if small_cloud_1_x <= -100:
        small_cloud_1_x = 640

    small_cloud_2_x -= 0.8
    if small_cloud_2_x <= -100:
        small_cloud_2_x = 640

    long_cloud_2_x -= 0.7
    if long_cloud_2_x <= -150:
        long_cloud_2_x = 640

    cake_back_prop_x -= BACKGROUND_SPEED
    if trophy_back_prop_x == (10 * DISTANT_TILE_SIZE[0]):
        cake_back_prop_x = WIDTH

    trees_back_prop_x -= BACKGROUND_SPEED
    if cake_back_prop_x == (7 * DISTANT_TILE_SIZE[0]):
        trees_back_prop_x = WIDTH

    trophy_back_prop_x -= BACKGROUND_SPEED
    if trees_back_prop_x == (7 * DISTANT_TILE_SIZE[0]):
        trophy_back_prop_x = WIDTH


    # DRAWING    
    screen.fill((255, 161, 183))  # always the first drawing command

    for i in range(10):
        screen.blit(floor_tile, (floor_tile_x + i * 80, floor_tile_y))

    screen.blit(draw_background_cake_prop(), (cake_back_prop_x, cake_back_prop_y))

    screen.blit(draw_background_trees_prop(), (trees_back_prop_x, trees_back_prop_y))

    screen.blit(draw_background_trophy_prop(), (trophy_back_prop_x, trophy_back_prop_y))

    screen.blit(draw_row(cloud_left, cloud_middle, cloud_right, 3, CLOUD_TILE_SIZE), (long_cloud_x, long_cloud_y))
    screen.blit(draw_row(cloud_left, cloud_middle, cloud_right, 2, CLOUD_TILE_SIZE), (small_cloud_1_x, small_cloud_1_y))
    screen.blit(draw_row(cloud_left, cloud_middle, cloud_right, 2, CLOUD_TILE_SIZE), (small_cloud_2_x, small_cloud_2_y))
    screen.blit(draw_row(cloud_left, cloud_middle, cloud_right, 3, CLOUD_TILE_SIZE), (long_cloud_2_x, long_cloud_2_y))



    #END OF THE LOOP
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()