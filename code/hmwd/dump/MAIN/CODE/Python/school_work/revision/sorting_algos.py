import random,time
num={}
num["unsorted"]=[70,30,50,10,22]
dorandom = 0

if dorandom == 1:
    for i in range(100):
        num["unsorted"].append(random.randint(1,100))

print("\nUnsorted\n",num["unsorted"],"\n\n\n\n")
    

def bubble():
    for i in range(len(num)-1):
        for ii in range(len(num)-1):
            now = num[ii]
            after = num[ii+1]
            if after < now:
                num[ii] = after
                num[ii+1] = now
    print(num)



def merge():
    length = len(num["unsorted"])
    mid_pointer = round_up(length/2)
    num["half_0"] = []
    num["half_1"] = []
    for number in num["unsorted"][0:mid_pointer]:
        num["half_0"].append(number)
    for number in num["unsorted"][mid_pointer:]:
        num["half_1"].append(number)

    print(num["half_0"])
    print(num["half_1"])





def round_up(insert):
    length = str(insert)
    decP = length.index(".")
    decimal = "0" + length[decP:]
    decimal = float(decimal)
    if decimal != "0": length = float(length) + (1 - decimal)
    return int(length)


def test():
    var={}
    var["t"] = [3,123,12,31,4,5]
    mid = 5
    mid = int(mid)
    
    for i in var["t"][2:mid]:
        num["t"] = num
#test()



merge()











