
highest = float('-inf')
lowest = float('inf')

totalWage = 0
MiddleUpper = 0

villians =["Joker","Magneto","Red Mist","Doc Ock"]

for counter in range(4):
    

    wages=[21,17,3,5]

    print(villians[counter],":£",wages[counter],"million")

    totalWage = totalWage + wages[counter]


    if highest < wages[counter]:
        highest = wages[counter]
        
    elif lowest > wages[counter]:
        lowest = wages[counter]




while True:
    for counter in range(4):
        
        if highest < wages[counter]:
            
            highest = wages[counter]
        
        elif lowest > wages[counter]:
            lowest = wages[counter]

        elif MiddleUpper < highest and MiddleUpper > lowest:
            MiddleUpper=wages[counter]
            break

        
        





print(wages,"is sorted")

print(totalWage,"Million is the total bill")
print("The highest is",highest)

print(MiddleUpper)
print("The lowest is",lowest)









