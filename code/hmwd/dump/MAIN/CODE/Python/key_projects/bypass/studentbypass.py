import subprocess,os,time
from keyboard import is_pressed

global connect



#taskkill /im SRService.exe /t /f

def primary():
    print("primary start")
    while True:
     
        if is_pressed('`'):
            print("\n\nrelease")
            y=subprocess.run("ipconfig /release",shell=True)
            print(y)
            time.sleep(1)
            
            while True:
                
                if is_pressed('`'):
                    
                    print("\n\nrenew")
                    x=subprocess.run('ipconfig /renew',capture_output=True,text=True)
                    print(x)
                    time.sleep(1)
                    
                    primary()

                    
os.popen('task_end.py')
primary()
