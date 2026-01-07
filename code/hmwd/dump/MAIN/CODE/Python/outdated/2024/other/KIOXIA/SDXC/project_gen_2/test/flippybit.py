import pyautogui as po
import random
while True:
    x = random.randint(1,8)
    y = random.randint(0,1)

    if x == 1:
        po.moveTo(1240,860)
    elif x == 2:
        po.moveTo(1302,862)
    elif x ==3:
        po.moveTo(1365,857)
    elif x ==4:
        po.moveTo(1415,865)
    elif x==5:
        po.moveTo(1486,852)
    elif x==6:
        po.moveTo(1549,866)
    elif x==7:
        po.moveTo(1615,857)
    elif x==8:
        po.moveTo(1670,867)

    if y==1:
        
        po.click()

    

        
