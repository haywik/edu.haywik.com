import subprocess, os, time, platform,threading,socket,random
import tkinter
from tkinter import *



def quiz_can_run():
    main = Tk()
    for widget in main.winfo_children():
        widget.destroy()


    main.attributes('-fullscreen',True)

    main.title("Quiz")

    main.config(bg="black")


    for i in range(10):
        main.columnconfigure(i,weight=1)
        main.rowconfigure(i,weight=1)


    Label(main,text="Welcome to Quizes ",font=2000,padx=40,pady=17,width=40,bg="white").grid(row=0,column=4)
    Label(main,text="\/ \/ Select Questioon type \/ \/",font=2000,bg="grey",width=1500,pady=20,padx=20).grid(row=2,column=0,columnspan=9)
    Label(main,text="quiz \n by hw",bg="black",fg="grey",padx=55,pady=25).grid(row=9,column=0)


    Button(main,text="Math Questions",bg="yellow",font=15).grid(row=3,column=2)
    Button(main,text="Both/Randomly generated",bg="Green",font=15).grid(row=3,column=4)
    Button(main,text="Non Math Questions",bg="orange",font=15).grid(row=3,column=6)

    main.mainloop()

