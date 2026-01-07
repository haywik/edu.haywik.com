import keyboard
import pyautogui



while True:

    if keyboard.read_key() == "q":
        print("program exit")
        exit()

    if keyboard.read_key() == "z":
        pyautogui.click(601,430)
        
        
    if keyboard.read_key() == "x":
        pyautogui.click(545,466)
        
        
    if keyboard.read_key() == "c":
        pyautogui.click(544,523)
       
    if keyboard.read_key() == "v":
        pyautogui.click(622,573)
        
    if keyboard.read_key() == "a":
        pyautogui.click(353,680)



