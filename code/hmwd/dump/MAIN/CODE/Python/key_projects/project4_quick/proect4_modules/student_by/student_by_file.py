import pygetwindow as gw
import pyautogui
import time
import pygetwindow
import ctypes
while True:
    try:
        def minimize_window():
            user32 = ctypes.windll.user32
            SW_MINIMIZE = 6
            hWnd = user32.GetForegroundWindow()
            user32.ShowWindow(hWnd, SW_MINIMIZE)


        # Find the window by title
        window = gw.getWindowsWithTitle('student.exe')[0]

        # Minimize the window
        window.minimize()
    except:
        time.sleep(1)
        print("No app")
