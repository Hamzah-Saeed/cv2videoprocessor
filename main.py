import numpy as np
import cv2 as cv 
import filters

capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
lastKey = 1


if not capture.isOpened(): 
    print("Camera cannot be opened")
    exit()
while True: 
    ret, frame = capture.read() #is frame read and the actual frame.
    if not ret:
        print("The frame wasn't read.")
        break

    #Checks for last keystroke to determine which filter to use. System is somewhat janky, might have to spam the key
    key = cv.waitKey(1) & 0xFF
    if key == ord('1'):
        lastKey = 1
    elif key == ord('2'):
        lastKey = 2
    elif key == ord('3'):
        lastKey = 3
    elif key == ord('4'):
        lastKey = 4
    elif key == ord('5'):
        lastKey = 5
    elif key == ord('q'):
        break

    if lastKey == 5: 
        customFrame = filters.filter_cartoon(frame)
    elif lastKey == 4: 
        customFrame = filters.filter_blur(frame)
    elif lastKey == 3:
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

