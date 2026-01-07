import pyautogui as po
import PIL
import pyscreeze
import time,os#
import platform
import os
import socket
import subprocess,re
protocle= [
    'help="help"'
    'Hub Reboot = "hub_reboot"'
    'Homework = "homework"'
    'Computer Science setup = "ict"'  
    'System Info = "system_info'
    'Command Prompt = "cmd_prompt"'
    'task manager = "task_manager"'
    'install = "install"'
]

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

    delay = 0.45
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
    time.sleep(delay)

    po.hotkey('ctrl', 't')
    po.write("https://smartrevise.online/student/home/Index")
    time.sleep(delay)
    po.press('enter')
    time.sleep(delay)

    po.hotkey('ctrl', 't')
    po.typewrite("https://docs.google.com/spreadsheets/d/1fK5HU2xedO0vVLm3_EwjL_fYOVhnBkeklmmzI3wkSsw/edit?gid=0#gid=0")
    time.sleep(delay)
    po.press('enter')
    
    
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

    po.hotkey('ctrl', 't')
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

    po.hotkey('ctrl', 't')
    po.typewrite("https://smartrevise.online/student/home/Index")
    time.sleep(delay)
    po.press('enter')

    po.hotkey('ctrl', 't')
    po.typewrite("https://docs.google.com/document/d/1e0WUW43KrkTKIwcW-TdlbdM4OdbyB7vJ-1ntqSu35lM/edit")
    time.sleep(delay)
    po.press('enter')

    po.hotkey('ctrl', 't')
    po.typewrite("https://docs.google.com/spreadsheets/d/1fK5HU2xedO0vVLm3_EwjL_fYOVhnBkeklmmzI3wkSsw/edit?gid=0#gid=0")
    time.sleep(delay)
    po.press('enter')

    po.hotkey('ctrl', 't')
    po.typewrite("")
    time.sleep(delay)
    po.press('enter')

    for i in range(5):
        i = str(i)
        po.hotkey('ctrl', i)
        time.sleep(1)

    time.sleep(delay)
    po.hotkey('ctrl', 't')

   
def personal():  ##not finished   just a copy of school_ict currently
    print("personal mode start")
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

    po.hotkey('ctrl', 't')
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

    po.hotkey('ctrl', 't')
    po.typewrite("https://smartrevise.online/student/home/Index")
    time.sleep(delay)
    po.press('enter')

    po.hotkey('ctrl', 't')
    po.typewrite("https://docs.google.com/document/d/1e0WUW43KrkTKIwcW-TdlbdM4OdbyB7vJ-1ntqSu35lM/edit")
    time.sleep(delay)
    po.press('enter')

    po.hotkey('ctrl', 't')
    po.typewrite("")
    time.sleep(delay)
    po.press('enter')

    for i in range(5):
        i = str(i)
        po.hotkey('ctrl', i)
        time.sleep(1)

    time.sleep(delay)
    po.hotkey('ctrl', 't')

def revision():

    print("revision mode start")
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


    
    po.typewrite("https://docs.google.com/document/d/1e0WUW43KrkTKIwcW-TdlbdM4OdbyB7vJ-1ntqSu35lM/edit")
    time.sleep(delay)
    po.press('enter')

    for i in range(5):
        i = str(i)
        po.hotkey('ctrl', i)
        time.sleep(1)

    time.sleep(delay)
    po.hotkey('ctrl', 't')

    


def get_system_info():
    uname = platform.uname()

    print("System:", uname.system)
    print("Node:", uname.node)
    print("Release:", uname.release)
    print("Version:", uname.version)
    print("Machine:", uname.machine)
    print("Processor:", uname.processor)
    print("Hostname:", socket.gethostname())
    print("IP address:", socket.gethostbyname(socket.gethostname()))
    print("\nEnvironment Variables:")

    md = input("more details? Y/N").lower()
    if md == "y":

        for key, value in os.environ.items():
            print(f"{key}: {value}")
        print("\nCPU Information:")
        if uname.system == "Windows":
            out = subprocess.run("wmic cpu get caption, MaxClockSpeed", capture_output=True, text=True, shell=True)
            out3 = out.stdout
            out2 = out3.replace("CompletedProcess(args='wmic cpu get caption, MaxClockSpeed', returncode=0)", "")
            print(out2)
        else:
            cpu_info = subprocess.check_output("lscpu", shell=True).decode()
            print(cpu_info)

        print("\nMemory Information:")
        if uname.system == "Windows":
            memory_info = subprocess.check_output("systeminfo | findstr /C:\"Total Physical Memory\"", shell=True).decode()
            print(memory_info)
        else:
            memory_info = subprocess.check_output("free -h", shell=True).decode()
            print(memory_info)


def command_prompt():
    print("starting command_prompt")
    print("Info: type exit to exit \n :  Type shell=True to enable subprocess wit shell use \nshell=False to turn off, \n Type config to config")
    config = input("type configs:").lower()
    while True:
        cin = input(":>")
        if cin == "config":
            config = input("type configs:").lower()
            cin = input(":>")
        if cin=="exit":
            exit()
        try:
            if config=="shell=false":
                args = cin.split()
                x = subprocess.run(args,capture_output=True,text=True)
                print(x.stdout)
                print(x.stderr)
            elif config=="shell=true":
                x = subprocess.run(cin,shell=True)
                print(x)
        except Exception as e:
            print("\nerror :")
            print(e)
            print("\n")


def task_manager():
    print("Starting task manager")

def install():
    print("Installing Python Packages")
    import subprocess

    print("Installing Python Packages")

    print("pyautogui:")
    subprocess.run('python -m pip install pyautogui', shell=True)
    print("psutil")
    subprocess.run('python -m pip install psutil', shell=True)
    print("google emails api client")
    subprocess.run('python -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib',
                   shell=True)
    print("updating pip")
    subprocess.run('python -m pip install pip --upgrade', shell=True)

    input("End")


def quick_cmd(x):
    if "shutdown" in x:
        integers = re.findall(r'\d+', x)
        print("intergers",integers)
        for i in integers:
            print("1",i)
            time=i

        run = 'shutdown /f /s /t ' + time
        print(run)

        subprocess.run(run,shell=True)

    elif "refresh" in x:
        while True:
            print("refresh starting close program to stop")
            po.hotkey('ctrl','r')
            time.sleep(1)
    else:
        print("\n Cmd unrecognized \n")
        print(protocle)
    


