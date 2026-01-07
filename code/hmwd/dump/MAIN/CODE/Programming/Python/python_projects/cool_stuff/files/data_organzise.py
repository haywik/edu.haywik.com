import math,os

print("Starting Sortings and categorizations of data")    #ouputs a message to the user

#data = [4,1,5,3,5,1,2,3,555,12,3,4441,0,0,1,2,441,31231,3452341,1231,552134132,433421,12313]   #data of numbers


def make_data():
    os.system('cls')
    try:
        data = []
        user = input("Enter numbers:")
        if user == "exit":
            exit()
        user = user.split()
        for i in user:
            i = int(i)
            data.append(i)
    except:
        print("Invalid data")
        make_data()
    return data

def all():
    os.system('cls')
    data = make_data()

    sort1 = sort(data)
    even1= even_odd(data)
    prime1 = prime(data)
    sqaure1 = square(data)
    
    return sort1,even1,prime1,sqaure1
    
def sort(data):
    os.system('cls')
    if not data:
        data = make_data()
    length = len(data)  #length of the data
    for i in range(length):
        for current in range(len(data)-1):
         

            if data[current] > data[current+1]:
                temp = data[current]

                data[current] = data[current+1]

                data[current+1] = temp

    
    return "Sorted",data

def even_odd(data):
    os.system('cls')
    even = ["even"]
    odd=["odd"]

    if not data:

        data = make_data()

    print("Debug",data)

    for i in data:
        if i/2 == int(i/2):
            even.append(i)
        else:
            odd.append(i)
        

    return even,odd

def prime(data):
    os.system('cls')
    prime = ["prime"]
    not_prime = ["not prime"]

    if not data:

        data = make_data()
    for i in data:
        if i/2 != int(i/2) and i/3 != int(i/3) and i/5 != int(i/7):
            prime.append(i)
        else:
            not_prime.append(i)

    return prime,not_prime

def square(data):
    os.system('cls')
    square = ["sqaure"]
    not_square = ["not sqaure"]

    if not data:

        data = make_data()
    for i in data:
        if float(math.sqrt(i)) == int(math.sqrt(i)):
           
            square.append(i)
        else:
            not_square.append(i) 

    return square,not_square


def calc(data):
    os.system('cls')
    print("Type end to exit calc")

    while True:
        num = input("\n\nEnter Caclulation: ")

        if num == "end":
            break

        num = eval(num)

        print("ANS:",num)