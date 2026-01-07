import subprocess


print("Installing Python Packages")

subprocess.run('python -m pip install pyautogui',shell=True)

subprocess.run('python -m pip install psutil',shell=True)

subprocess.run('python -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib',shell=True)

subprocess.run('python -m pip install pip --upgrade',shell=True)



input("End")

