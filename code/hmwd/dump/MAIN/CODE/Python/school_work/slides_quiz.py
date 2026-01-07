from random import shuffle
import random


def not_math():
    q = [
        ("What colour is cheese","yellow","YELLOW"),
        ("What colour is grass","green"),
        ("What language is this","python")
        ]
    

    shuffle(q)


    for i in range(len(q)):
        ans = input(f"{q[i][0]}:")

        if ans in q[i]:
            print("Correct")
        else:
            print(f"Incorrect it was {q[i][1]}")










def math():
    respond =""
    while respond !="end":
        x = random.randint(10,100)
        y = random.randint(10,100)
        

        print(x)
        print("+")
        print(y)
        respond = int(input("Equals:"))
        answer = x+y
        if respond == answer:
            print("correct")

        else:
            print("incorrect  == ",answer)
            

choice = int(input("Math(1) or Normal(2):"))

if choice == 2:
    not_math()
elif choice == 1:
    math()
