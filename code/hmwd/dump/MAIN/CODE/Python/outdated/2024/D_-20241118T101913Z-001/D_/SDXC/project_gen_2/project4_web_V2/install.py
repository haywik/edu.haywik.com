import subprocess


print("Installing Python Packages")

subprocess.run('python -m pip install pip --upgrade',shell=True)

subprocess.run('python -m pip install pyautogui',shell=True)

subprocess.run('python -m pip install psutil',shell=True)

subprocess.run('python -m pip install flask',shell=True)

subprocess.run('python -m pip install PyP100',shell=True)

subprocess.run('python -m pip install keyboard',shell=True)

subprocess.run('python -m pip install jsonify',shell=True)

subprocess.run('python -m pip install PIL',shell=True)
input("End")

