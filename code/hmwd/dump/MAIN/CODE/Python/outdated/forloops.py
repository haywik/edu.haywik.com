import math


sum = 0
sum2 = 0
sum3 = 0
sum4 = 0
highest = float('-inf')
lowest = float('inf')
high=0
count=0

for i in [5, 4, 3, 2, 1, ]:

    count = count+1
    
    print(i)
   
    sum = sum + i

    if i > highest:
        highest = i

    if i < lowest:
        lowest = i


    


     
    
print("Aveage:",sum/count)
print("sum",sum)
print("Highest number",highest)
print("Lowest number",lowest)


print("End")



