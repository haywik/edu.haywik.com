print("work 4       - 17/04/24")



def work4_start():


    goal = 20
    bal = 10.5

        
    print("You need",goal)

    print("You have",bal)

    extra = eval(input("Enter money you have as extra:"))

    total = bal + extra

    if total > goal:
        print("goal reached")
        print("You have",total)
    else:
        print("Not there")
        print("you have2",total)

        dif = goal - total

        print("You need this much more",dif)
