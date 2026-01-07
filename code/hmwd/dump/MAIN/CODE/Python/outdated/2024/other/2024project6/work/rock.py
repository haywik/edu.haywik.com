import random

def computer(var):

    a = random.randint(1,3)

    if a == 1:
        var = "rock"
    elif a == 2:
        var = "paper"
    elif a == 3:
        var = "scissors"
        
    


def game():

    print(" ") 
    print("Welomce to rock paper sicisors")
    gen = 1

    a = random.randint(1,3)
    print(" ") 
    if a == 1:
        var = "rock"
    elif a == 2:
        var = "paper"
    elif a == 3:
        var = "scissors"
    
    user = input("Rock , paper, scissors type").lower()
    print(" ") 
    print("Computer is ",var)
    print(" ") 
    if user == var:
        print("Draw")
    elif user == "rock" and var == "paper":
        print("You lose")
    elif user == "paper" and var == "scissors":
        print("You lose")
    elif user == "scissors" and var == "rock":
        print("You lose")
    else:
        print(" ") 
        print("You win")
        print(" ") 
        
while True:
    
    game()


