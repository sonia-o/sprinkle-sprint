# pygame template

import pygame
import os


pygame.init()

WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

x_pos = 30
y_pos = 300
current_pos = 2  ## 1 for up, 2 for normal, 3 for down
down = False     ## Tracks if the sprite has reached the top and is now falling down

character = ["redline_spoon.png", "tile_0103.png", "tile_0104.png"]
character_type = 1
sprite = pygame.image.load(os.path.join("downloads", character[character_type]))

sprite = pygame.transform.scale(sprite, (60, 80))
sprite_down = pygame.transform.rotate(sprite, 270)

draw_image = sprite

# ---------------------------
# class Object:

def move():
    global x_pos, y_pos
    global draw_image
    global sprite_down
    global current_pos
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        current_pos = 3
        draw_image = sprite_down
        y_pos = 320
        current_pos = 2

    if keys[pygame.K_UP]:
        current_pos = 1
        # draw_up()
        # y_pos = 260

def draw_up():
    global draw_image, x_pos, y_pos
    screen.blit(draw_image, (x_pos, y_pos))

running = True
clock = pygame.time.Clock()

while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES
    # All game math and comparisons happen here

    draw_image = sprite
    fall_rate = 1
    rise_rate = 1
    if current_pos == 1:
        if y_pos > 10 and down == False:
            rise_rate = rise_rate*15
            y_pos -= rise_rate
            if y_pos <= 10:
                down = True ## If the sprite reach the top, then it will be set as true
        if down:
            if y_pos < 300:
                fall_rate = fall_rate*10
                y_pos += fall_rate
            elif y_pos >= 300:
                down = False
                current_pos = 2
                continue
    else:
        move()

    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command]
    draw_up()
    if current_pos == 2:
        y_pos = 300

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)

    #---------------------------

pygame.quit()
