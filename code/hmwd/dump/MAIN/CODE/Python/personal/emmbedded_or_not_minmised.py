import random,time


embedded = ["micorwave","keyboard","fitness trackers","pacemakers","car brake system","AC","traffic light system","cctv","barcode scanner","auto doors","slowcooker","monitor","sound system","mri scanner","washing machine","simple house gagets"]
list_length1 = len(embedded) -1

non_embedded = ["personal computer","laptop","chromebook","server","apple smart watch","iphone","rasberry pi"]
list_length2 = len(non_embedded) -1

correct_count = 0
total_count = 0

def correct():
    global total_count,correct_count
    correct_count = correct_count + 1
    print(f"\nYou are Correct {correct_count} out of {total_count}")

def incorrect():
    global total_count,correct_count
    print(f"\nYou are Incorrect {correct_count} out of {total_count}")

def invalid():
    global total_count,correct_count
    print("incorrect input answer")
    total_count = total_count -1



while True:
    total_count = total_count+1
    random_list =random.randint(1,2)
    if random_list == 1:
        string = embedded[random.randint(0,list_length1)].upper()
        user = input(f"\nIs a > {string} < Embedded? Y or N:").lower()
        if user == "y":
            correct()
        elif user=="n":
            incorrect()
        else:
            print("incorrect input answer")
            total_count = total_count -1
    else:
        string = non_embedded[random.randint(0,list_length2)].upper()
        user = input(f"\nIs a > {string} < Embedded? Y or N:").lower()
        if user == "n":
            correct()
        elif user=="y":
            incorrect()
        else:
            invalid()
