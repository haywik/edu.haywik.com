import os,time
from colorama import Fore, init
def clco(): #short for clear console
    os.system('cls')

def ds(): #delay and spacing
    time.sleep(0.4)
    print(" ")


def calc():
    clco()
    while True:
        expr = input("Enter the expression: ")
        print(eval(expr))
        ds()
        if expr == "exit":
            print("Exitiing calculator")
            ds()
            break



def calc2():
    clco()
    while True:
        try:
            num1 = input("Enter first number: ")
            ds()
            operator = input("Enter operator (+, -, *, /): ")
            ds()  
            num2 = input("Enter second number: ")
            ds()

            if operator =="exit" or num1 == "exit" or num2 == "exit":
                print("Exiting calculator")
                time.sleep(1)
                ds()
                break
            num1 = float(num1)
            num2 = float(num2)
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            
            else:
                print("Invalid operator")
                
            print(f"The result is: {result}")
        except:
            print("Error check your inputs. (dont divide by 0)")
        
        ds()

def calc_viewcode():
    clco()
    calc_code = '''
while True:

    expr = input("Enter the expression: ") # you dont need int() around the input, weridly enough, its eval() that does the math and bad stuff, dont use it its lazy    

    print(eval(expr)) #eval does the math as it evalulates


    if expr == "exit":
    
        print("Exitiing calculator") #if user wants to leave

        break  #leaves the while loop
    
        
    print(calc_code)    #prints results

    # use a bunch of if statemnets for each opertor to detmine what to do as in take 2 inputs
    # and an input of a operator. then do the math
'''
    print(calc_code)
    ds()
    input("Press enter to continue")


def calc_viewcode2():
    clco()
    calc_code2 = '''
    clco() #custom function for clearingt the console so it looks nice
    while True:
        try:
            num1 = input("Enter first number: ")
            ds()   #custom functions for delay and spacing
            operator = input("Enter operator (+, -, *, /): ")
            ds()  
            num2 = input("Enter second number: ")
            ds()

            if operator =="exit" or num1 == "exit" or num2 == "exit": #checks if user wants to leave
                print("Exiting calculator")
                break
            num1 = float(num1) #from string format to float (includes demcials)
            num2 = float(num2)
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            
            else:
                print("Invalid operator")
                
            print(f"The result is: {result}") # this is a f string u dont need it but its nice to know
        except:
            print("Error check your inputs. (dont divide by 0)")
        
        ds()
        

'''

    print(calc_code2)
    ds()
    input("Press enter to continue")



def calc_options():
    global user,level
    from security import log_action
    from primary import user,level
    log_action("Calc opened",user,level)
    clco()
    print(Fore.BLUE,"1. Lazy Calc")
    ds()
    print("2. View Code lazy")
    ds()
    print("3. Simple Calculator")
    ds()
    print("4. View Code simple")
    ds()
    print(Fore.RED,"0. Main Menu")
    ds()
    print(Fore.GREEN)
    option = input("Selection: ")
    ds()
    if option == "1":  #string for conistancy instead of int() takes too much time
        calc()
        calc_options()
    elif option == "2":
        calc_viewcode()
        calc_options()
    elif option == "3":
        calc2()
        calc_options()
    elif option == "4":
        calc_viewcode2()
        calc_options()
    elif option == "0":
        print("Returning to main menu")
        ds()
        from primary import main_menu
        main_menu()
    else:
        print("Invalid selection")
        calc_options()