print("main.py")

import tkinter

#old school work files

import schoolwork.work1 as work1
import schoolwork.work2 as work2
import schoolwork.work3 as work3
import schoolwork.work4 as work4
import schoolwork.work5 as work5


import schoolwork2 as sch2

import sc



def gui():
    primary =tkinter.Tk()
    primary.geomtry("250x300")



    primary.mainloop()





#sc.security()

schoolfileOP = input("New (N) or old (O) school work folder?:").lower()

mod = int(input("\nEnter what work you would like to open as a number only:\n"))


if schoolfileOP == "O":
    
    if mod == 1:
        
        work1.work1_start()

    elif mod == 2 :
        work2.work2_start()

    elif mod == 3:
        work3.work3_start()

    elif mod == 4:
        work4.work4_start()

    elif mod == 5:
        work5.work5_start()
        
    else:
        print("Not found")


elif schoolfileOP == "N":

    pass

    
