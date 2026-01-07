from login import data
import time



def enter():
    delay = 0.5
    user = input("\nEnter username:")
    time.sleep(delay)
    pasw = input("\nEnter password:")
    time.sleep(delay)
    try:
        userpos = data.username.index(user)
    except Exception as e:
        print("\nInalid Username",e)
        enter()
        
    if pasw == data.password[userpos]:
        print("\nAccess Granted")
        time.sleep(delay*2)
        return 1
    else:
        print("\nAccess Denied")
        enter()

    
def create():
    delay = 0.5
    username = data.username.copy()
    password = data.password.copy()
    admin = input("Enter admin password:")
    if admin != "123456":
        print("Access Denied")
        create()
        
    user = input("\nEnter username:")
    while user in username:
        print("\nUsername taken")
        user = input("\nEnter username:")
    
    pasw = input("\nEnter password:")


    f = open("login/data.py","w")

    username.append(user)
    password.append(pasw)

   

    write = f"""username = {username}
password = {password}"""


    f.write(write)

    print("Account Created")

    time.sleep(delay*2)


