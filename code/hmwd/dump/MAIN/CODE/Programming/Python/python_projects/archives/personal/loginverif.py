import pyautogui as po
import keyboard

import time


time.sleep(5)
print("delay end")
def right():
    while True:
        if keyboard.is_pressed('p'):
            time.sleep(0.2)
            print("break")
            break
            break
    
        po.rightClick()
        if keyboard.is_pressed('p'):
            time.sleep(0.2)
            print("break")
            break
            break
            



while True:
    
    if keyboard.is_pressed('p'):
        time.sleep(0.2)
        print("right start")
        right()
