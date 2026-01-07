
def f020():
    first = input("First Name:")
    #last = input("Last Name:")
    print(f"Your name is {len(first)} chacters long")


def f021():
    first = input("First Name:")
    last = input("Last Name:")

    print(f"{first} {last} is {len(first)+len(last)} chacters long")

def f022():
    first = input("First Name:").lower()
    last = input("Last Name:").lower()
    print(first.title(),last.upper())

def f023():
    r = input("Line of rhyme:")

    print(len(r)," Chacters")
    
    

    start = int(input("starting number:"))-1
    end = int(input("Ending number:"))-1


    print(r[start:end])


def f025():
    first = input("First Name:").lower()

    if len(first) < 5:
        
    
        last = input("Last Name:").upper()

        print(first.upper()+last)
    else:
        print(first)


def f026():
    vow = ["a","e","i","o","u"]
    word = input("Enter word:")

    if word[0:1] in vow:
        word = word+"way"

    else:    
        for i in word:
            if i not in vow:
                word = word.replace(i,"")
                word = word + i + "ay"
                break

    print(word)

    


f023()



    
    
