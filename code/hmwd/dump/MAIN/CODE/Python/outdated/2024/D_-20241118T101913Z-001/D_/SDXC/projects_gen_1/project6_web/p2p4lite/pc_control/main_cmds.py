import pyautogui as po
import PIL
import pyscreeze
import time,os
import platform
import os
import socket
import subprocess
try:
    import pygetwindow as gw
except:
    print("cant import pygetwindow")
def hub_reboot():
    print("Hub reboot start")
    po.hotkey('super', 'd')

    delay = 0.3
    os.startfile('chrome.exe')
    time.sleep(1)
    window = gw.getActiveWindow()
    if not window.isMaximized:
        po.hotkey('super', 'up')
        time.sleep(delay)
    x, y = 872, 24
    colour = (211, 227, 253)
    time.sleep(1)
    screenshot = po.screenshot()
    if screenshot.getpixel((0, 0)) == (7, 1, 27):
        time.sleep(delay)
        po.hotkey('super', 'shift', 'right')
    for ii in range(10):
        po.hotkey('ctrl', 'w')
    os.startfile('chrome.exe')
    time.sleep(1)
    window = gw.getActiveWindow()
    if not window.isMaximized:
        po.hotkey('super', 'up')
        time.sleep(delay)
    x, y = 872, 24
    colour = (211, 227, 253)
    time.sleep(1)
    screenshot = po.screenshot()
    if screenshot.getpixel((-1002, 106)) == colour or screenshot.getpixel((-1002, 106)) == (56, 38, 42):
        time.sleep(delay)
        po.hotkey('super', 'shift', 'right')
    time.sleep(1)
    po.hotkey('ctrl','t')
    time.sleep(delay)
    po.typewrite("http://192.168.0.1/sky_rebootCPE.html")
    time.sleep(delay)
    po.press('enter')
    time.sleep(3)
    po.press('enter')
    time.sleep(delay)
    po.press('enter')

