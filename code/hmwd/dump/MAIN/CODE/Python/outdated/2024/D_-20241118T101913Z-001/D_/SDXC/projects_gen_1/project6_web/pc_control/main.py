import platform
import os
import socket
import subprocess,time
import pc_control.main_cmds as main_cmds
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
def pc_control_main_portal(cmd):

    if cmd == "help":
        print("help triggered")
    elif cmd == "hub_reboot":
        f =main_cmds.hub_reboot()
    elif cmd == "homework":
        f =main_cmds.homework()
    elif cmd=="ict":
        f =main_cmds.school_ict()
    elif "cmd_prompt" in cmd:
        cmd = cmd.replace("cmd_prompt", "")
        f =main_cmds.command_prompt(cmd)
    elif "test" in cmd:
        print("test")
        return "test"
    else:
        f ="NA"
    return f


