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

custom_font = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 20)
custom_font_small = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 5)

main_menu = pygame.Surface((640, 400))
image1 = pygame.image.load(os.path.join("downloads/shop_menu", "shop.png"))
button = ["buy_button.png", "orange_buybutton.webp", "equip_button.png", "equipped_button.png", "quit_button.png", "pop_up_screen.png", "ok_button.png"] ## Store the image file for easy changes
price = [0, 50, 50]
character = ["spoon.png", "fork.png", "knife.png"]
charcter_name = ["Spoon", "Fork", "Knife"]
owned = [True, False, False]    # List of sprites with True representing owned sprites and False for unowned sprites
equip = 0                      # current used character

button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[0]))
button1_appear = pygame.transform.scale(button1_appear, (103, 40))

button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[0]))
button2_appear = pygame.transform.scale(button2_appear, (103, 40))

button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[0]))
button3_appear = pygame.transform.scale(button3_appear, (103, 40))

spoon_text = custom_font.render("spoon", True, (255, 255, 255))
fork_text = custom_font.render("fork", True, (255, 255, 255))
knife_text = custom_font.render("knife", True, (255, 255, 255))

quit_appear = pygame.image.load(os.path.join("downloads/pause_menu", button[4]))
quit_appear = pygame.transform.scale(quit_appear, (30, 30))

buy_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[5]))
buy_appear = pygame.transform.scale(buy_appear, (470, 200))

button1_click = pygame.Rect(116, 247, 103, 40)  # (x, y, width, height)
button2_click = pygame.Rect(273, 247, 103, 40)  
button3_click = pygame.Rect(430, 247, 103, 40) 
quit_click = pygame.Rect(590, 18, 30, 30) 

custom_font_small = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 15)
credit = 50 # Currency
credit_text = custom_font_small.render("Credit: " + str(credit), True, (255, 255, 255))

# ---------

current_buy = -1
buy = False             # If buy screen should appear
insufficient = False    # If insufficient funds screen should appear

not_enough_funds_text = custom_font.render("Insufficient Funds", True, (255, 255, 255))
ok_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[6]))
ok_appear = pygame.transform.scale(ok_appear, (80, 40))

ok_click = pygame.Rect(365, 204, 80, 40) 
quit_buy_appear = pygame.Rect(432, 166, 30, 30) 

# ---------------------------

def shop():
    global image1
    global sprite_button
    global character
    main_menu.blit(image1, (0, 0))
    main_menu.blit(button1_appear, (116, 247))
    main_menu.blit(button2_appear, (273, 247))
    main_menu.blit(button3_appear, (430, 247))

    x_image = [138, 300, 455]
    for x in range (3): ## Draw out the sprite images
        sprite = pygame.image.load(os.path.join("downloads/shop_menu", character[x]))
        sprite = pygame.transform.scale(sprite, (40, 60))
        main_menu.blit(sprite, (x_image[x] + 7, 178))
    
    if buy:
        main_menu.blit(buy_appear, (90, 130))
        main_menu.blit(quit_appear, (432, 166))
        main_menu.blit(ok_appear, (365, 204))

        purchase_line1 = custom_font_small.render(f"Purchase {charcter_name[current_buy]}", True, (255, 255, 255))
        purchase_line2 = custom_font_small.render(f"for {price[current_buy]} credits?", True, (255, 255, 255))
        main_menu.blit(purchase_line1, (225, 199))
        main_menu.blit(purchase_line2, (225, 219))
        
    if insufficient:
        main_menu.blit(buy_appear, (90, 130))
        main_menu.blit(quit_appear, (432, 166))
        main_menu.blit(ok_appear, (365, 204))

        insufficient_line1 = custom_font_small.render(f"Insufficient Funds", True, (255, 255, 255))
        insufficient_line2 = custom_font_small.render(f"you need {price[current_buy]-credit}", True, (255, 255, 255))
        insufficient_line3 = custom_font_small.render(f"more credits", True, (255, 255, 255))
        main_menu.blit(insufficient_line1, (210, 195))
        main_menu.blit(insufficient_line2, (210, 214))
        main_menu.blit(insufficient_line3, (210, 235))

    main_menu.blit(spoon_text, (135, 143))
    main_menu.blit(fork_text, (298, 143))
    main_menu.blit(knife_text, (451, 143))

    main_menu.blit(quit_appear, (590, 18))
    main_menu.blit(credit_text, (22, 18))

    screen.blit((main_menu), (0, 0))

def refresh_button():
    global button1_appear
    global button2_appear
    global button3_appear
    global button

    if owned[0] == True:
        if equip == 0:
            button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[3]))
        else:
            button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[2]))
    else:
        button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[0]))
    button1_appear = pygame.transform.scale(button1_appear, (103, 40))

    if owned[1] == True:
        if equip == 1:
            button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[3]))
        else:
            button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[2]))
    else:
        button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[0]))
    button2_appear = pygame.transform.scale(button2_appear, (103, 40))

    if owned[2] == True:
        if equip == 2:
            button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[3]))
        else:
            button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[2]))
    else:
        button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", button[0]))
    button3_appear = pygame.transform.scale(button3_appear, (103, 40))

def select(item: int, money: int) -> bool: # Check to see if there are sufficient funds
    if price[item] > money:
        return False
    else:
        return True

# class Object:

running = True
clock = pygame.time.Clock()

while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
                

    # GAME STATE UPDATES
    # All game math and comparisons happen here
    refresh_button()
    mouse_pos = pygame.mouse.get_pos()
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        if buy or insufficient:
            if quit_buy_appear.collidepoint(mouse_pos):
                current_buy = -1
                buy = False             # If buy screen should appear
                insufficient = False    # If insufficient funds screen should appear
            if ok_click.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if buy:
                    credit = credit - price[current_buy]
                    credit_text = custom_font_small.render("Credit: " + str(credit), True, (255, 255, 255))   
                    owned[current_buy] = True
                current_buy = -1
                buy = False             # If buy screen should appear
                insufficient = False    # If insufficient funds screen should appear
        else:
            if button1_click.collidepoint(mouse_pos):
                print("Button clicked!")
                if owned[0] == True:
                    equip = 0
                else:
                    current_buy = 0
                    if select(0, credit) == True:
                        buy = True
                    else:
                        insufficient = True
            elif button2_click.collidepoint(mouse_pos):
                print("Button clicked!")
                if owned[1] == True:
                    equip = 1
                else:
                    current_buy = 1
                    if select(1, credit) == True:
                        buy = True
                    else:
                        insufficient = True
            elif button3_click.collidepoint(mouse_pos):
                print("Button clicked!")
                if owned[2] == True:
                    equip = 2
                else:
                    current_buy = 2
                    if select(2, credit) == True:
                        buy = True
                    else:
                        insufficient = True
            elif quit_click.collidepoint(mouse_pos):
                print("Exit!")
            ## Leave Menu Screen

    # DRAWING
    screen.fill((0, 0, 35))  # always the first drawing command]
    shop()

    print(mouse_pos)
    # # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)

    #---------------------------

pygame.quit()
