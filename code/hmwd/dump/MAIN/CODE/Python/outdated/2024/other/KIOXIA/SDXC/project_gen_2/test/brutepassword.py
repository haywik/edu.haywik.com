import pyautogui
from keyboard import is_pressed
from random import choice, randrange
from string import ascii_letters

# Infinite loop for typing random passwords until 'q' is pressed
while not is_pressed('q'):
    # Generate a random password of length between 1 and 8
    password_length = randrange(1, 9)
    password = ''.join(choice(ascii_letters) for _ in range(password_length))

    # Type the generated password as fast as possible with no typing delay
    pyautogui.typewrite(password, interval=0)  # Interval set to 0 for maximum speed
