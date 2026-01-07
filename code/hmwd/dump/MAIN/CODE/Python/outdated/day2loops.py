count = 0
a = 0
m50 = ""
#a = int(input("What number do you want to check for"))



for i in [23,45,17,2,65,54,29,71,50,99,3,57]:
    print("\nDouble of i is" ,i*2)    

    if a == i:
        print("\n",a,"is in the array")
    elif i > 50:
        i = str(i)
        m50 = m50 + "," + i
    elif i < 50:
        count = count+1
        
    elif i == 50:
        count=count+1



       
print("\nNumber less than 50 or 50:",count)
print("\nnumbers that are more than 50:",m50)




