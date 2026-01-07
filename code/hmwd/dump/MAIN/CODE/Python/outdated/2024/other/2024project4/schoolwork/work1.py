pass
import time

print("work1 - 15/04/2024")


def work1_start():
    
    
   

    

    def DS():
        time.sleep(0.6)
        print("  ")

    def Bill_Splitter():
        DS()
        
        print("Bill splitter")

        DS()
        
        bill = int(input("Enter total bill:"))

        DS()
        
        people = int(input("Enter aomount of people:"))

        DS()
                     
        split_bill = bill / people

        print("Each person pays",split_bill)

    try:
        input("Press enter to start bill splitter:")
        Bill_Splitter()

    except:
        print("error")
        
