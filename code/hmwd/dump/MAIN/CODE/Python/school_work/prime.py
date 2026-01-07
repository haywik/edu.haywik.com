num,l=0,0
prime = []
nprime=[]

while True:

    num = num + 1
    l = l + 1
    

    if (num/2 == int(num/2) or num/3 == int(num/3) or num/5 == int(num/5) or num/7 == int(num/7) or num**0.5 == int(num**0.5)) and (num not in [2,3,5,7]):
        #print("\n\n")
        nprime.append(num)
        #print("not prime",num)
       
    else:
        #print("\n\n")
        prime.append(num)
        #print("prime",num)
       
    if l > 100:
        print(prime)
        print(nprime)S
        l=0
 
