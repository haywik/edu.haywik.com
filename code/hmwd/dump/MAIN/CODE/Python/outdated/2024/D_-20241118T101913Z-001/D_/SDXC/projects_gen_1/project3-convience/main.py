# project convience
# primary consiering pyautogui and automating tasks unsing python
# such as start up


##


import time,os,subprocess,pyautogui,threading,platform,webbrowser


def school_startup():
    print("School startup")

    webbrowser.open("classroom.google.com")

    os.startfile('explorer.exe')



school_startup()