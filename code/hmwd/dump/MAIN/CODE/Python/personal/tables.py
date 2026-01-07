import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

#varibles

cord_count = 100
cord_min = 1
cord_max = 20

x1 = []
y1 = []

x2 = []
y2 = []

#config



plt.ylim(cord_min,cord_max)
plt.xlim(cord_min,cord_max)

style.use("fivethirtyeight")

#functions

def r_cords(x,y):
    global cord_count,cord_max,cord_min
    

    for i in range(cord_count):
        x.append(random.randint(cord_min,cord_max))
        y.append(random.randint(cord_min,cord_max))


    return x,y


def sort(data):
    length = len(data)  #length of the data
    for i in range(length):
        for current in range(len(data)-1):
            if data[current] > data[current+1]:
                temp = data[current]
                data[current] = data[current+1]
                data[current+1] = temp
  
    return data



x1,y1 = r_cords(x1,y1)

an = animation(x1,y1)

plt.show()







