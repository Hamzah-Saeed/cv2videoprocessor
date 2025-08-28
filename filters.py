import numpy as numpy
import cv2 as cv

def filter_none(frame):
    return frame

def filter_grayscale(frame):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

def filter_canny(frame, low=80, high=160):
    return cv.Canny(frame, low, high)

def filter_blur(frame):
    return cv.blur(frame, (20,20))

def filter_cartoon(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                 cv.THRESH_BINARY, 9, 9)
    color = cv.bilateralFilter(frame, 9, 300, 300)
    return cv.bitwise_and(color, color, mask=edges)