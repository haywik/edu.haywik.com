

#import pyautogui as po
import time
import platform
import os
import socket
import subprocess

test = subprocess.run("help",capture_output=True)
print(test)

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



#get_system_info()
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
                print(x)
                print(x.stdout)
                print(x.stderr)
            elif config=="shell=true":
                x = subprocess.run(["powershell","-Command",cin],capture_output=True)
                print(x.stdout)
        except Exception as e:
            print("\nerror :")
            print(e)
            print("\n")


command_prompt()

while True:
    cmd = input("\nEnter Command:").lower()

    if cmd == "help":
        print(protocle)
    elif cmd == "hub_reboot":
        hub_reboot()
    elif cmd == "homework":
        homework()
    elif cmd=="ict":
        school_ict()
    elif cmd=="system_info":
        get_system_info()
    elif cmd=="cmd_prompt":
        command_prompt()
    elif cmd=="task_manager":
        task_manager()
    elif cmd == "install":
        install()
    else:
        quick_cmd(cmd)


