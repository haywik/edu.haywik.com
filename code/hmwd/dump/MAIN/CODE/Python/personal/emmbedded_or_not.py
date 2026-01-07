import random,time


embedded = ["micorwave","keyboard","fitness trackers","pacemakers","car brake system","AC","traffic light system","cctv","barcode scanner","auto doors","slowcooker","monitor","sound system","mri scanner","washing machine","simple house gagets"]

non_embedded = ["personal computer","laptop","chromebook","server","apple smart watch","iphone","rasberry pi"]

correct_count = 0
total_count = 0
while True:
    total_count = total_count+1
    random_list =random.randint(1,2)

    if random_list == 1:
        list_length = len(embedded) -1

        string = embedded[random.randint(0,list_length)]

        string = string.upper()
        
        user = input(f"\nIs a > {string} < Embedded? Y or N:").lower()

        if user == "y":
            correct_count = correct_count + 1
            print(f"\nYou are Correct {correct_count} out of {total_count}")
            
        elif user=="n":
            print(f"\nYou are Incorrect {correct_count} out of {total_count}")
        else:
            print("incorrect input answer")
            total_count = total_count -1

    elif random_list == 2:
        list_length = len(non_embedded) -1

        string = non_embedded[random.randint(0,list_length)]
        string = string.upper()
        user = input(f"\nIs a > {string} < Embedded? Y or N:").lower()

        if user == "n":
            correct_count = correct_count + 1
            print(f"\nYou are Correct {correct_count} out of {total_count}")
            
        elif user=="y":
            print(f"\nYou are Incorrect {correct_count} out of {total_count}")
        else:
            print("incorrect input answer")
            total_count = total_count -1
