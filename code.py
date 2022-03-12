import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('example2.png') --> you can use example barcode picture
# code = decode(img)
# print(code)
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
