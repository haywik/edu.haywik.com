import random
x=1
number =random.randint(10,100)

key1= 12930231
key2 = random.randint(1000,key1)


encrypted2 = number * key2
print("ecrypted")

while True:
    x = random.randint(1,1000000)
    

    if encrypted2 / x == number:
        print("found",encrypted2 / x)
        break
    
