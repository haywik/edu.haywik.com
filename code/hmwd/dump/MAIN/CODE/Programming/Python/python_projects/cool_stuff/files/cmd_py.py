import subprocess,os


def cmd_run():
    os.system('cls')
    while True:
        user = input("\n\ncmd:>")

        if user == "end":
            break

        print("")
        subprocess.run(user,shell=True)