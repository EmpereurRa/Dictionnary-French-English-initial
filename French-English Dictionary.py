import pygame
import time
import sys
from TextBoxfile2 import *

pygame.init()

window = pygame.display.set_mode((1500,750))

white = (255,255,255)
black = (0,0,0)
gray = (90,90,90)
red = (200,0,0)
light_red = (255,0,0)
green = (34,177,76)
light_green = (0,255,0)
light_blue = (0,0,200)
blue = (0,0,255)
silver = (200,200,200)
orange = (200,100,20)
light_orange = (200,100,80)
dark_yellow = (155,155,0)
yellow = (200,200,0)
light_yellow = (255,255,0)

pygame.display.set_caption('French-English Dictonary')

icon = pygame.image.load('France Flag.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

block_size = 10
TIME = 15

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 70)

text_boxes = []
text_boxes.append(Text_box(600,400,300,50, border=4))

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(window, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                pass
                #controls()

            if action == "StartEng":
                DictInEnglish()

            if action == "StartFre":
                StartFre()

            if action == "astl1":
                astt1()

            if action == "back":
                game_intro()

    else:
        pygame.draw.rect(window, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)


    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    window.blit(textSurf, textRect)


def messaage_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (1500 / 2), (750 / 2)+y_displace
    window.blit(textSurf, textRect)
    
def Dict():

    intro = True

    while intro:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        window.fill(black)
        messaage_to_screen("French Dictionary/Dictionnaire Français ",
                           blue,
                           -100,
                           "large")               

        button("Exit", 100,600,100,50, red, light_red, action="quit")
        button("English", 500,500,100,50, yellow, light_yellow, action="StartEng")
        button("Français", 900,500,100,50, green, light_green, action="StartFre")

        pygame.display.update()
        clock.tick(15)

def DictInEnglish():
     
  # English = True

  # while English:
        
  #     for event in pygame.event.get():
  #         if event.type == pygame.QUIT:
  #             pygame.quit()
  #             quit()
  #     
  #         if event.type == pygame.KEYDOWN:
  #             if event.key == pygame.K_g:
  #                 English = False
  #             if event.key == pygame.K_q:
  #                 pygame.quit()
  #                 quit()
        
        window.fill(black)  
        running = True
        while running:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for box in text_boxes:
                        box.check_click(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    for box in text_boxes:
                        if box.active:
                            box.add_text(event.key)

            window.fill((54,54,54))

            for box in text_boxes:
                box.draw(window)


            button("Exit", 100,600,100,50, red, light_red, action="quit")

            messaage_to_screen("French dictionary",
                               blue,
                               -100,
                               "large") 
            pygame.display.update()

def StartFre():

        window.fill(black)  
        Français= True
        while Français:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for box in text_boxes:
                        box.check_click(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN:
                    for box in text_boxes:
                        if box.active:
                            box.add_text(event.key)

            window.fill((54,54,54))

            for box in text_boxes:
                box.draw(window)


            button("Exit", 100,600,100,50, red, light_red, action="quit")

            messaage_to_screen("Dictionnaire Anglais",
                               blue,
                               -100,
                               "large") 
            pygame.display.update()

Dict()








