import numpy as numpy
import cv2 as cv

def filter_none(frame):
    return frame

def filter_grayscale(frame):
    return cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

def filter_canny(frame, low=80, high=160):
    return cv.Canny(frame, low, high)
