heroes =["Batman","WonderWoman","Superman","Spiderman"]


print("Current Pilot:",heroes[0])


print("Current Co-Pilot:",heroes[1])


heroes[2]=("HitGirl")


print("Superman has allergy flare:",heroes[2],"is replacing him")


heroes.append("IronMan")


heroes.append("Thor")


print(heroes)


new = int(input("Which hero would you like to replace? - as a number:"))

print(heroes)
 new = new-1

newhero = input("Enter the name:")

heroes[new] = newhero

print(heroes)
