import cv2
import numpy as np
import imutils
from pyzbar.pyzbar import decode

lower_white = np.array([0,0,0], np.uint8)
upper_white = np.array([0,0,255], np.uint8)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
