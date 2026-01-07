import time

global access

access = 0


def security():
    access = 0

    
    while access == 0:
        time.sleep(1)
    
        print("\nSecuity login required\n")

        time.sleep(1)
    
        print("\n\\\***********************************///\n")

        time.sleep(0.7)
    
        username = ["hay","harry","oscar"]

        password = ["1012","2010","1517"]

        ID=int(input("\nEnter User ID:"))
        
        user = input("\nEnter username:")

        passw = input("\nEnter password:")

        print("\nProcessing")

        time.sleep(0.8)

        IDcheck = len(username)

        if ID >= IDcheck or ID < 0:
            print("\nError - check user id is correct")
            security()
        
        if user == username[ID] and passw == password[ID]:
            print("\nAccess granted")
            access = 1
        
        else:
            print("\nAccess Denied")

  


print("\nD-7 ")

time.sleep(1.25)

Admin = input("\nPress Enter to begin:")

if Admin == "admin1":
    print("\nHello admin")

else:
    security()
