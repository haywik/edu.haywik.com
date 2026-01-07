print("work2.py  15/04/24")

import time

def work2_start():

    
    def DS():
        time.sleep(0.6)
        print(" ")




    def age_wider():
        

        year = int(input("Enter the year"))

        DS()

        mounth=int(input("Enter the mounth by number:"))

        DS()

        ybirth = int(input("Enter year of birth:"))

        DS()
        
        Mbirth = int(input("Enter mounth in numbers:"))

        DS()

        age = year - ybirth

        mouth = Mbirth - mounth

        if mouth < Mbirth:
            age = age - 1

        print("You are",age,"years old"," and mouths",mouth)


    
    input("Press enter to start Age wider:")
    age_wider()
