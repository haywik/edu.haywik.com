password = "hello"

attempts = 0

while True:
    guess = input("Enter Password")

    if guess == password:
        print("Correct")
        break
    else:
        attempts = attempts + 1


    if attempts >= 4:
        print("too many attemps")
        break
