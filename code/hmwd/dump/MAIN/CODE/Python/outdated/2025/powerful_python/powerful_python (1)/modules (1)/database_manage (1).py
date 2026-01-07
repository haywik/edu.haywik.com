import time,os,sqlite3,sys,pandas
from colorama import Fore, init
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

def clco(): #short for clear console
    os.system('clear')
    if os.name == 'nt':
        os.system('cls')

def ds(): #delay and spacing
    time.sleep(0.4)
    print(" ")



#creation of databases
def user_data_database():

    connection = sqlite3.connect("powerful_python/userdata.db")
    cursor = connection.cursor()

    sqlCommand= """
    CREATE TABLE user
    (
        username TEXT,
        password TEXT,
        birthyear INTEGER,
        level INTEGER,
        date_added TEXT,
        primary key (username)
        
    )"""

    cursor.execute(sqlCommand)

    print("database created")

    connection.commit()

    connection.close()


def log_database():
    connection = sqlite3.connect("powerful_python/logdata.db")
    cursor = connection.cursor()

    sqlCommand = """

    CREATE TABLE log
    (       
        username TEXT,
        level INTEGER,
        device TEXT,
        ip TEXT,
        whoami TEXT,
        action TEXT,
        date TEXT,
        primary key (date)
    
    )"""

    cursor.execute(sqlCommand)

    print("log database created")

    connection.commit()

    connection.close()



def database_manage():
    global connection,connection2,cursor,cursor2
    
    from security import level
    if level > 9:
        
        print("Database manage.")
        ds()
        while True:
            open_database()
            database1 = pandas.read_sql_query("SELECT * FROM user",connection)
            database2 = pandas.read_sql_query("SELECT * FROM log",connection2)
            sql_cmd_base = input("Database 1 (userdata.db) or database 2 (logdata.db): ")
            sql_cmd = input("Manual SQL command: ")
            if sql_cmd_base =="exit" or sql_cmd =="exit":
                from primary import main_menu
                main_menu()

            if sql_cmd =="view all":
               
                print("data base 1 of userdata.db")
                
                print(database1)
                print("data base 2 of logdata.db")
                
                print(database2)
                ds()
                input("Press Enter to continue")
        
            
            else:
            
                try:
                    if sql_cmd_base == "1":
                        print("executing command",sql_cmd)
                        cursor.execute(sql_cmd)
                        connection.commit()
                    elif sql_cmd_base == "2":
                        print("executing command",sql_cmd)
                        cursor2.execute(sql_cmd)
                        connection2.commit()
                except Exception as e:
                    print("Could not execute",e)
                    time.sleep(5)
            close_database()
            clco()
    else:
        print("Access Denied")
        ds()
        close_database()
        clco()
        time.sleep(7)
        from primary import main_menu
        main_menu()

