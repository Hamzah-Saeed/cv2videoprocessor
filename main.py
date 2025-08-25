import numpy as np
import cv2 as cv 
import filters

capture = cv.VideoCapture(0)
lastKey = 1
if not capture.isOpened(): 
    print("Camera cannot be opened")
    exit()
while True: 
    ret, frame = capture.read() #is frame read and the actual frame.
    if not ret:
        print("The frame wasn't read.")
        break

    #Checks for last keystroke to determine which filter to use. System is somewhat janky, might have to spam the key, could be refined
    if cv.waitKey(1) == ord('3'):
        lastKey = 3
    elif cv.waitKey(1) == ord('2'):
        lastKey = 2
    elif cv.waitKey(1) == ord('1'):
        lastKey = 1
    if lastKey == 3:
        customFrame = filters.filter_canny(frame)
    elif lastKey == 2:
        customFrame = filters.filter_grayscale(frame)
    else:
        customFrame = filters.filter_none(frame)

    cv.imshow('frame', customFrame)
    if cv.waitKey(1) == ord('q'):
        print("escape key was pressed")
        break

capture.release()
cv.destroyAllWindows()

