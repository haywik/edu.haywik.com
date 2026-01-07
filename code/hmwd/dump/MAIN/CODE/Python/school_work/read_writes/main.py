import time
from data import *
opt = input("\n1.Login,2.New user").lower()





    
def login():
    global user,passw
    up=""
    u=""
    p=""
    u = input("\nEnter username:")
    try:
        up = user.index(u)
    except:
        print("\nInvalid Username")
        login()
        
    p = input("\nEnter password")

    if p == passw[up]:
        print("\nAccess Granted")
        menu()
    else:
        print("\nAccess Denied")
        login()


def create():
    global user,passw
    us=""
    pw=""
    admin = input("\nEnter admin password, for account creation")

    if admin=="123456":
        while True:
            us =input("\nEnter new username:")
            if us in user:
                print("\nUsername taken")
            else:
                pw=input("Enter password")

                user.append(us)
                passw.append(pw)

                f = open("data.py","w")

                f.write=(user)
                f.write=(passw)

                print("User created")
                menu()
                break
                
            

def menu():
    print("Main menu")

    time.sleep(10)


   

if opt == "1" or opt == "login":
    login()

elif opt=="2" or opt=="create":
    create()
