import subprocess   



cmd = subprocess.run("whoami", capture_output=True, text=True).stdout
#print(cmd.strip())