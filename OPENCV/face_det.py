import numpy as np
import  cv2
import math

face_cascade = cv2.CascadeClassifier("/home/mirtunjay/OpenCV/data/haarcascades/haarcascade_frontalface_smile.xml")

cap = cv2.VideoCapture(0)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
    		r=int(math.sqrt(((x-w)*(x-w))+((y-h)*(y-h)))/2)
        	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
     		print str(h)+","+str(w)+"\n"
    	cv2.imshow('img',img)
    	if cv2.waitKey(1) & 0xFF == ord('q'):
			break

cap.release()
cv2.destroyAllWindows()
