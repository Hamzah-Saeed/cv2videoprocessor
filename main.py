import numpy as numpy
import cv2 as cv 

capture = cv.VideoCapture(0)
if not capture.isOpened(): 
    print("Camera cannot be opened")
    exit()
while True: 
    ret, frame = capture.read() #is frame read and the actual frame.
    if not ret:
        print("The frame wasn't read.")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        print("escape key was pressed")
        break

capture.release()
cv.destroyAllWindows

