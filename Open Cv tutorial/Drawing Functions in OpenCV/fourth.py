import numpy as np
import cv2

# create a black image
img = np.zeros((512,512,3),np.uint8)

# Draw a line from left top corner to right bottom corner
img = cv2.line(img,(0,0),(511,511),(255,240,255),5)

# Draw a rectangle from (100,0) to (240,220)
img = cv2.rectangle(img,(100,0),(240,220),(0,255,0),3)
# to fill the rectangle pass -1 instead of 3

# Draw a circle with its center at (240,220) and radius 40
img = cv2.circle(img,(240,220),40,(0,0,255),5)
# to fill the circle pass -1 instead of 5

# Draw an ellipse
img = cv2.ellipse(img,(256,256),(100,50),0,0,180,255 ,5)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

# Display the image
cv2.imshow('image',img)

# Wait for key press
cv2.waitKey(0)
