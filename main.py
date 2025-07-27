import pygame
import json
import constants as c
from background import Background
from obstacle_manager import Obstacle_Manager
from donut_manager import Donut_Manager
from sprite import Sprite
from menu import Menu
from main_menu import MainMenu
from pause_menu import PauseMenu
from obstacle import Obstacle
from shop_menu import Shop_menu
from die_menu import DieMenu

with open('game_state.json', 'r') as f:
    game_state = json.load(f)

pygame.init()

screen = pygame.display.set_mode(c.SIZE)
clock = pygame.time.Clock()

background_obj = Background()
obstacle_manager = Obstacle_Manager()
donut_manager = Donut_Manager()
sprite_obj = Sprite()
menu_obj = Menu()
pause_menu_obj = PauseMenu()
obstacle_obj = Obstacle()
main_menu_obj = MainMenu()
die_menu_obj = DieMenu()

sprite_alive = True
game_paused = False
game_ongoing = False
donut_count = game_state["donut_count"]               # Load from JSON
upgrade_start_time = None
store_menu_open = False
owned = game_state["owned"]                             # Load from JSON
equip = game_state["equip"]                             # Load from JSON
custom_font_small = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 15)
custom_font_large = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 30)
frames_per_obstacle = 67
frame_counter_obstacles = 0
game_start_time = None
speed_index = game_state["speed_index"]                 # Load from JSON
colour_index = game_state["colour_index"]               # Load from JSON

shop_menu_obj = Shop_menu(owned, equip)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            if store_menu_open:
                store_menu_return, donut_count = shop_menu_obj.shop_menu_update(owned, click_pos, equip, donut_count)
                if store_menu_return == -1:
                    store_menu_open = False
                else:
                    equip = store_menu_return
            elif main_menu_obj.play_button_rect.collidepoint(click_pos):
                game_ongoing = True
                sprite_alive = True
                game_paused = False
                game_start_time = pygame.time.get_ticks()
            elif main_menu_obj.options_button_rect.collidepoint(click_pos):
                main_menu_obj.options(screen, donut_count, owned, equip, speed_index, colour_index) # options button
                if c.SPEED == c.FOREGROUND_SPEED:
                    speed_index = 0
                elif c.SPEED == c.FOREGROUND_SPEED_MEDIUM:
                    speed_index = 1
                elif c.SPEED == c.FOREGROUND_SPEED_FAST:
                    speed_index = 2
                if c.COLOUR == c.COLOUR_PINK:
                    colour_index = 0
                elif c.COLOUR == c.COLOUR_YELLOW:
                    colour_index = 1
                elif c.COLOUR == c.COLOUR_BLUE:
                    colour_index = 2
            elif main_menu_obj.store_button_rect.collidepoint(click_pos):
                store_menu_open = True
                # main_menu_obj.store(screen) # store button
            elif pause_menu_obj.play_rect.collidepoint(click_pos):
                game_paused = False
            elif pause_menu_obj.quit_rect.collidepoint(click_pos):
                running = False
            elif die_menu_obj.ok_button_rect.collidepoint(click_pos):
                game_ongoing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True

    if speed_index == 0:
        frames_per_obstacle = 67
    elif speed_index == 1:
        frames_per_obstacle = 40
    elif speed_index == 2:
        frames_per_obstacle = 35
    
    frame_counter_obstacles += 1
    if frame_counter_obstacles >= frames_per_obstacle and game_paused == False and game_ongoing == True and sprite_alive == True:
        obstacle_manager.create_obstacle()
        donut_manager.create_donut(obstacle_manager.obstacles_list[-1].random_num)
        frame_counter_obstacles = 0

    if game_ongoing == False:
        main_menu_obj.main_menu(screen, background_obj, colour_index)
        if store_menu_open:
            shop_menu_obj.draw_shop(screen, donut_count, colour_index)

    elif sprite_alive == True and game_paused == False and game_ongoing == True: 
        # GAME STATE UPDATES
        # All game math and comparisons happen here
        background_obj.update_background(c.SPEEDS[speed_index])
        obstacle_manager.update_obstacles(c.SPEEDS[speed_index])
        donut_manager.update_donuts(c.SPEEDS[speed_index])
        sprite_obj.sprite_update(equip)

        # DRAWING
        background_obj.draw_background(screen, c.COLOURS[colour_index])
        obstacle_manager.draw_obstacles(screen)
        donut_manager.draw_donuts(screen)
        sprite_obj.before_draw(screen)
        credit_text = custom_font_small.render("Donuts: " + str(donut_count), True, (255, 255, 255)) # set to 0 for default
        screen.blit(credit_text, (22, 18))

        current_time = pygame.time.get_ticks()
        if current_time - game_start_time < 3000:
            pause_text = custom_font_large.render("Press SPACE to Pause", True, (255, 255, 255))
            screen.blit(pause_text, (c.SIZE[0] // 2 - pause_text.get_width() // 2, 350))

        for obj in obstacle_manager.obstacles_list:
            collide = obj.rect.colliderect(sprite_obj.sprite_rect)              #Got collide rect method from chatgpt but modified code for this project
            collide_duck = obj.rect.colliderect(sprite_obj.sprite_down_rect)    #----------
            if collide or collide_duck:
                sprite_alive = False
                background_obj.reset_background()
                obstacle_manager.reset_obstacles()
                donut_manager.reset_donuts()

        for i in range(len(donut_manager.donut_list) - 1, -1, -1):
            collide = donut_manager.donut_list[i].rect.colliderect(sprite_obj.sprite_rect)
            collide_duck = donut_manager.donut_list[i].rect.colliderect(sprite_obj.sprite_down_rect)
            if collide or collide_duck:
                if donut_manager.donut_list[i].image == donut_manager.donut_list[i].pink_donut:
                    upgrade_start_time = pygame.time.get_ticks()
                    sprite_obj.min = c.HEIGHT - c.CLOSE_TILE_SIZE[1]- (sprite_obj.sprite_height * 4.5)
                del donut_manager.donut_list[i]
                donut_count += 1

        if upgrade_start_time != None:
            current_time = pygame.time.get_ticks()
            time_passed = current_time - upgrade_start_time
            if time_passed <= 1500:
                upgrade_text = custom_font_large.render("upgrade collected!", True, (255, 255, 255))
                screen.blit(upgrade_text, (c.SIZE[0] // 2 - upgrade_text.get_width() // 2, 350))
            elif time_passed >= 5000:
                sprite_obj.min = c.HEIGHT - c.CLOSE_TILE_SIZE[1]- (sprite_obj.sprite_height * 3.5)

    elif sprite_alive == False and game_ongoing == True:
        die_menu_obj.draw_death_menu(screen, c.COLOURS[colour_index])

    elif game_paused:
        if game_paused == True:
            pause_menu_obj.draw_pause_menu(screen, colour_index)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

game_state["donut_count"] = donut_count
game_state["owned"] = owned
game_state["equip"] = equip
game_state["speed_index"] = speed_index
game_state["colour_index"] = colour_index
with open('game_state.json', 'w') as f:
    json.dump(game_state, f)

pygame.quit()