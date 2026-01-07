list = []

a = 0
b = 1
c = 0


limit = int(input("How many times would you like the program to run?:"))




for i in range(limit):

    c = a + b

    a = b

    b = c


    print(c)
