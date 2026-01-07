import random
print("welcome")

def rps():
    a = input("Rock,Paper or Scissors? ")
    choice = "null"
    ai_choice = random.randint(1,3)

    choice = a.lower()

    print(f" you chose {choice}!")

    if choice == "paper" or choice == 2:
        choice = 2
    elif choice == "rock" or choice == 1:
        choice = 1
    if choice == "scissors" or choice == 3:
        choice = 3



    #says ai's choice
    if ai_choice == 1:
        print("AI chose ROCK!")
    elif ai_choice == 2:
        print("AI chose PAPER!")
    if ai_choice == 3:
        print("AI chose SCISSORS!")

    
# rock = 1, paper = 2, scissors = 3
    print(f"you chose {a.upper()}")
    if choice == ai_choice:
        print("DRAW")
        
#you win conditions
    elif choice == 1 and ai_choice == 3:
        print("You win!")
    elif choice == 3 and ai_choice == 2:
        print("You win!")
    elif choice == 1 and ai_choice == 3:
        print("You win!")
#ai win conditions
    elif choice == 3 and ai_choice == 1:
        print("You lost to their rock!")
    elif choice == 2 and ai_choice == 3:
        print("You lost to their scissors!")
    elif choice == 1 and ai_choice == 2:
        print("You lost to their paper!")


def start():
    error = False
    choice = input("Play Rock,Paper,Scissors? Y/N ")
    if choice.isnumeric():
        error = True

    if error == False:
        choice = choice.upper()
        if choice == "YES" or choice == "Y":
            rps()
        elif choice == "NO" or choice == "N" or choice == "NOPE":
            print("Affirmative")
        else:
            print("ERROR")
            print("RESTARTING")
            start()
    else:
        print("ERROR")
        print("RESTARTING")
        start()

#start()


def rps_test():
    a = input("Rock,Paper or Scissors? ")
    choice = "null"
    ai_choice = random.randint(1,3)

    choice = a.lower()

    print(f" you chose {choice}!")

    if choice == "paper" or choice == 2:
        choice = 2
    elif choice == "rock" or choice == 1:
        choice = 1
    if choice == "scissors" or choice == 3:
        choice = 3



    #says ai's choice
    if ai_choice == 1:
        print("AI chose ROCK!")
    elif ai_choice == 2:
        print("AI chose PAPER!")
    if ai_choice == 3:
        print("AI chose SCISSORS!")

