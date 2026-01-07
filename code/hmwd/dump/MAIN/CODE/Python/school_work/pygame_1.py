import keyboard 
import pygame
import pyautogui as po
import time,os,subprocess
import time
from pygame.locals import *
from pygame import rect


pygame.init()
screen = pygame.display.set_mode((1000,500))

rect = ball.get_rect()



run = True
speed = 5

while run:
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                rect = rect.move(speed)
            elif e.key == pygame.K_p:
                pygame.quit()
        
        

