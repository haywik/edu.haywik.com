

print("task_end starting")
import subprocess,time,os

subprocess.run("chrome.exe",shell=True)
def secondary():

    print("taskkilling")

    subprocess.run('taskkill /im student.exe /t /f',shell=True,capture_output=False)
    subprocess.run('taskkill /im WAgent.exe /t /f',shell=True,capture_output=False)
    subprocess.run('taskkill /im lskHlpr64.exe /t /f',shell=True,capture_output=False)
    subprocess.run('taskkill /im SRAgent.exe /t /f',shell=True,capture_output=False)
    subprocess.run('taskkill /im AgentPackageMonitoring.exe /t /f',shell=True,capture_output=False)
    subprocess.run('taskkill /im BridgeCommunication.exe /t /f',shell=True,capture_output=False)
    os.system("cls")

while True:
    time.sleep(0.75)
    secondary()
