import cv2,keyboard
pause = False
def flipper(x):
    if x == 1:
        x = 0
    else:
        x = 1

    return x

# Initialize the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)
freeze = 1
while True:
    if not pause:
        ret ,frame = cap.read()


        cv2.imshow('Webcam Feed', frame)


    if keyboard.is_pressed('q'):
        pause = True
    if keyboard.is_pressed('r'):
        pause = False
    cv2.waitKey(1)



cap.release()
cv2.destroyAllWindows()

