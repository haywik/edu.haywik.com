import subprocess, os, time, platform,threading,socket
import tkinter
from tkinter import *
def run_main():
    subprocess.run(['python/main_menu.bat'],check=False)


main = Tk()
for widget in main.winfo_children():
    widget.destroy()
main.attributes('-fullscreen',True)
main.config(bg='black')
main.title("Student Details")

for i in range(10):
    main.rowconfigure(i,weight=1)
    main.columnconfigure(i, weight=1)

Label(main,text="Student Database",font=400,bg="white",width=40,height=1).grid(row=1,column=3,columnspan=5)

Label(main,text="Student tk \n by hw",font=5,fg="grey",bg="black").grid(row=9,column=9,rowspan=1,columnspan=1)

Button(main,text="Add Student",bg="green",font=20).grid(row=4,column=1,rowspan=1,columnspan=1)

Button(main,text="Edit Student",bg="yellow",font=20).grid(row=4,column=3,rowspan=1,columnspan=1)

Button(main,text="Delete Student",bg="red",font=20).grid(row=4,column=5,rowspan=1,columnspan=1)

Button(main,text="Search Student",bg="purple",font=20).grid(row=4,column=7,rowspan=1,columnspan=1)

Button(main,text="Main Menu",bg="grey",font=25,command=run_main).grid(row=4,column=9,rowspan=1,columnspan=1)

def add_student():
    class student:
        name = "unknown"
        surname = "unknown"
        dob = "unknown"
        gender = "unknown"
        address = "unkown"
    for widget in main.winfo_children():
        widget.destroy()


    student.address()
    Label(main,text="")


main.mainloop()