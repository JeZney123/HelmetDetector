from __future__ import print_function
from basicmotiondetector import BasicMotionDetector
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2



print("[INFO] starting cameras...")
webcam = VideoStream(src=0).start()
picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
firstFrame = None

while True:

    (ret, frame) = picam.read()
    frame = imutils.resize(frame, width=400)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if firstFrame is None:
        firstFrame = gray
        continue

    frameDelta = cv2.absdiff(firstFrame, gray)
    thresh = cv2.threshold(frameDelta, 40, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:

        if cv2.contourArea(c) < 5000:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #cap=webcam.read()[1]
        #cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f')+'.jpg',cap)

    cv2.imshow('PI Camera',frame)

    k = cv.waitKey(30) & 0xff
    if k == 27: #Ctrl+c
        break

picam.release()
cv2.destroyAllWindows()
