import time
import random
### the Cuben#


##varibles and lists

random = 0

Options = ['Calculator (1)\n',
           "Number Guess (2)",
           "Bmi Calculator(3)",
           "Gcse pass/fail(4)",
           "Number Teller(5)",
           "Sprinkler (6)",
           "BMI x10(7)",
           "Timer(8)",]

name = ["Hayden","Harry","Jason","Oscar"]
           

total_uses_bmi = 0
## libary of options
def stopwatch():
    print("Timer \n")
    
    a = int(input("Enter how long:"))
    for i in range(a):
        #a = a - 1
        print(i)
        
    
        time.sleep(1)
    print("Timer  Ended")    


def highest_number():
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    num10 = 0
    while count != 10:
        print("Highest Number out of 10")
         




    

def bmi_x10():
    responses = 0
    global total_uses_bmi
    heavy_bmi = 0
    normal_bmi = 0
    light_bmi = 0
    while total_uses_bmi !=10:
        
        print("\nBmi Calculator")
        weight = int(input("(KG) Weight:"))
        height = int(input("(M) Height:"))
        print("")
       
        total_uses_bmi = total_uses_bmi + 1
        
        height_2 = height * height
        total = weight / height_2
        
        print("Your bmi is",total,)
        
        if total < 18:
            print("Your underweight")
            light_bmi = light_bmi +1
            
        elif total > 18 and total < 23:
            print("Your ok")
            normal_bmi = normal_bmi +1
        elif total > 24:
            print("Your overweight")
            heavy_bmi = heavy_bmi+1
        else:
            print("Error")
        print("Uses:",total_uses_bmi,"/10")
        
        time.sleep(1)
    print("\nOverweight patience",heavy_bmi,"\n Normal patience",normal_bmi,"\n Underweight patience",light_bmi,)    
    print("\n\n *BMI x10 Finished*")
    time.sleep(2.9)
        




def number_teller():
    number = 0
    while number != 12345:
        number = int(input("Enter a number"))

        if number > 0:
            print("Number is positive")
        elif number < 0:
            print("Number is negative")
        elif number == 0:
            print("Number is 0")
        else:
            print("Invaild number")

    print("Program ended")

            

    


def gcse():
    print("GCSE pass/fail")
    score1 = int(input("Enter Score1:"))
    score2 = int(input("Enter Score2:"))
    score3 = score1 + score2
    score4 = score3 / 2
    if score4 > 70:
        print("Merit")
    elif score4 > 40 and score4 < 70:
        print("Pass")
    else:
        print("Fail")


def sprinkler():
    temp = eval(input("enter tempreature"))
    moisture = eval(input("enter soil moisture"))

    if temp > 30 and moisture < 20:
        print("Turn on sprinkler")
    else:
        print ("Turn off sprinkler")


def Calculator():
    print("\nCalculator \n")
    num1 = int(input("Number 1 :"))
    symbol = input("Symbol:")
    num2 = int(input("Number 2 :"))
    if symbol == "+":
        answer = num1 + num2
        print("\n", num1, " + ", num2, " = ", answer, )
    elif symbol == "-":
        answer = num1 - num2
        print("\n", num1, " - ", num2, " = ", answer, )
    elif symbol == "/":
       
        answer = num1 / num2
        print("\n", num1, " / ", num2, " = ", answer, )

    elif symbol == "x" or "X":
       
        answer = num1 * num2
        print("\n", num1, " x ", num2, " = ", answer, )
    else:
     print("Error")



def Random_Guesser():
    print("UNAVILBLE")
    time.sleep(1)
    print("Guess the numer")
    print("From 1-100")
    
    a = random.randint(1,100)
    guess = -1

    while guess != a:
        c = input("Enter Guess:")
        if guess != a:
            print("Try again")
            if c > a:
                print("Lower")
            elif c < a:
                print("Heigher")
    print("Well done")
        
                
                        
        



    
def bmi_cal():
    global total_uses_bmi
    print("\nBmi Calculator")
    weight = int(input("(KG) Weight:"))
    height = int(input("(M) Height:"))
   
    total_uses_bmi = total_uses_bmi + 1
    
    height_2 = height * height
    total = weight / height_2
    
    print("Your bmi is",total,)
    
    if total < 18:
        print("Your underweight")
    elif total > 18 and total < 23:
        print("Your ok")
    elif total > 24:
        print("Your overweight")
    else:
        print("Error")
    print("Uses:",total_uses_bmi,)
    
    time.sleep(2.3)
   







### Options
def user_options():
    i = 1
    while i == 1:
        time.sleep(1)
        print("\nWhat would you like to do? \n")
        print(Options)
        user_op = int(input(":"))
        if user_op == 1:
            Calculator()
        elif user_op == 2:
            Random_Guesser()
        elif user_op == 3:
            bmi_cal()
        elif user_op == 4:
            gcse()
        elif user_op == 5:
            number_teller()
        elif user_op == 6:
            sprinkler()
        elif user_op == 7:
            bmi_x10()
        elif user_op == 8:
            stopwatch()


##verification  
   

def user_verification_1():
    num = 0
    unknow_user_verfi = 0
    while unknow_user_verfi != 1234:
        unknow_user_verfi = input("\nEnter Pin:")
        print(" ")
       
        unknow_user_verfi = int(unknow_user_verfi)
       
        if unknow_user_verfi == 1234:
           
            time.sleep(1)
           
            print("\n**Access Granted** \n")

        elif num > 5:
            print("Access denied, Program terminated")
            exit()
        elif unknow_user_verfi != 1234:
            print("Access denied try again")
            num = num+1
           
        else:
            print("Error")
            


## primary user interartuion

print("Welcome to the Cuben \n")
time.sleep(1)
user_name = input("Enter your name:")

if user_name == "hayden":
    user_options()

print("\nHello ", user_name)
time.sleep(1)
# @@ Verification
user_verification_1()

# @@ Options
user_options()
# @
