

from security import *

def login():
    x=0
    print("\nVerifcation Required")
    
    option = input("\n1.Login\n2.Create\n").lower()

    if option == "1" or option == "login":
        x=enter()
        if x != 1:
            print("Denied")
            login()
    else:
        create()
        login()

try:
    login()
except Exception as e:
    print("error in login",e)
    login()


from web import auth
