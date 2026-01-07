import os, random, time

password = "4321"

max_attempts = 0



def login():

    max_attemps = 1
    
    print("Login in terminal")

    while True:
        
        user_attempt = input("Enter the password")

        if user_attempt == password:
            print("Access granted")

            exit()

        elif max_attemps >= 3:
            print("Your locked out")

            quit()

        else:
            print("Access denied")

            max_attemps = max_attemps +1

        

        
        
login()
