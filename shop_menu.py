# pygame template

import pygame
import os
import constants as c

class Shop_menu:
    def __init__(self, owned, equip):
        self.custom_font = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 20)
        self.custom_font_small = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 5)

        self.character = [
            "spoon.png", 
            "fork.png", 
            "knife.png"
            ] 
        self.button = [
            "buy_button.png", 
            "orange_buybutton.webp", 
            "equip_button.png", 
            "equipped_button.png", 
            "new_exit_button.png", 
            "pop_up_screen.png", 
            "ok_button.png"
            ]      
        ## Store the image file for easy changes
        self.price = [0, 50, 50]
        self.character_name = [
            "Spoon", 
            "Fork", 
            "Knife"
            ]
        self.image1 = pygame.image.load(os.path.join("downloads/shop_menu", "shop.png"))

        if owned[0]:
            if equip == 0:
                self.button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[3]))
            else:
                self.button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[2]))
        else:
            self.button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[0]))
        self.button1_appear = pygame.transform.scale(self.button1_appear, (103, 40))

        if owned[1]:
            if equip == 1:
                self.button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[3]))
            else:
                self.button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[2]))
        else:
            self.button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[0]))
        self.button2_appear = pygame.transform.scale(self.button2_appear, (103, 40))

        if owned[2] == True:
            if equip == 2:
                self.button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[3]))
            else:
                self.button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[2]))
        else:
            self.button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[0]))
        self.button3_appear = pygame.transform.scale(self.button3_appear, (103, 40))

        self.spoon_text = self.custom_font.render("spoon", True, (255, 255, 255))
        self.fork_text = self.custom_font.render("fork", True, (255, 255, 255))
        self.knife_text = self.custom_font.render("knife", True, (255, 255, 255))

        self.quit_appear = pygame.image.load(os.path.join("downloads/pause_menu", self.button[4]))
        self.quit_appear = pygame.transform.scale(self.quit_appear, (40, 40))

        self.buy_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[5]))
        self.buy_appear = pygame.transform.scale(self.buy_appear, (470, 200))

        self.button1_click = pygame.Rect(116, 247, 103, 40)  # (x, y, width, height)
        self.button2_click = pygame.Rect(273, 247, 103, 40)  
        self.button3_click = pygame.Rect(430, 247, 103, 40) 
        self.quit_click = pygame.Rect(590, 18, 30, 30) 

        self.custom_font_small = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 15)

        self.current_buy = -1
        self.buy = False             # If buy screen should appear
        self.insufficient = False    # If insufficient funds screen should appear

        self.not_enough_funds_text = self.custom_font.render("Insufficient Funds", True, (255, 255, 255))
        self.ok_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[6]))
        self.ok_appear = pygame.transform.scale(self.ok_appear, (80, 40))

        self.ok_click = pygame.Rect(365, 204, 80, 40) 
        self.quit_buy_appear = pygame.Rect(432, 166, 30, 30) 

