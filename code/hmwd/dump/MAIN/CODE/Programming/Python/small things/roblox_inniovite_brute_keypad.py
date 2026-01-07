import pyautogui as po
import time

time.sleep(3)

onex, oney = 875,461
twox,twoy = 944,464
threex,threey =1025,463
fourx,foury = 882,530
fivex,fivey = 955,532
sixx,sixy = 1032,539
sevenx,seveny = 871,611
eightx,eighty = 947,611
ninex,niney = 1020,614
zerox,zeroy = 951,685
enterx,entery = 866,689

count = "3189"

for i in count:
    if i == "1":
        po.moveTo(onex,oney)
        time.sleep(0.1)
        po.click()
        
