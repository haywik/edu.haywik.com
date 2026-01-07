import subprocess, os, time, platform

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

hub_bat = r"C:\Users\ross\Documents\python\console_code_network\project 2\networkhub.bat"

#"C:\Users\ross\Documents\python\console_code_network\project 2\networkhub.bat"

#"D:\python\console_code_network\project 2\networkhub.bat"

booster_bat = r"C:\Users\ross\Documents\python\console_code_network\project 2\netweork-hub-booster.bat"

#"C:\Users\ross\Documents\python\console_code_network\project 2\netweork-hub-booster.bat"

#D:\python\console_code_network\project 2\netweork-hub-booster.bat"

sync_bat = r"C:\Users\ross\Documents\python\console_code_network\project 2\blink-sync-mod.bat"

#"C:\Users\ross\Documents\python\console_code_network\project 2\blink-sync-mod.bat"


#"D:\python\console_code_network\project 2\blink-sync-mod.bat"


items = [hub_bat, booster_bat, sync_bat]
x = 0
while True:
    error = 0

    x = x + 1
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

    if error == 1:
        print(RED+"#################################__ERROR__#########################"+RESET)

    print(i1, "\n", i2, "\n", i3)

    if error == 1:
        print(RED+"#################################__ERROR__#########################"+RESET)


