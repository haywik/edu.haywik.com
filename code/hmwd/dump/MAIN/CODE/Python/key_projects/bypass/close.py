import subprocess
import time


while True:
    time.sleep(1)


    x = subprocess.run('taskkill /F /FI "Status eq running" /FI "IMAGENAME ne chrome.exe" /FI "IMAGENAME ne pythonw.exe" /FI "IMAGENAME ne python.exe" /FI "IMAGENAME ne py.exe" /FI "IMAGENAME ne close.exe" /FI "IMAGENAME ne cmd.exe" /FI "IMAGENAME ne powershell.exe" /FI "IMAGENAME ne explorer.exe"')

    print(x)
