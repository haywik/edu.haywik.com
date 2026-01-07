import random,time
import pyautogui as po
from keyboard import is_pressed
import keyboard
po.PAUSE = 0.015

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
text=""
x = 0
print("Start in 5s")
time.sleep(5)

num_cap = random.randint(2,9)
while True:
    if is_pressed('`'):
        po.prompt("end")
        break
    
    
    
    

   
    num_alpha = random.randint(0, len(alpha) - 1)

    text = alpha[num_cap]

    po.typewrite(text)
   
    x = x +1
    if x == num_cap:
        #po.press('enter')
        #keyboard.press_and_release('enter')
        po.leftClick()
        print("enter")
        num_cap = random.randint(2,9)
        x = 0
        
    
