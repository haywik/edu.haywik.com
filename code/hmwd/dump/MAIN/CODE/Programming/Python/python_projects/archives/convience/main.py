import tkinter as tk
import pyautogui as po

print("Starting convinces version 3")

#functions
def test():
    print("test")

def start_ui():
    ui_start = tk.Tk()
    ui_start.title("Hello")
    tk.Button(ui_start, text="Start",bg="GREEN",height=2,width=10 ,command=ui_start.destroy).pack()
    ui_start.mainloop()

start_ui()

def quit_all():
    
    quit()
#config

ui = tk.Tk()
ui.title("Interact")



#structure 10x10

for i in range(10):
    ui.rowconfigure(i, weight=1)
    ui.columnconfigure(i, weight=1)

#main area
    

tk.Button(ui, text="Quit",bg="GREY",height=2,width=10,command=quit_all).grid(row=10,column=10)

ui.mainloop()
