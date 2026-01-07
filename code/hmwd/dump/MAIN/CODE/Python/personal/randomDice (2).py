import random as ra


while True:
    try:
        max = int(input("Enter dice max:"))
        roll = ra.randint(1,max)
        print("dice: ",roll)
    except:
        pass
