
import time



loop_amount = int(input("How many times shoudl the program run?"))



for loop in range(loop_amount):

    loop_out = loop + 1

    time.sleep(1)
   
    print(loop_out)
                  
    #print("\r",loop_out,end=" ",flush=True)
    
