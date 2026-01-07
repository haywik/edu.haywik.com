import time,random






def circle(grid):

    try:target = int(input("Circles: Enter your target (1-9)"))
    except:
        print("Invalid Input")
        circle(grid)

    if grid[target] == "[X]" or grid[target] == "[O]" or target > 9 or target < 0:
        print("Postion taken")
        circle(grid)
    else:    
        grid[target] = "[O]"

    return grid


def cross(grid):

    try:target = int(input("Crosses: Enter your target (1-9)"))
    except:
        print("Invalid Input")
        circle(grid)

    if grid[target] == "[X]" or grid[target] == "[O]" or target > 9 or target < 0:
        print("Postion taken")
        circle(grid)
    else:    
        grid[target] = "[X]"

    return grid





def check(grid):
    end = False
    for i in range(1,9):
        if grid[i] == "[X]" or grid[i] == "[O]":
            end = False
            break

    if end == True:
        print("Game end")
        start()

    return False
        

    
    



def game(player,grid):
    

    print(grid[1],grid[2],grid[3],"\n",grid[4],grid[5],grid[6],"\n",grid[7],grid[8],grid[9])


    if player == "circle":
        cross(grid)
    else:
        circle(grid)
        print("D else")
             
    if check(grid) == False:
        game(player,grid)




def start():
    grid = {1 : "[1]", 2 : "[2]", 3 : "[3]",4 : "[4]",5 : "[5]", 6 : "[6]", 7 : "[7]", 8 : "[8]", 9 : "[9]",}

    
    input("Assign yourself Cross Or Circle, Enter to continue\n")

    print("Here is the grid\n\n\n\n")

    time.sleep(1)
    
    print(" ",grid[1],grid[2],grid[3],"\n",grid[4],grid[5],grid[6],"\n",grid[7],grid[8],grid[9])


    input("Enter to start")

    
    if random.randint(1,2) == 1:
        player="circle"
    else:
        player="cross"

    game(player,grid)


    



start()
   
