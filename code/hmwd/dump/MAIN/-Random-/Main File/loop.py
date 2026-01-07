i = 0
a = 0
import time

print("Hello")

input("Press enter to proceed")

username = input("Name?:")

userpass = input("Password?:")

password = "1234"

if username == "Hayden":
    print("Hello Hayden")
    if userpass == "1234":
        print("Welcome")
    else:
        print("Access denied")
else:
    print("Error")



input("Timer")
while True:
    time.sleep(1)
    a = a + 1
    print(a)
    
