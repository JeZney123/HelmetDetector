from __future__ import print_function
from basicmotiondetector import BasicMotionDetector
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

#helmet_cascade = cv2.CascadeClassifier('LBPCascade_helmet.xml')
#motorcycle_cascade = cv2.CascadeClassifier('LBPcascade_motorcycle.xml')

print("[INFO] starting cameras...")
picam = VideoStream(usePiCamera=True).start()
webcam = VideoStream(src=0).start()
time.sleep(2.0)
piMotion = BasicMotionDetector()
camMotion = BasicMotionDetector()
total = 0

while True:
	frames = []

	#for stream in picam:
	frame = webcam.read()
	frame = imutils.resize(frame,width=400)
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		#locs = motion.update(gray)

	if total<32:
		frames.append(gray)
		continue

	frames.append(gray)

	total += 1
	timestamp = datetime.datetime.now()
	ts = timestamp.strftime("%A %d %B %Y %I:%M:%Sp")

	for (frame,name) in zip(frames,("Picamera")):
		cv2.putText(frame,ts,(10,frame.shape[0]-10),cv2.FONT_HERSHEY_SIMPLEX,0.35,(0,0,255),1)
		cv2.imshow(name,frame)

	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break

print("[INFO] Cleanning up...")
cv2.destroyAllWindows()
webcam.stop()
picam.stop()


