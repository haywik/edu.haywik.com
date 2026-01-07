import pyttsx3
engine = pyttsx3.init()

import webbrowser,subprocess,datetime,pyautogui

#cmd 1

def open_chrome():
    print("open chrome")
    engine.say("Opening chrome")
  
    subprocess.run("start chrome", shell=True)

def close_chrome():
    print("close chrome")
    engine.say("Closing chrome")
  
    subprocess.run("taskkill /f /im chrome.exe", shell=True)    

def open_website(website):
    
    web = "https://www."+website+".com"
    web = web.replace(" ","")   
    engine.say("opening"+website+".com")
    
    print("opening website",web)
    webbrowser.open(web)
  


#cmd 2


def open_steam():
    print("open steam")
    engine.say("Opening Steam")
    subprocess.run("C:\\Program Files (x86)\\Steam\\steam.exe", shell=True)

def close_steam():   
    print("close steam")
    engine.say("Closing Steam")
    subprocess.run("taskkill /f /im steam.exe", shell=True)


#cmd 3

def get_time():
    print("get time")
    now_time = datetime.datetime.now()
    engine.say("The time is "+str(now_time.hour)+" hours and "+str(now_time.minute)+" minutes")
   

def get_date():
    print("get date")
    now_date = datetime.datetime.now()
    engine.say("The date is "+str(now_date.day)+" "+str(now_date.strftime("%B"))+" "+str(now_date.year))
   

#cmd4



def skip_video():
    print("skip video")
    engine.say("Skipping video")
    pyautogui.hotkey('shift', 'n')


def resume_pause_video():
    print("stop or start video")
    engine.say("Stopping or starting video")
    pyautogui.hotkey('k')


def mute_video():
    print("video auido")
    engine.say("video auidoS")
    pyautogui.hotkey('m')



#cmd5 pc control



def lock_pc():
    print("lock pc")
    engine.say("Locking pc")
    subprocess.run("rundll32.exe user32.dll,LockWorkStation", shell=True)

def shutdown_pc():
    print("shutdown pc")
    engine.say("Shutting down pc")
    subprocess.run("shutdown /s /t 1", shell=True)