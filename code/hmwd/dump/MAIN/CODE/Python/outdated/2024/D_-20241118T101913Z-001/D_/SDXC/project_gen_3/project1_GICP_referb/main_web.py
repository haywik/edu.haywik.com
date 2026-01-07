from flask import Flask,render_template,jsonify,request,abort,redirect
import subprocess,datetime
import pc_control.main_cmds
import pc_control.main_cmds
import pc_control.main_cmds
from datetime import *
import time,keyboard
import pyautogui as po
start_time = datetime.now()
app = Flask(__name__)
whitelist_ips = ['192.168.0.53','192.168.0.7','192.168.0.70','192.168.0.65','127.0.0.1','172.31.221.252']
def check_ip():
    client_ip = request.remote_addr
    if client_ip not in whitelist_ips:
        abort(403)

'''
@app.route('/',methods=['POST'])
def ():    
'''
@app.before_request
def sc_ip():
    check_ip()

@app.route('/')
def main_redirect():
    return redirect("/main")
@app.route('/main')
def index():
    return render_template('index.html')

@app.route('/smarthome')
def smarthome_back():
    
    return render_template('smarthome.html')

@app.route('/quick')
def quick_back():
    return render_template('quick.html')
@app.route('/get-uptime',methods=['GET'])
def get_uptime_back():
    up_time = datetime.now() - start_time
    up_time = str(up_time).split(".")[0]

    return jsonify({'up_time':up_time})






@app.route('/reboot-network',methods=['POST'])
def network_reboot_back():
    print("rebooting Network")
    import pc_control
    from pc_control.main_cmds import hub_reboot
    hub_reboot()
    return "hub rebooting"



@app.route('/machine-disconnect',methods=['POST'])
def machine_disconnect_back():
    print("PC disconnect")
    subprocess.run("netsh wlan disconnect",shell=True)
    return "PC dissconected",200

@app.route('/machine-signout',methods=['POST'])
def machine_signout_back():
    print("signing out machine") 
    subprocess.run("shutdown /l")
    return "signing out machine",200

@app.route('/machine-shutdown',methods=['POST'])
def machine_shutdown_back():
    print("Sever shutdown")
    subprocess.run('shutdown /f /s /t 10',shell=True)
    return "PC shutdown 10 seconds"


@app.route('/machine-lock',methods=['POST'])
def machine_lock_back():
    print("locking machine")
    subprocess.run('rundll32.exe user32.dll,LockWorkStation',shell=True)
    po.keyUp('winleft')
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
    subprocess.run('C:\\Users\\haywi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Eco.url',shell=True)
    return "starting Eco"

@app.route('/run-mc',methods=['POST'])
def start_mc_back():
    print("starting Minecraft")
    subprocess.run('C:\\XboxGames\\Minecraft Launcher\\Content\\Minecraft.exe',shell=True)
    return "starting mc"

@app.route('/run-roblox',methods=['POST'])
def start_roblox_back():
    print("starting roblox")

    subprocess.run('C:\\Users\\haywi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Roblox\\Roblox Player.lnk',shell=True)
    return "starting roblox"


@app.route('/run-forts',methods=['POST'])
def start_forts_back():
    subprocess.run('C:\\Users\\haywi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Forts.url',shell=True)
    return "starting forts"

@app.route('/run-steam',methods=['POST'])
def start_steam_back():
    print("starting steam")
    subprocess.run('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk',shell=True)
    return "starting Steam"

@app.route('/run-satisfactory',methods=['POST'])
def start_satisfactory_back():
    print("starting satisfactory")
    po.press('super')
    time.sleep(0.3)
    po.typewrite('satisfactory')
    time.sleep(0.5)
    po.press('enter')  
    return "starting satisfactory"

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
    return "Ict starting"

@app.route('/open-revision',methods=['POST'])
def open_revision_back():
    print("opening revsion")
    import pc_control
    from pc_control.main_cmds import revision

    revision()
    return "started revision"


@app.route('/run-whatsapp',methods=['POST'])
def run_whatsapp_back():
    print("starting whatsapp")
    subprocess.run('C:\\Users\\haywi\\Desktop\\WhatsApp.lnk',shell=True)
    return "starting whatsapp"

@app.route('/run-discord',methods=['POST'])
def run_discord_back():
    print("starting discord")
    subprocess.run('C:\\Users\\haywi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk',shell=True)
    return "starting discord"

@app.route('/run-chrome',methods=['POST'])
def run_chrome_back():
    print("starting chrome")
    subprocess.run('start chrome.exe',shell=True)  
    return "starting chrome"

@app.route('/run-vscode',methods=['POST'])
def run_vscode_back():
    print("starting vscode")
    subprocess.run('C:\\Users\\haywi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk',shell=True)
    return "starting vscode"



if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=4000)




