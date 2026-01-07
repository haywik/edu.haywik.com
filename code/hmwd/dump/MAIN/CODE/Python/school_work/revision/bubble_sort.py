import random,time

num=[5,4,3,2,1,0]
dorandom = 1

if dorandom == 1:
    for i in range(100):
        num.append(random.randint(1,100))

print("\nUnsorted\n",num)
    

def bubble():
    for i in range(len(num)-1):
        for ii in range(len(num)-1):
            now = num[ii]
            after = num[ii+1]
            if after < now:
                num[ii] = after
                num[ii+1] = now
    print(num)


    
        
