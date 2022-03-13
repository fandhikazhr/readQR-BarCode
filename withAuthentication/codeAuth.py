import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('data.text') as f:
    myDataList = f.read().splitlines()
    
while True:
    success, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList:
            myOutput = 'Authorized'
            colorAuth = (80,255,0)
        else:
            myOutput = 'Un-Authorized'
            colorAuth = (0,0,255)
