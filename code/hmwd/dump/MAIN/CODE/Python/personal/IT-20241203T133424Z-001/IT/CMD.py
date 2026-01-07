import subprocess

def command_prompt():
    print("starting command_prompt")
    print("Info: type exit to exit \n :  Type shell=True to enable subprocess wit shell use \nshell=False to turn off, \n Type config to config")
    config = input("type configs:").lower()
    while True:
        cin = input(":>")
        if cin == "config":
            config = input("type configs:").lower()
            cin = input(":>")
        if cin=="exit":
            exit()
        try:
            if config=="shell=false":
                args = cin.split()
                x = subprocess.run(args,capture_output=True,text=True)
                print(x.stdout)
                print(x.stderr)
            elif config=="shell=true":
                x = subprocess.run(cin,shell=True)
                print(x)
        except Exception as e:
            print("\nerror :")
            print(e)

command_prompt()
