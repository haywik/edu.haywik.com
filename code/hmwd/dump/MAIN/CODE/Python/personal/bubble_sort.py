import random

data = []

data_count = 500
data_max = 400

for i in range(data_count):
    data.append(random.randint(0,data_max))


#data = [669,4,3,1,4,4,410,4333,90000,999999,4242342]

for xx in range(len(data)-1):
    
    for i in range(len(data)-1):


        if data[i] > data[i+1]:
            temp = data[i]
            data[i] = data[i+1]
            data[i+1] = temp


            #print("\n",data)



print(f"\n \n \n \n \n \n \n Final Sorted data: {data}")


    
