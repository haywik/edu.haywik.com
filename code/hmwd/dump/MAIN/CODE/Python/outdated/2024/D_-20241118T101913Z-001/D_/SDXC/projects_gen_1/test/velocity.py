

while False:
    try:
        dis = eval(input("distance:"))
        time = eval(input("time"))
        v = dis/time
        v =round(v ,2)
        
        print(v)
    except:
        pass


while True:
    try:
        a = int(input("places:"))
        x = eval(input("::"))
        x = round(x,a)
        print(x)
    except:
        pass
