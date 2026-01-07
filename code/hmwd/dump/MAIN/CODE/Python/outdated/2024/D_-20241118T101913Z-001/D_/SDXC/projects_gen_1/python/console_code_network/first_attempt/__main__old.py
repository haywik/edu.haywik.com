import subprocess, os, time, platform
import tkgui
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"
set_f = 0
a = 0
b=0
c=0
hub_bat = r"D:\python\console_code_network\project 2\networkhub.bat"

#"C:\Users\ross\Documents\python\console_code_network\project 2\networkhub.bat"

booster_bat = r"D:\python\console_code_network\project 2\netweork-hub-booster.bat"

#"C:\Users\ross\Documents\python\console_code_network\project 2\netweork-hub-booster.bat"

sync_bat = r"D:\python\console_code_network\project 2\blink-sync-mod.bat"

#"C:\Users\ross\Documents\python\console_code_network\project 2\blink-sync-mod.bat"



def hub_wifi(arg):
    pass

items = [hub_bat, booster_bat, sync_bat]
x = 0
def calculate(a,b,c):
    error = 0
    set_f=0

    print(x)
    for i in items:
        result = subprocess.run([i], capture_output=True, text=True, shell=True)

        result = str(result)

        if "Reply from" in result and "unreachable" not in result:

            #runs if ping was able to get a reply

            if "networkhub.bat" in i:
                i1 = "Hub(192.169.0.1)-Good"
                i1 = GREEN + i1 + RESET

            elif "netweork-hub-booster.bat" in i:
                i2 = "Hub_Booster(192.168.0.26)-Good"
                i2 = GREEN + i2 + RESET

            elif "blink-sync-mod.bat" in i:
                i3 = "Blink_Mod(192.168.0.26)-Good"
                i3 = GREEN + i3 + RESET
        else:



            if "networkhub.bat" in i:
                i1 = "Hub(192.169.0.1)-Bad"
                i1 = RED + i1 + RESET
                error = 1
            elif "netweork-hub-booster.bat" in i:
                i2 = "Hub_Booster(192.168.0.26)-Bad"
                i2 = RED + i2 + RESET
                error = 1

            elif "blink-sync-mod.bat" in i:
                i3 = "Blink_Mod(192.168.0.26)-Bad"
                i3 = RED + i3 + RESET
                error = 1
    
    os.system('cls')

    set_f = 1

    a = i1
    b=i2
    c=i3
    print(a,i1)
    return i1,i2,i3




re = calculate(a,b,c)

print(re)