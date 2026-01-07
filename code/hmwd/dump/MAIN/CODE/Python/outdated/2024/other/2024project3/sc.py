print("sc.py")

import time
import getpass
from os import system, name
import database.users1 as users1
import database.adminpas as adminpas

AC = 0
global delay_time
global space_gap

import time

delay_time = 0.4
space_gap = " "

time.sleep(delay_time)

def delay():
    time.sleep(delay_time)

def space():
    print(space)

def spay():
    print(space_gap)
    time.sleep(delay_time)



users = users1.username
paw = users1.password
adpas = adminpas.adminpass



def security():
    global AC
    AC = 0
    rep = 0
    users = users1.username
    paw = users1.password
    pst=0


    while AC == 0 :

        rep = rep+1

        spay()

        admintest = input("Welcome to Ash, Press enter to login:")

        spay()

        user = input("Please enter your username:").lower()

        spay()

        if admintest == adpas:
            print("Admin acces granted")
            break
            
        elif admintest == adpas:
            print("Your password is hidden---")

            spay()
            passw = input("\rPlease enter your password:")

            spay()

        else:
            print("Your password is hidden---")
            
            passw = getpass.getpass("\rPlease enter your password:")

            spay()



        try:
            postion= users.index(user)

            int(postion)

            pst = postion

            print("Your ID is ",postion)

            spay()

        except:
            print("Name not found")

            spay()



        if user == users[pst] and passw == paw[pst]:
            print("Access granted")

            spay()

            AC = 1


        else:
            print("Access denied")

            spay()


            if rep > 4:
                print("Your locked out - restart the program")

                spay()

                exit()

#AC = 1
#access = 1
