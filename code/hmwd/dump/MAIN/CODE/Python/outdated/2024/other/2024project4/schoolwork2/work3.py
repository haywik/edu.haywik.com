
import time

pocketMoney = 0.01

PMtotal = 0


for days in range(0,30):
    
    print("It is day ",days)

    time.sleep(0.2)

    print("You will get £ ",pocketMoney)

    time.sleep(0.2)


    PMtotal = PMtotal + pocketMoney

    pocketMoney = pocketMoney * 2


    print("you have a total of ",PMtotal)

