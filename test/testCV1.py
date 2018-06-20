import numpy as np
import cv2
import imutils
from imutils.video import VideoStream
import time

print("[INFO] starting cameras...")
picamera = VideoStream(usePiCamera=True).start()
webcam = VideoStream(src=0).start()
time.sleep(2.0)

while(True):
    (ret1, frame1) = picamera.read()
    #(ret2, frame2) = webcam.read()
    
    frame1 = imutils.resize(frame1, width=500)
    #frame2 = imutils.resize(frame2, width=500)

    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('Picamera',gray)
    
    #cv2.imshow('Webcam',frame2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
picamera.release()
webcam.release()
cv2.destroyAllWindows()
