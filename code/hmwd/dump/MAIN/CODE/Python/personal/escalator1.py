import subprocess

def run(cmd):
    completed = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command",cmd], capture_output=True)
    return completed


x = run("whoami")

print(x)
