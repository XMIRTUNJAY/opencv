import numpy
import cv2
cap=cv2.VideoCapture(0)
while  True:
	ret,frame=cap.read()
	cv2.imwrite('pic.jpg',frame)
	frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	print frame
	cv2.imshow('nishant_chirand',frame)
	if cv2.waitKey(30) & 0xff == ord('q'):
		break
		
cap.release()
cv2.destroyAllWindows()
