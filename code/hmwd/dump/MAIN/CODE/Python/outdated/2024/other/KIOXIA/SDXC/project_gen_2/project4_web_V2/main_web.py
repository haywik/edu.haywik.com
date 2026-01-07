from flask import Flask,render_template,jsonify,request,abort
import subprocess,datetime
import pc_control.main_cmds
import pc_control.main_cmds
import pc_control.main_cmds
from datetime import *
import time
import pyautogui as po
start_time = datetime.now()
app = Flask(__name__)
whitelist_ips = ['192.168.0.53','192.168.0.7','192.168.0.70','192.168.0.65','172.31.218.185']
def check_ip():
    client_ip = request.remote_addr
    if client_ip not in whitelist_ips:
        abort(403)

@app.before_request
def sc_ip():
    check_ip()

@app.route('/')
def index():
    
    now = datetime.now()
    up_time = now - start_time
    up_time = str(up_time).split(".")[0]
    print(f"uptime:{up_time}")
    return render_template('index.html',up_time=up_time)



@app.route('/reboot-network',methods=['POST'])
def network_reboot_back():
    print("rebooting Network")
    import pc_control
    from pc_control.main_cmds import hub_reboot
    hub_reboot()
    return "hub rebooting"



@app.route('/server-shutdown',methods=['POST'])
def server_shutdown_back():
    print("server shutdown")
    subprocess.run("netsh wlan disconnect",shell=True)
    return "Server Shutting Down",200

@app.route('/machine-shutdown',methods=['POST'])

def machine_shutdown_back():
    print("shutting down machine")
    subprocess.run("rundll32.exe user32.dll,LockWorkStation",shell=True)
    return "Machine Shutting Down 10 seconds",200

@app.route('/machine-lock',methods=['POST'])
def machine_lock_back():
    print("locking machine")
    subprocess.run("shutdown /l")
    return "Machine Locking"    

@app.route('/close-all',methods=['POST'])
def close_all_back():
    print("closing all")
    subprocess.run('taskkill /F /FI "IMAGENAME ne WindowsTerminal.exe" /FI "IMAGENAME ne python.exe" /FI "IMAGENAME ne main_web.exe" /FI "STATUS eq running"')
    return "closing all" 

@app.route('/close-stated',methods=['POST'])
def close_stated_back():
    subprocess.run("taskkill /f /im chrome.exe",shell=True)
    return "Killed stated"

@app.route('/run-eco',methods=['POST'])
def start_eco_back():
    print("starting Eco")
    po.press('super')
    time.sleep(0.3)
    po.typewrite('eco')
    time.sleep(0.5)
    po.press('enter')
    return "starting Eco"
'''
@app.route('/',methods=['POST'])
def ():    
'''
@app.route('/run-mc',methods=['POST'])
def start_mc_back():
    print("starting Minecraft")
    po.press('super')
    time.sleep(0.3)
    po.typewrite('minecraft')
    time.sleep(0.5)
    po.press('enter')
    return "starting mc"

@app.route('/run-roblox',methods=['POST'])
def start_roblox_back():
    print("starting roblox")
    po.press('super')
    time.sleep(0.3)
    po.typewrite('roblox')
    time.sleep(0.5)
    po.press('enter')
    return "starting roblox"


@app.route('/run-forts',methods=['POST'])
def start_forts_back():
    print("starting forts")
    po.press('super')
    time.sleep(0.3)
    po.typewrite('forts')
    time.sleep(0.5)
    po.press('enter')  
    return "starting forts"

@app.route('/run-steam',methods=['POST'])
def start_steam_back():
    print("starting steam")
    po.press('super')
    time.sleep(0.3)
    po.typewrite('steam')
    time.sleep(0.5)
    po.press('enter')  
    return "starting Steam"


@app.route('/open-homework',methods=['POST'])
def open_homework_back():
    print("opening homework")
    import pc_control
    from pc_control.main_cmds import homework
    homework()
    return "opening homework"


@app.route('/open-ict',methods=['POST'])
def open_ict_back():
    print("Opening Ict")
    import pc_control
    from pc_control.main_cmds import school_ict
    school_ict()
    return "revision"

@app.route('/open-revision',methods=['POST'])
def open_revision_back():
    print("opening revsion")
    import pc_control
    from pc_control.main_cmds import revision

    revision()
    return "started revision"
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=4000)




