import cv2
import numpy as np

helmet_cascade = cv2.CascadeClassifier('cascade.xml')

img = cv2.imread('137.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
helmet = helmet_cascade.detectMultiScale(gray,1.1,3)
print(helmet)

if helmet != ():
    print("Helmet")
    for (x,y,w,h) in helmet:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
else:
    print("Nothing")

    

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
