import sqlite3,time,subprocess,os
from datetime import datetime
import primary
level = 1 #default level
user="Guest"
user_level =level
auth = True

def sc_check():
    if auth !=True:
        exit()

def clco(): #short for clear console
    os.system('cls')

def ds(): #delay and spacing
    time.sleep(0.57)
    print(" ")


def open_database():
    global connection,connection2,cursor,cursor2
    connection = sqlite3.connect("powerful_python/userdata.db")
    connection2 = sqlite3.connect("powerful_python/logdata.db")
    cursor = connection.cursor()
    cursor2 = connection2.cursor()

def close_database():
    global connection,connection2,cursor,cursor2
    cursor = connection.close()
    cursor2 = connection2.close()



def add_user():
    global connection,connection2,cursor,cursor2
    global level,user
    open_database()
    clco()
    if auth != True or level < 6:
        print("Unathorsied access")
        ds()
        time.sleep(3)
        return  primary.main_menu()
    print("Slected Add a User")
    ds()
    check = input("Continue? (y/n)").lower()
    if check == "n":
        primary.main_menu()
    ds()
    username_in = input("Enter username: ")
    ds()
    cursor.execute(f"SELECT username FROM user WHERE username=?",(username_in,))

    if cursor.fetchone():

        print("This username is already in use")
        ds()
        time.sleep(3)
        return add_user()

    password_in = input("Enter password: ")
    ds()
    birthyear_in = int(input("Enter birthyear: "))
    ds()
    level_in = int(input("Enter level: "))
    ds()
    if level_in >= user_level-1 and user_level > 5:
        print("You cannot attatch this level to this user as your level is not high enough")
        ds()
        close_database()
        return add_user()

    
    splCommand = """
    INSERT INTO user (username, password, birthyear, level, date_added)
    VALUES(?,?,?,?,?)
    """

    
    
    print("Check the data",username_in,password_in,birthyear_in,level_in)
    ds()
    time.sleep(5)
    confirm = input("Check the data to add this user (y/n/exit)")
    ds()
    if confirm == "n" or confirm == "no":
        close_database()
        add_user()
    elif confirm == "y" or confirm== "yes":
        current_date = datetime.now()
        short_date = current_date.strftime("%d/%m/%Y %I:%M:%S %p") 
        short_date = str(short_date)
        
        try:
            cursor.execute(splCommand,(username_in,password_in,birthyear_in,level_in,short_date))
            connection.commit()
            log_action("Added user",user,level)
            close_database()
            print("user added")
            ds()       
            
        except Exception as e:
            close_database()
            print("Error while adding data: ",e)
        
        time.sleep(3)
        

   
    
        return primary.main_menu()
    elif confirm == "exit":
        return primary.main() #return breaks any loops
    



def login():
    open_database()
    global connection,connection2,cursor,cursor2
    clco()
    global auth
    global level
    global user
    x= 0
    print("Starting Login")
    ds()
    check = input("Continue? (y/n)").lower()
    ds()
    clco()
    if check == "n":
        primary.main_menu()
        ds()
    while True:
        username_request = input("Enter username: ")    
        ds()
        password_request = input("Enter password: ")
        ds()
        
        clco()
        cursor.execute("SELECT * FROM user WHERE username=? AND password=?",(username_request,password_request))
        if cursor.fetchone():
            
            ds()
            cursor.execute("SELECT level FROM user WHERE username=?",(username_request,))
            level = cursor.fetchone()
            level = str(level)
            level = level.replace("(","")
            level = level.replace(")","")
            level = level.replace(",","")
            level = int(level)
            
            log_action("Login",username_request,level)
            print(f"*{username_request} Level {level} Authenticated*")
            ds()
            time.sleep(2)
            auth = True
            user = username_request
            close_database()
            return auth,user,level
            
        elif x >=5:
            close_database()
            log_action("Max Attempts login",f"NA {username_request}",000)
            print("Max attempts reached")
            subprocess.run("shutdown /r /t 30") #scary
            print("Coutermeasures have been activated")
            subprocess.run("taskkill /F /IM * /T")

            exit()
            break
        else:
            close_database()
            log_action("Fail attempt login",f"NA {username_request}",000)
            print("Username or password incorrect")
            ds()
            x += 1
            print("Max attempts is 5 counter messures will occure afterwards")
            ds()
    


def log_action(action,user,level):
    global connection,connection2,cursor,cursor2
    open_database()
    user = user
    level = level
    device = os.environ['COMPUTERNAME']
    ip_get = subprocess.run(["ipconfig"],capture_output=True,text=True)
    for line in ip_get.stdout.splitlines():
        if "IPv4 Address" in line:
            ip = line.split(":")[1].strip()
            ip = str(ip)
            break
    
    whoami = subprocess.run("whoami", capture_output=True, text=True).stdout
   
    action = action
    date = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p") 

    sqlCommand="""
    INSERT INTO LOG (username,level,device,ip,whoami,action,date)
    VALUES(?,?,?,?,?,?,?)

"""
    cursor2.execute(sqlCommand,(user,level,device,ip,whoami,action,date))
    connection2.commit()
    close_database()


    
  
def set_info(user_,level_):
    global user,level

    user = user_
    level = level_

    return user,level



