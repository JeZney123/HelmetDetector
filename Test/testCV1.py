import numpy as np
import cv2

picamera = cv2.VideoCapture(0)

while(True):
    ret1, frame1 = picamera.read()
    ret2, frame2 = webcam.read()
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('Picamera',gray)
    cv2.imshow('Webcam',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
picamera.release()
webcam.release()
cv2.destroyAllWindows()
