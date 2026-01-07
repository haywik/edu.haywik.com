import time, os, subprocess, threading, importlib
import __main__ as ma
import tkinter as tk
from tkinter import *

main = Tk()

main.geometry("1500x750")
main.resizable(False, False)
main.title("Primary Telemetry")

#header = Label(main, text = "Hi")

def exit_program(button):
    time.sleep(0.2)
    exit()


def satus1():

  pass













##########################

exit_button = Button(main, text="Exit", width=7, command=lambda: exit_program(exit_button))

exit_button.config(background="red", activebackground="Green")

exit_button.place(x=1437, y=720)

###############################


#main.mainloop()
