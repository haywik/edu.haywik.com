print("main5.py")


#stucture:
'''
Imports -   external modules (time)
import files
Varbibles
Looks/smootharity 
module control - (Open/run)
user interface
security
Run user request
end

'''

#IMPORT - external modules
import time, os, getpass

#import modules and data
import databasefolder,workfolder


#VARIBLES
#Structure varibles
delay_time = 0.2
line_gap = " "

modules = ["Work1","Work2","Work3"]
global folder_path
folder_path='N:\coding\Python\2024\2024project5\workfolder'

#User varibles
access = False


#Looks and smootharity


#delay
def red():
    time.sleep(delay_time)

    
#line gap    
def gap():
    print(line_gap)

    
#line gap and delay    
def top():
    time.sleep(delay_time)
    print(line_gap)
    




def files_in_folder(folder_path):

 
    Files = os.listdir(folder_path)
    
    for i in Files:
        print(i)




def module_control_user():
    top()
    
    print("Slect a module to run:")
    
    top()
    
    print(database)
    
    top()
    
    module_selection = input("Enter the name of the module you would like to run ( cap senetive)")
    
    top()
    
    if module_selection in modules:
        print("Module found")
        
        
#module_control_user()

files_in_folder(folder_path)
