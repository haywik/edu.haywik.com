import random as r
import time as t
event = 0

odd =[]
even=[]

while True:
    
    event = event+1
    num = r.randint(1,10000000000)
    print(f"\n\n\n\n\nNumber: {num}")
    
    num2 = num/2  

    if num2 == int(num2):
        print("even",num)
        even.append(num)
    else:
        print("odd",num)
        odd.append(num)


    #optional
    
        
    print(f"\n\n\n\n")
    print("Odd",odd)
    print("even",even)

    t.sleep(1)
