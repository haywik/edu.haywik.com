print("starting main.py -- hot iron")

import time
import pygame as p


#start pygamne
p.init() 
#set up display configs
width = 1500
height = 800
screen = p.display.set_mode((width,height))
#how fast the scren updates
clock = p.time.Clock()
running=True

#varibles
background = "white"
screen.fill(background)
p_colour = "white"
#player
scale = 50
player = p.image.load("assests\mouse.png")
player = p.transform.scale(player,(scale,scale))
p_x = width // 2 - scale // 2
p_y = height // 2 - scale // 2
speed =4

#buttons

start_button = p.image.load("assests\start_button.png")
start_button = p.transform.scale(start_button, (200,100))

while running:
    clock.tick(60)
    #if user presses x button in top right

    for event in p.event.get():
        print(f"Event:{event}")
        if event.type == p.QUIT:
            running=False
        elif event.type == p.KEYDOWN:
            if event.key == p.K_SPACE:
                p_colour = "red"
        
        elif event.type == p.KEYUP:
            if event.key == p.K_SPACE:
                p_colour = "white"
    
   
    key = p.key.get_pressed()

    if key[p.K_w]:
        p_y = p_y - speed

    if key[p.K_s]:
        p_y = p_y + speed   
    
    if key[p.K_a]:
        p_x = p_x - speed       

    if key[p.K_d]:  
        p_x = p_x + speed

    p_x = max(0 ,min(width - scale, p_x))
    p_y = max(0 ,min(height - scale, p_y))

    screen.fill(background)


    #start button
    screen.blit(start_button,(width/2-200,height/2-100))

    
    screen.blit(player,(p_x,p_y))

    


   
        
    

    p.display.update()
 



p.quit()












#splendid
