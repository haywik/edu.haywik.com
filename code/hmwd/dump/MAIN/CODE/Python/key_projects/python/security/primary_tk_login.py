import subprocess, os, time, platform,threading,socket
import tkinter
from tkinter import *
can_run=1

def sc_login_run():
    global can_run
    global submit_cmd
    global user

    main = Tk()


    main.geometry("500x350")
    #main.attributes('-fullscreen',True)
    main.resizable(False,False)

    main.columnconfigure(0, weight=1)
    main.columnconfigure(1, weight=1)
    main.columnconfigure(2, weight=1)
    main.columnconfigure(3, weight=1)
    main.columnconfigure(4, weight=1)
    main.columnconfigure(5, weight=1)
    main.columnconfigure(6, weight=1)
    main.columnconfigure(7, weight=1)
    main.columnconfigure(8, weight=1)
    main.columnconfigure(9, weight=1)

    main.rowconfigure(0, weight=1)
    main.rowconfigure(1, weight=1)
    main.rowconfigure(2, weight=1)
    main.rowconfigure(3, weight=1)
    main.rowconfigure(4, weight=1)
    main.rowconfigure(5, weight=1)
    main.rowconfigure(6, weight=1)
    main.rowconfigure(7, weight=1)
    main.rowconfigure(8, weight=1)
    main.rowconfigure(9, weight=1)



    def login(arg):
        for widget in main.winfo_children():
            widget.destroy()
        global user
        global pas
        global ag
        global ad
        global user_new_c
        Label(main,text="Please Login Into Project BOB",font=10,bg="grey").grid(row=0,column=3,columnspan=4)
        Label(main,text="Username:",font=7).grid(row=3,column=3)
        Label(main,text="Password:",font=7).grid(row=4,column=3)
        ag = Label(text="Access Granted", font=15, bg="black")
        ag.grid(row=8, column=5)
        ad = Label(text="Access denied",font=15,bg="black")
        ad.grid(row=8,column=3)

        user_new_c = Button(main,text="New User",bg="pink",font=4,command=tk_new_user)
        user_new_c.grid(row=8,column=1)
        user = Entry(main,width=20,bg="white",font=("Impact",12))
        user.grid(row=3,column=4,columnspan=2)
        pas = Entry(main, width=20, bg="white",show="*", font=("Impact", 12))
        pas.grid(row=4, column=4, columnspan=2)

        submit = Button(main, text="Submit", bg="Green", font=4, command=submit_cmd)
        submit.grid(row=8, column=8)
        return submit


    def send_back_user():
        global user

        user_name = user.get()

        return user_name
    def submit_cmd():
        global permission

        from security import primary_login
        from security.primary_login import security_login

        u = user.get()
        p = pas.get()

        permission = security_login(u,p)
        if permission == "1":
            ag.config(bg="Green")
            ad.config(bg="Black")
            main.after(3000,main.destroy)

        else:
            ad.config(bg="red")
            ag.config(bg="black")

        return permission



    def new_user_cmd(us,pa,ad):
        global admin_input
        global login2
        global submit2
        from security import primary_login as primary_login

        from security.primary_login import security_create



        p = pas_new.get()

        u = user_new.get()

        a = admin_input.get()



        z = primary_login.security_create(u,p,a)

        if z == "1":
            admin_input.destroy()

            submit2.destroy()

            Label(text="User Created",font=20,bg="Green").grid(row=7,column=0,columnspan=9)
        elif z == "0":
            admin_input.destroy()
            login2.destroy()
            submit2.destroy()

            Label(text="Access Denied",font=10,bg="red",padx=10,pady=10).grid(row=7,column=0,columnspan=9)
        elif z=="2":

            Label(text="User Taken try again",font=10).grid(row=7,column=0,columnspan=9)
        elif z=="3":

            Label(text="Password is not 8 chacters long or is too simple",font=10,bg="yellow").grid(row=7,column=0,columnspan=9)

    def tk_new_user():
        for widget in main.winfo_children():
            widget.destroy()
        for widget in main.winfo_children():
            widget.destroy()
        global user_new
        global pas_new
        global admin_input
        global s
        global sd
        global e
        global login2
        global submit2
        Label(main, text="\/    Please Enter Details    \/", font=13, bg="grey").grid(row=0, column=3, columnspan=5)
        Label(main, text="-Pass and User will be lower cased-",font=8,bg="blue").grid(row=1,column=3,columnspan=4)
        Label(main, text="Username:", font=7).grid(row=3, column=3)
        Label(main, text="Password:", font=7).grid(row=4, column=3)
        Label(main,text="Administrator:",font=8).grid(row=5,column=3)
        #Label(main,text="Password must be 8 characters long",font=6,bg="purple").grid(row=7,column=1,columnspan=7)
        #s = Label(main,text="User Created",font=6,bg="black").grid(row=1,column=0)
        #sd = Label(main, text="Failed(Access)", font=6, bg="black").grid(row=1, column=0)
        #e = Label(main, text="Password Requirments", font=6, bg="black").grid(row=1, column=0)
        user_new = Entry(main, width=20, bg="white", font=("Impact", 12))
        user_new.grid(row=3, column=4, columnspan=4)
        pas_new = Entry(main, width=20, bg="white", font=("Impact", 12))
        pas_new.grid(row=4, column=4, columnspan=4)
        admin_input = Entry(main,width=20,bg="orange",show="*",font=("Impacts",13))
        admin_input.grid(row=5,column=4,columnspan=4)

        login2 = Button(main, text="Login", bg="pink",font=4, command=lambda : login(0))
        login2.grid(row=8,column=1)
        submit2 = Button(main, text="Submit", bg="Green", font=4,command=lambda :new_user_cmd(user_new,pas_new,admin_input))
        submit2.grid(row=8, column=8)



    login(1)


    main.config(bg="black")
    main.title("Login")


    main.mainloop()



