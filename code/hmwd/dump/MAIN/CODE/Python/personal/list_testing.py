import random
list1 = [10,23,44,22,11]
list1_extension_amount = 5000000


def find(num):
    list1_count=0
    global list1
    find = num
    if num in list1:
        print(f"\n \n{find} in list finding ID")
        list1_length = len(list1) - 1
        for i in range(list1_length+1):
            
            if list1[i] == find:
                print(f"\n{find} is {i} in list")
                
                list1_count = list1_count+1
    else:       
        print("not in list1")

    print(f"\n{find} occured {list1_count} times")
def list_extend():
    global list1,list1_extension_amount
    for i in range(list1_extension_amount):
        list1.append(random.randint(1,100))
    print(f"\nlist1 is {list1}")


list_extend()
find(10)
