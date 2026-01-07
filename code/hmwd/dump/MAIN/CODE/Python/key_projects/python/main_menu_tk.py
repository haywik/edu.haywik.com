import subprocess, os, time
import tkinter
from tkinter import *

def main_menu_run():


    from console_code_network import Primary_tk
    from console_code_network.Primary_tk import network_satus_run
    from security import primary_login
    from security.primary_login import security_login
    from security import login_details
    from security.login_details import login_log
    from security.login_details.login_log import logged
    from quiz import quiz_main
    from quiz.quiz_main_tk import quiz_can_run
    

    user_name = logged[-1]



    main = Tk()
    for widget in main.winfo_children():
        widget.destroy()

    main.attributes('-fullscreen',False)

    main.title(f"Main Menu {user_name}")

    main.config(bg="black")


    for i in range(10):
        main.columnconfigure(i,weight=1)
        main.rowconfigure(i, weight=1)


    Label(main,text="Main Menu \n by hw",font=1,bg="black",fg="grey",width=10).grid(row=9,column=9)


    Label(main,text=f"Welcome to project BOB, {user_name}:",font=200,bg="white",pady=5,padx=40).grid(row=0,column=4)

    def network_com():
        Label(main, text="Loading Module", font=10, bg="red").grid(row=8, column=4)
        print("loading module")

        main.destroy()
        network_satus_run()

    if user_name == "hayden":

        Button(main,text="Network Devices",font=15,bg="green",padx=45,command=network_com).grid(row=8,column=8)


    def local_host():
        from project4_web_V2 import main_web

        main_web.main_web_run()
        
    Button(main,text="Local Hosting",font=15,bg="green",padx=45,command=local_host).grid(row=2,column=2)    



    main.mainloop()


