import pygame
import os
from background import Background
import json
import constants as c

pygame.init()    

class MainMenu:
    # uploading all buttons
    def __init__(self):
        self.options_button = pygame.image.load(os.path.join("downloads", "optionsbutton.png"))
        self.options_button = pygame.transform.scale(self.options_button,(95,45))
        self.options_button_rect = self.options_button.get_rect()

        self.store_button = pygame.image.load(os.path.join("downloads", "storebutton.png"))
        self.store_button = pygame.transform.scale(self.store_button,(100,50))
        self.store_button_rect = self.store_button.get_rect()

        self.play_button = pygame.image.load(os.path.join("downloads", "playbutton.png"))
        self.play_button = pygame.transform.scale(self.play_button,(200,80))
        self.play_button_rect = self.play_button.get_rect()

        self.settings_button = pygame.image.load(os.path.join("downloads", "settingsbutton.png"))
        self.settings_button = pygame.transform.scale(self.settings_button,(135,52))
        self.settings_button_rect = self.settings_button.get_rect()

        self.quit_button = pygame.image.load(os.path.join("downloads", "quitbutton.png"))
        self.quit_button = pygame.transform.scale(self.quit_button,(136,52))
        self.quit_button_rect = self.quit_button.get_rect()

        self.x_button = pygame.image.load(os.path.join("downloads", "exitbutton.png"))
        self.x_button = pygame.transform.scale(self.x_button,(40,40))

        self.logo = pygame.image.load(os.path.join("downloads", "sprinkle_sprint_official.png"))
        self.logo = pygame.transform.scale(self.logo,(370, 250))

    # options screen
    def options(self, screen, donut_count, owned, equip, speed_index, colour_index):
        with open('game_state.json', 'r') as f:
            game_state = json.load(f)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 5 <= mouse[0] <= 48 and 5 <= mouse[1] <= 48:
                        return
                    elif 248 <= mouse[0] <= 384 and 150 <= mouse[1] <= 200:
                        self.settings(screen, colour_index) # settings button
                        if c.COLOUR == c.COLOUR_PINK:
                            colour_index = 0
                        elif c.COLOUR == c.COLOUR_YELLOW:
                            colour_index = 1
                        elif c.COLOUR == c.COLOUR_BLUE:
                            colour_index = 2
                    elif 248 <= mouse[0] <= 384 and 220 <= mouse[1] <= 272:
                        game_state["donut_count"] = donut_count
                        game_state["owned"] = owned
                        game_state["equip"] = equip
                        game_state["speed_index"] = speed_index
                        game_state["colour_index"] = colour_index
                        with open('game_state.json', 'w') as f:
                            json.dump(game_state, f)
                        pygame.quit() # quits window

            pygame.display.set_caption("options")

            screen.fill(c.COLOURS[colour_index])
            screen.blit(self.settings_button,(248,150))
            screen.blit(self.quit_button,(248,220))
            screen.blit(self.x_button,(8,8))

            mouse = pygame.mouse.get_pos()

            pygame.display.update()
        
        pygame.quit()


    # settings screen (placeholder)
    def settings(self, screen, colour_index):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 5 <= mouse[0] <= 48 and 5 <= mouse[1] <= 48:
                        return # exit to main screen
                    elif 130 <= mouse[0] <= 230 and 115 <= mouse[1] <= 155:
                        c.COLOUR = c.COLOUR_PINK
                        colour_index = 0
                    elif 270 <= mouse[0] <= 370 and 115 <= mouse[1] <= 155:
                        c.COLOUR = c.COLOUR_YELLOW
                        colour_index = 1
                    elif 410 <= mouse[0] <= 510 and 115 <= mouse[1] <= 155:  
                        c.COLOUR = c.COLOUR_BLUE
                        colour_index = 2
                    elif 130 <= mouse[0] <= 230 and 265 <= mouse[1] <= 305:
                        c.SPEED = c.FOREGROUND_SPEED
                    elif 270 <= mouse[0] <= 370 and 265 <= mouse[1] <= 305:
                        c.SPEED = c.FOREGROUND_SPEED_MEDIUM
                    elif 410 <= mouse[0] <= 510 and 265 <= mouse[1] <= 305:
                        c.SPEED = c.FOREGROUND_SPEED_FAST
            
            pygame.display.set_caption("settings")

            button_x = 270
            button_y = 115

            font = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 30)
            smallfont = pygame.font.Font("downloads/font/Pixel Digivolve.ttf", 20) 

            screen.fill(c.COLOURS[colour_index])

            pygame.draw.rect(screen,(204,125,85),[button_x - 140,button_y,100,40])
            pygame.draw.rect(screen,(204,125,85),[button_x,button_y,100,40])
            pygame.draw.rect(screen,(204,125,85),[button_x + 140,button_y,100,40])
            pygame.draw.rect(screen,(204,125,85),[button_x - 140,button_y + 150,100,40])
            pygame.draw.rect(screen,(204,125,85),[button_x,button_y + 150,100,40])
            pygame.draw.rect(screen,(204,125,85),[button_x + 140,button_y + 150,100,40])

            mouse = pygame.mouse.get_pos()

            if 130 <= mouse[0] <= 230 and 115 <= mouse[1] <= 155:
                pygame.draw.rect(screen,(252, 136, 163),[button_x - 140,button_y,100,40])
                self.colour_index = 0
            elif 270 <= mouse[0] <= 370 and 115 <= mouse[1] <= 155:
                pygame.draw.rect(screen,(255,210,90),[button_x,button_y,100,40])
                self.colour_index = 1
            elif 410 <= mouse[0] <= 510 and 115 <= mouse[1] <= 155:  
                pygame.draw.rect(screen,(134, 204, 227),[button_x + 140,button_y,100,40])
                self.colour_index = 2
            elif 130 <= mouse[0] <= 230 and 265 <= mouse[1] <= 305:
                pygame.draw.rect(screen,(152,195,119),[button_x - 140,button_y + 150,100,40])
            elif 270 <= mouse[0] <= 370 and 265 <= mouse[1] <= 305:
                pygame.draw.rect(screen,(152,195,119),[button_x,button_y + 150,100,40])
            elif 410 <= mouse[0] <= 510 and 265 <= mouse[1] <= 305:
                pygame.draw.rect(screen,(152,195,119),[button_x + 140,button_y + 150,100,40])

            background = font.render('background',font,(255, 255, 255)) 
            screen.blit(background,(217,50))
            difficulty = font.render('difficulty',font,(255, 255, 255)) 
            screen.blit(difficulty,(235,200))
            pink = smallfont.render('pink',True,(255, 255, 255))
            screen.blit(pink,(156,120))
            yellow = smallfont.render('yellow',True,(255, 255, 255)) 
            screen.blit(yellow,(280,120))
            blue = smallfont.render('blue',True,(255, 255, 255)) 
            screen.blit(blue,(434,120))
            normal = smallfont.render('easy',True,(255, 255, 255)) 
            screen.blit(normal,(153,270))
            hard = smallfont.render('medium',True,(255, 255, 255)) 
            screen.blit(hard,(282,270))
            expert = smallfont.render('hard',True,(255, 255, 255)) 
            screen.blit(expert,(433,270))

            screen.blit(self.x_button,(8,8))

            pygame.display.update()
        
        pygame.quit()

    
    # store screen (placeholder)
    def store(self, screen):
        running = True
        while running:        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 5 <= mouse[0] <= 48 and 5 <= mouse[1] <= 48:
                        return # exit to main screen
                    
            pygame.display.set_caption("store")

            screen.fill(c.COLOUR)
            screen.blit(self.x_button,(8,8))


            mouse = pygame.mouse.get_pos()

            pygame.display.update()

        pygame.quit()


    # main screen 
    def main_menu(self, screen, background, colour_index):
        pygame.display.set_caption("game")

        background.update_background_main_menu(screen, c.COLOURS[colour_index])
        screen.blit(self.options_button,(6, 3))
        screen.blit(self.store_button,(540, 1))
        screen.blit(self.play_button,(210,250))
        screen.blit(self.logo, (125, 30))
        self.play_button_rect.topleft = (210, 250)
        self.options_button_rect.topleft = (6, 3)
        self.store_button_rect.topleft = (540, 1)
