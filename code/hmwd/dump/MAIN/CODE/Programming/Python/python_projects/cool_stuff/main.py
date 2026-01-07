import time,os

from files import data_organzise,cmd_py






files = [
    ("Data_organzise A ","Sort A1","Even Or Odd A2","Prime A3","Square A4","Calculator A5"),
    ("Useful B","Command Prompt  B1","Quick Buttons B2","Student Bypass_V1 B3")
]


while True:
    input("\n\n\nEnter for Main Menu::")

    os.system('cls')

    print("\n\n",files[0])

    print("\n",files[1])

    option = input("\nEnter:").lower()

    print("\n")

    if option == "exit":
        exit()
    elif option=="a":
        x = data_organzise.all()
        print("*Data*:",x)
    elif option == "a1":
        x = data_organzise.sort(0)
        print("*Data*:",x)
    elif option == "a2":
        x = data_organzise.even_odd(0)
        print("*Data*:",x)
    elif option == "a3":
        x = data_organzise.prime(0)
        print("*Data*:",x)
    elif option == "a4":
        x = data_organzise.square(0)
        print("*Data*:",x)
    elif option == "a5":
        x = data_organzise.calc(0)
        

    elif option == "b1":
        x = cmd_py.cmd_run()

