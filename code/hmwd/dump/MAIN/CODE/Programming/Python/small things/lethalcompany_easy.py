import keyboard,time
import pyautogui as po

import pytesseract
import mss
from PIL import Image


print("Starting lethal compnay auto right clickers")

def click():
    print("clicking")
    while True:
        if keyboard.is_pressed('F6'):
            print("clicking stopped")
            start()
            break
        po.rightClick()
        time.sleep(0.2)
        if keyboard.is_pressed('F6'):
            print("clicking stopped")
            start()
            break
            
            
def safety(target):
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])  # Capture Screen 1
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)  
        text = pytesseract.image_to_string(img).lower()  # Extract text (convert to lowercase)
        
        if target.lower() in text:
            print(f"Found '{target}' on the screen!")


            
def start():
    print("program start")
    while True:
        time.sleep(0.1)
        if keyboard.is_pressed('F6'):
            click()
            
            
#start()

while True:
    time.sleep(1)
    #safety("entrace")
    start()

#home,    ##does not work the best when transparency behind text
