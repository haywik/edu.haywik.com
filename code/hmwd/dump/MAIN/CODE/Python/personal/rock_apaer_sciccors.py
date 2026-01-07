import random


while True:
    #do code

    #stop code #
    break




number = random.randint(1,10)

guess = int(input("Guess:"))

if guess == number:
    print("Correct")
else:
    print("Incorrect")
