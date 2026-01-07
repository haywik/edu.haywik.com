import subprocess
from keyboard import is_pressed
global connect

#taskkill /im SRService.exe /t /f
def secondary():
   

    subprocess.run('taskkill /im student.exe /t /f',shell=True)
    subprocess.run('taskkill /im WAgent.exe /t /f',shell=True)
    subprocess.run('taskkill /im lskHlpr64.exe /t /f',shell=True)
    subprocess.run('taskkill /im SRAgent.exe /t /f',shell=True)
    subprocess.run('taskkill /im AgentPackageMonitoring.exe /t /f',shell=True)
    subprocess.run('taskkill /im BridgeCommunication.exe /t /f',shell=True)


def primary():


    while True:
        secondary()
        if is_pressed('`'):
            print("release")
            y=subprocess.run("ipconfig /release",shell=True)
            print(y)
            

                
            while True:
                secondary()
                if is_pressed('`'):
                    
                    print("renew")
                    x=subprocess.run('ipconfig /renew',capture_output=True,text=True)
                    print(x)
                    
                    primary()

while True:
    secondary()
    
    primary()


