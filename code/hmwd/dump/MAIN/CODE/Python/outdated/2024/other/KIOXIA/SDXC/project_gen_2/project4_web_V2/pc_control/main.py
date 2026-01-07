import platform
import os
import socket
import subprocess,time
import main_cmds
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


#auto minmise cmd
while True:
    cmd = input("\nEnter Command:").lower()

    if cmd == "help":
        print(protocle)
    elif cmd == "hub_reboot":
        main_cmds.hub_reboot()
    elif cmd == "homework":
        main_cmds.homework()
    elif cmd=="ict":
        main_cmds.school_ict()
    elif cmd=="system_info":
        main_cmds.get_system_info()
    elif cmd=="cmd_prompt":
        main_cmds.command_prompt()
    elif cmd=="task_manager":
        main_cmds.task_manager()
    elif cmd == "install":
        main_cmds.install()
    else:
        main_cmds.quick_cmd(cmd)


