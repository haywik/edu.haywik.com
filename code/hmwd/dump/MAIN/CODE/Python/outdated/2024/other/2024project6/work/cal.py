import time
import random
import os

a=1


def add(var):
    
    var = num1 + num2
    print(var)
    return var

def minus(var):
    var = num1 - num2
    return var

def multi(var):

    var = num1 * num2
    return var

def div(var):

    var = num1 / num2
    return var


def Calculator():

    global num1
    global symbol
    global num2
    global answer

    answer = 1


    
    print("\nCalculator \n")

    if a == 1:
    
        num1 = int(input("Number 1 :"))
        
        symbol = input("Symbol:").lower()
        
        num2 = int(input("Number 2 :"))

    
    
        if symbol == "+":
            add(answer)
            
            
        elif symbol == "-":
            answer = num1 - num2
            
            
        elif symbol == "/":
           
            answer = num1 / num2
            

        elif symbol == "x":
           
            answer = num1 * num2
            
            
        else:
         print("Error - symbol not recognised")


        print("\n", num1,symbol, num2, " = ", answer)


    else:
        print("Enter a correct symbol or enter a number")

        Calculator()



Calculator()