# ---------------------------

    def draw_shop(self, screen:pygame, credit, colour_index):
        # Draws the store menu

        # Parameters:
        # credit (int): The amount of collected donuts (game currency)
        # colour_index (int): which color selected

        # Returns:
        # Nothing
        self.x_image = [138, 300, 455]
        screen.fill(c.COLOURS[colour_index])
        screen.blit(self.image1, (0, 0))
        
        screen.blit(self.spoon_text, (135, 143))
        screen.blit(self.fork_text, (298, 143))
        screen.blit(self.knife_text, (451, 143))

        for x in range (3): ## Draw out the sprite images
            self.sprite = pygame.image.load(os.path.join("downloads/shop_menu", self.character[x]))
            self.sprite = pygame.transform.scale(self.sprite, (40, 60))
            screen.blit(self.sprite, (self.x_image[x] + 7, 178))

        self.credit_text = self.custom_font_small.render("Donuts: " + str(credit), True, (255, 255, 255)) # set to 0 for default
        screen.blit(self.button1_appear, (116, 247))
        screen.blit(self.button2_appear, (273, 247))
        screen.blit(self.button3_appear, (430, 247))
        
        if self.buy:
            screen.blit(self.buy_appear, (90, 130))
            screen.blit(self.quit_appear, (432, 166))
            screen.blit(self.ok_appear, (365, 204))

            self.purchase_line1 = self.custom_font_small.render(f"Purchase {self.character_name[self.current_buy]}", True, (255, 255, 255))
            self.purchase_line2 = self.custom_font_small.render(f"for {self.price[self.current_buy]} donuts?", True, (255, 255, 255))
            screen.blit(self.purchase_line1, (225, 199))
            screen.blit(self.purchase_line2, (225, 219))

        if self.insufficient:
            screen.blit(self.buy_appear, (90, 130))
            screen.blit(self.quit_appear, (432, 166))
            screen.blit(self.ok_appear, (365, 204))

            insufficient_line1 = self.custom_font_small.render(f"Insufficient Funds", True, (255, 255, 255))
            insufficient_line2 = self.custom_font_small.render(f"you need {self.price[self.current_buy]-credit}", True, (255, 255, 255))
            insufficient_line3 = self.custom_font_small.render(f"more donuts", True, (255, 255, 255))
            screen.blit(insufficient_line1, (210, 195))
            screen.blit(insufficient_line2, (210, 214))
            screen.blit(insufficient_line3, (210, 235))

        screen.blit(self.quit_appear, (580, 18))
        screen.blit(self.credit_text, (22, 18))
        

    def refresh_button(self, owned, equip):
        # Updates the state of the buttons

        # Parameters:
        # owned (list): Which sprite the user has bought
        # equip (int): current sprite used

        # Returns:
        # Nothing
        if owned[0]:
            if equip == 0:
                self.button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[3]))
            else:
                self.button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[2]))
        else:
            self.button1_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[0]))
        self.button1_appear = pygame.transform.scale(self.button1_appear, (103, 40))

        if owned[1]:
            if equip == 1:
                self.button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[3]))
            else:
                self.button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[2]))
        else:
            self.button2_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[0]))
        self.button2_appear = pygame.transform.scale(self.button2_appear, (103, 40))

        if owned[2]:
            if equip == 2:
                self.button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[3]))
            else:
                self.button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[2]))
        else:
            self.button3_appear = pygame.image.load(os.path.join("downloads/shop_menu", self.button[0]))
        self.button3_appear = pygame.transform.scale(self.button3_appear, (103, 40))

    def sufficient_funds(self, item: int, money: int) -> bool: # Check to see if there are sufficient funds
        # Checks if there are enough funds

        # Parameters:
        # item (int): Item that user wants to buy
        # money (int): he amount of collected donuts (game currency)

        # Returns:
        # If user is able to buy it or not
        if self.price[item] > money:
            return False
        else:
            return True

    def shop_menu_update(self, owned, mouse_pos, equip, credit):  
        # Updates the shop menu with given parameters

        # Parameters:
        # owned (list): List of owned sprites (boolean).
        # mouse_pos (tuple): Current position of the mouse.
        # equip (int): The current sprite equipped.
        # credit (int): The amount of collected donuts (game currency)

        # Returns:
        # New equip and credit value
        self.refresh_button(owned, equip)  
        if self.buy or self.insufficient:
            if self.quit_buy_appear.collidepoint(mouse_pos):
                self.current_buy = -1
                self.buy = False             # If buy screen should appear
                self.insufficient = False    # If insufficient funds screen should appear
            if self.ok_click.collidepoint(mouse_pos):
                if self.buy:
                    credit = credit - self.price[self.current_buy]
                    self.credit_text = self.custom_font_small.render("Donuts: " + str(credit), True, (255, 255, 255))   
                    owned[self.current_buy] = True
                self.current_buy = -1
                self.buy = False             # If buy screen should appear
                self.insufficient = False    # If insufficient funds screen should appear
        else:
            if self.button1_click.collidepoint(mouse_pos):
                if owned[0]:
                    equip = 0
                else:
                    self.current_buy = 0
                    if self.sufficient_funds(0,  credit):
                        self.buy = True
                    else:
                        self.insufficient = True
            elif self.button2_click.collidepoint(mouse_pos):
                if owned[1]:
                    equip = 1
                else:
                    self.current_buy = 1
                    if self.sufficient_funds(1,  credit):
                        self.buy = True
                    else:
                        self.insufficient = True
            elif self.button3_click.collidepoint(mouse_pos):
                if owned[2]:
                    equip = 2
                else:
                    self.current_buy = 2
                    if self.sufficient_funds(2,  credit):
                        self.buy = True
                    else:
                        self.insufficient = True
            elif self.quit_click.collidepoint(mouse_pos):
                return -1, credit
            
        self.refresh_button(owned, equip)
        return equip, credit