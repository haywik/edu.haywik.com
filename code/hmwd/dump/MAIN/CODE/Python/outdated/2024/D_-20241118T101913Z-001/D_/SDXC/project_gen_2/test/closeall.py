import subprocess,time,keyboard
import psutil
from pynput import keyboard
x =0
def close_all_back():
    print("closing all")

    subprocess.run('taskkill /F /FI "IMAGENAME ne " /FI "IMAGENAME ne fontdrvhost.exe" /FI "IMAGENAME ne svchost.exe" /FI "IMAGENAME ne python.exe" /FI "IMAGENAME ne pythonw.exe" /FI "IMAGENAME ne mkchelper.exe" /FI "IMAGENAME ne chrome.exe" /FI "IMAGENAME ne closeall.py" /FI "STATUS eq running"')
    

        
        
    
    return "closing all" 




def display_tasks():
    print(f"{'PID':<10}{'Process Name':<25}{'CPU%':<10}{'Memory%':<10}")
    print("=" * 55)
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']
            cpu = proc.info['cpu_percent']
            memory = proc.info['memory_percent']
            print(f"{pid:<10}{name:<25}{cpu:<10}{memory:<10.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


 
while x < 300:
    
    time.sleep(1)
    close_all_back()
    #display_tasks()
    x=x+1
    
