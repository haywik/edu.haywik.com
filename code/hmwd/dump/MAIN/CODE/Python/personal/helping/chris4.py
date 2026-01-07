import time
import threading
import random
import os



# path should normally be C:\Users\Home\AppData\Local\Programs\Python\Python313\ filename
#                                                                                ^^^^^^^^
#test file should be 'pythontest' unless deleted    
#important btw 
linenum = 1
#bumboclat
def delete_file():
    global save_as
    delete = input("delete file? Y/N")
    try:
        delete = delete.upper()
        if delete == "Y":
            os.remove(save_as)
        elif delete == "N":
            print("Cancelling deletion")
    except TypeError:
        print("invalid answer,try again.")



       
       
def make_file():
    global filename
    #checks file name
    filename = input("What is new file name?(DO NOT PUT ANY .txt or .py IN!!)----> ")
    print("Please repeat to ensure no typos.")
    ensure = input("What is the new file name?(DO NOT PUT ANY .txt or .py IN!!)----> ")
    if filename == ensure:
        print("File name verified")
    else:
        print("Typo in one of the file names, please redo.")
        make_file()
        #checks if there is a .py or .txt
    if ".py" in filename or ".txt" in filename or "." in filename:
        print("NAUGHTY")
        make_file()
    filename = filename + ".py"
    try:
        if os.path.exists(filename) == True:
            print("ERROR, file already exists. Restarting")
            make_file()
        elif os.path.exists(filename) == False:
            print("File saved!")
            main_script()
           
    except Exception as e:
        print(e,": File already exists,Try again")
        make_file()




       
def edit_file():
    global filename
    #checks file name
    print("No need to enter the .py or .txt, I will do that if you don't! (by adding a .py)")
    filename = input("What is file name?----> ")
    print("Please repeat to ensure no typos.")
    ensure = input("What is the file name?----> ")
    if ".py" not in filename or ".txt" not in filename:
        filename = filename + ".py"
        if ".py" not in ensure or ".txt" not in ensure:
            ensure = ensure + ".py"
    if filename == ensure:
        print("No typos, proceeding")
        time.sleep(0.5)

        if os.path.exists(filename):
            time.sleep(0.5)
            print("File name verified")
            main_script()
        else:
            print("ERROR IN VERIFYING PATH")
            edit_file()
    else:
        print("Typo in one of the file names, please redo.")
        edit_file()
   



   
   
print("Five imported modules, time, threading,os ,pyautogui and random")
def decision():
    global choice
    #offers choice on files
    choice = input("press 1 for making a file, 2 for editing one, 3 for executing a pre-existing file and 4 for deleting a file ")
    if choice == "1":
        make_file()
        print("Preparing script")
       
    elif choice == "2":
        edit_file()
        print("Preparing script")
       
    elif choice == "3":
        #no point making a read_file function
        edit_file()
        print("Preparing script")
       
    elif choice == "4":
        delete_file()

    else:
        print("ERROR ON DECISION FUNCTION")
        decision()

       

def main_script():
    global filename,linenum,line,choice
    leave = False
    linenum = 0
    print("Remember, this will be just like writing in a normal py document.\n\ntype __exit__ twice to leave the program\n\n")
   
    if choice == "1":
        #creating new file
        print("removed for now")
               
    if choice == "2":
         #editing old file
        lines = []
       
        f = open(filename,"r")
        print(f.read())
        f.close()
       
       
        for line in open(filename, "r"):
            linenum += 1
       
        while True:
           
            linenum += 1
            with open(filename,"a") as file:
                line = input(f"line{linenum}: ")
                line = line + "\n"
               
                file.write(line)
            if "__exit__" in line:
               
                with open(filename,"r+") as file:
                    lines = file.readlines()
                    lines = lines[:-1]
                    file.seek(0)
                    file.writelines(lines)
                    file.truncate()



                   
                    print("Typing to file stopped, You can type anything now, type __exit__ again to quit or __start__ to start writing to file again\n")
                while True:
                    hastagline = input()
                    if "__start__" in hastagline:
                        print("Entering file writing mode again.\n")
                        break
                    elif "__exit__" in hastagline:
                        leave = True
                        print("leaving program")
                        break
            if leave:
                break
            else:
                continue
               
    if choice == "3":
        pass
    if choice == "4":
        delete_file()


