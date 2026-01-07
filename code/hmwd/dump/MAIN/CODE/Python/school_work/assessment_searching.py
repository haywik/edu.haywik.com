


maximum = int(input("Max:"))
number = int(input("Num:"))
minimum = 1
searches = 0

midpoint = (maximum+minimum)/2

print("mid",midpoint)

while number!=midpoint:
    
    if number < midpoint:
        maximum = midpoint - 1
    else:
        minimum = midpoint +1

    print(maximum,minimum,midpoint)

    searches = searches + 1

    midpoint = (maximum + minimum)/2

searches = searches +1

print("end::::",midpoint,searches)
