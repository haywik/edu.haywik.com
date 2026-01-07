#code made by haywik, data is logged in local database only

#created on fri.2.jan.2025
# edited on sun.5.jan.2025 (late night)
#days programming 2

#notes
'''
code is not optimised , its a bit messy

'''





def install():
    import subprocess
    subprocess.run("python -m pip install colorama")
    subprocess.run("python -m pip install pandas")

import time,os,sqlite3,sys,pandas
from colorama import Fore, init


level = 1
init() # starts colorama
user= "Guest"
def clco(): #short for clear console
    os.system('clear')
    if os.name == 'nt':
        os.system('cls')
    
    
    

def ds(): #delay and spacing
    time.sleep(0.4)
    print(" ")


def open_database():
    global connection,connection2,cursor,cursor2
    connection = sqlite3.connect("powerful_python/userdata.db")
    connection2 = sqlite3.connect("powerful_python/logdata.db")
    cursor = connection.cursor()
    cursor2 = connection2.cursor()

def close_database():
    global connection,connection2,cursor,cursor2
    cursor = connection.close()
    cursor2 = connection2.close()


def welcome():
    clco()
    print(Fore.RESET)
    time.sleep(0.5)
    color = Fore.GREEN
    text1 = 'print("Hello World")'
    delay =0.6
    
    
    time.sleep(0.6)

    
    text2 = "Welcome to Powerful Python by haywik"
    
    for char in text2:
        print(Fore.RESET+char,end='',flush=True)
        time.sleep(0.255)
    clco()
    time.sleep(1.5)
    print(Fore.BLUE+":>",end='',flush=True)
    time.sleep(0.4)
   
    print(color + text1,end='',flush=True)
    
    time.sleep(2)
        
        
        
def main_menu():
    global connection,connection2,cursor,cursor2
    from security import level, user,auth
    level = level
    user = user
    auth = auth
    

    print("\n \n \n **Starting Powerful Python by haywik** \n \n \n")
    
    clco()

    print(Fore.WHITE,"*Main Menu*")
    print(f"[ {user} L{level} ]")
    print(Fore.GREEN)
    ds()
    if level < 2:
        print(Fore.RED,"1. Login")
    else:
        print(Fore.LIGHTBLACK_EX,"1. Login")
    ds()
    print(Fore.LIGHTBLACK_EX,"2. Add User")
    
    ds()
    print(Fore.BLUE,"3. Calculator")
    ds()





    print(Fore.GREEN)
    option = input("Selection:")
    ds()
    if option == "1" or option.lower() == "login":
        print("Selected Login")
        ds()
        from security import login
        login()
        from security import level, user,auth
        level = level
        user = user
        auth = auth


        
    elif option == "2" or option.lower() == "add user":
        print("Selected Add User")
        ds()
        from security import add_user
        add_user()



    elif option.lower() == "database manage":
        open_database()
        print("Selected manage database")
        ds()
        check = input("Continue? (y/n)").lower()
        ds()
        if check == "n":
            main_menu()
           

        from powerful_python.modules.database_manage import database_manage

        database_manage()
        
        
            #options to see someones data,remove,edit or whole database, so basicly typing in your own sql statements
        



    elif option == "3" or option.lower() == "calculator":
        if level < 3:
            print("Level 2 Needed")
            time.sleep(2)
            ds()
            main_menu()
        print("Selected Calculator")
        ds()
        from modules.calculator import calc_options
        calc_options()
    elif option.lower() == "logout":
        print("Logging Out")
        ds()
        from security import set_info
        set_info("Guest",1)
        main_menu()
    elif option.lower() == "exit":
        print("Custom Command Entered")
        ds()
        print("Exiting")
        ds()
        exit()
    
    else:
        print("Invalid Selection")
        ds()
        time.sleep(1)
        main_menu()      

    




if __name__ == "__main__":
    #install()
    #welcome()
    while True:
        try:
            main_menu()
        except Exception as e:
            try:
                close_database()
            except:
                print("could not close datbase")
            from security import log_action
            from security import user,level
            log_action("Fall Back Error",user,level)
            print("Fallback error (logged) restart program",e)
            input("press enter to restart")
            os.execv(sys.executable, ['python']+sys.argv)