def homework():
    print("Homework start")
    po.hotkey('super', 'd')

    delay = 0.3
    os.startfile('chrome.exe')
    time.sleep(1)
    window = gw.getActiveWindow()
    if not window.isMaximized:
        po.hotkey('super','up')
        time.sleep(delay)

    x, y = 872,24
    colour = (211, 227, 253)
    time.sleep(1)
    screenshot = po.screenshot()
    #(56, 38, 42)

    if screenshot.getpixel((0,0)) == (7,1,27):
        time.sleep(delay)
        po.hotkey('super','shift','right')
    if screenshot.getpixel((x,y)) == colour :
        time.sleep(delay)
        print("changing user")
        po.moveTo(1847,74)
        time.sleep(delay)
        po.leftClick()
        time.sleep(delay)
        po.moveTo(1647,562)
        time.sleep(delay)
        po.leftClick()

    for ii in range(10):
        po.hotkey('ctrl','w')

    os.startfile('chrome.exe')
    time.sleep(1)
    window = gw.getActiveWindow()
    if not window.isMaximized:
        po.hotkey('super', 'up')
        time.sleep(delay)

    x, y = 872, 24
    colour = (211, 227, 253)
    time.sleep(1)
    screenshot = po.screenshot()
    if screenshot.getpixel((-1002, 106)) == colour or screenshot.getpixel((-1002, 106)) == (56, 38, 42):
        time.sleep(delay)
        po.hotkey('super', 'shift', 'right')
    if screenshot.getpixel((x, y)) == colour:
        time.sleep(delay)
        print("changing user")
        po.moveTo(1847, 74)
        time.sleep(delay)
        po.leftClick()
        time.sleep(delay)
        po.moveTo(1647, 562)
        time.sleep(delay)
        po.leftClick()

    po.moveTo(314,82)
    time.sleep(delay)
    po.leftClick()
    time.sleep(delay)





    time.sleep(1)

    po.typewrite("https://chatgpt.com/?model=auto")
    time.sleep(delay)
    po.press('enter')

    po.moveTo(237, 18)
    time.sleep(delay)
    po.rightClick()
    time.sleep(delay)
    po.press('p')
    time.sleep(delay)

    po.hotkey('ctrl','t')
    time.sleep(delay)
    po.typewrite("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(delay)
    po.press('enter')

    time.sleep(delay)
    po.rightClick()
    time.sleep(delay)
    po.press('p')
    time.sleep(delay)

    po.hotkey('ctrl','t')
    po.typewrite("https://classroom.google.com/a/not-turned-in/all")
    time.sleep(delay)
    po.press('enter')

    time.sleep(delay)
    po.rightClick()
    time.sleep(delay)
    po.press('p')
    time.sleep(delay)

    po.hotkey('ctrl', 't')
    po.typewrite("open.spotify.com")
    time.sleep(delay)
    po.press('enter')

    time.sleep(delay)
    po.rightClick()
    time.sleep(delay)
    po.press('p')
    time.sleep(delay)

    po.hotkey('ctrl', 't')
    po.typewrite("https://vle.mathswatch.co.uk/duocms/api/mw/google")
    time.sleep(delay)
    po.press('enter')
    time.sleep(delay)

    po.hotkey('ctrl', 't')
    po.typewrite("https://app.senecalearning.com/dashboard/assignments/todo")
    time.sleep(delay)
    po.press('enter')
    time.sleep(delay)

    po.hotkey('ctrl', 't')
    po.write("https://classroom.google.com/w/MzcxNTkwNjc4Njcw/tc/Njg1NDc0NDkxMDE2")
    time.sleep(delay)
    po.press('enter')
    time.sleep(5.5)
    po.click(869,910)
    time.sleep(1)
    for i in range(10):
        i = str(i)
        po.hotkey('ctrl',i)
        time.sleep(1)

    time.sleep(delay)
    po.hotkey('ctrl', 't')
    print("Homework finished")
def school_ict():
    print("school_ict start")
    po.hotkey('super', 'd')

    delay = 0.3
    os.startfile('chrome.exe')
    time.sleep(1)
    window = gw.getActiveWindow()
    if not window.isMaximized:
        po.hotkey('super', 'up')
        time.sleep(delay)
    x, y = 872, 24
    colour = (211, 227, 253)
    time.sleep(1)
    screenshot = po.screenshot()
    if screenshot.getpixel((0, 0)) == (7, 1, 27):
        time.sleep(delay)
        po.hotkey('super', 'shift', 'right')
    for ii in range(10):
        po.hotkey('ctrl', 'w')
    os.startfile('chrome.exe')
    time.sleep(1)
    window = gw.getActiveWindow()
    if not window.isMaximized:
        po.hotkey('super', 'up')
        time.sleep(delay)
    x, y = 872, 24
    colour = (211, 227, 253)
    time.sleep(1)
    screenshot = po.screenshot()
    if screenshot.getpixel((-1002, 106)) == colour or screenshot.getpixel((-1002, 106)) == (56, 38, 42):
        time.sleep(delay)
        po.hotkey('super', 'shift', 'right')
    time.sleep(1)
    time.sleep(1)
    po.moveTo(350, 69)
    time.sleep(delay)
    po.leftClick()
    time.sleep(delay)

    po.typewrite("https://copilot.microsoft.com/")
    time.sleep(delay)
    po.press('enter')

    po.moveTo(237, 18)
    time.sleep(delay)
    po.rightClick()
    time.sleep(delay)
    po.press('p')
    time.sleep(delay)

    po.hotkey('ctrl', '2')
    time.sleep(delay)
    po.typewrite("https://mail.google.com/mail/u/0/#inbox")
    time.sleep(delay)
    po.press('enter')

    time.sleep(delay)
    po.rightClick()
    time.sleep(delay)
    po.press('p')
    time.sleep(delay)

    po.hotkey('ctrl', 't')
    po.typewrite("https://classroom.google.com/c/NzA4OTU4MTQ0OTc4")
    time.sleep(delay)
    po.press('enter')

    time.sleep(delay)
    po.rightClick()
    time.sleep(delay)
    po.press('p')
    time.sleep(delay)

    po.hotkey('ctrl', 't')
    po.typewrite("https://docs.google.com/document/d/1qMI3b-iL5D-8qwGFkEctz3M40J-CS_NoiDvd60ee8Gg/edit")
    time.sleep(delay)
    po.press('enter')

    for i in range(5):
        i = str(i)
        po.hotkey('ctrl', i)
        time.sleep(1)

    time.sleep(delay)
    po.hotkey('ctrl', 't')




def command_prompt(x):
    try:
        x = subprocess.run(x,shell=True,capture_output=True,text=True)
        return x
    except:
        return "Error when running",x








    


