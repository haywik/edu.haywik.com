import time,subprocess

while True:
    x=subprocess.run("ipconfig /renew",shell=True)
    print(x)
    time.sleep(3.5)
    x=subprocess.run("ipconfig /release",shell=True)
    print(x)
    time.sleep(0.3)
