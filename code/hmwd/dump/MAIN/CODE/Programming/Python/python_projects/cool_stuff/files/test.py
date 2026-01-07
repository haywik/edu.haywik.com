x = 88
max = x/2
count=0

while count<max:
    count= count+1

    sqaure = count*count

    if sqaure == x:
        print("is square")
        break

    else:
        print(x,sqaure,count)

print("not square")