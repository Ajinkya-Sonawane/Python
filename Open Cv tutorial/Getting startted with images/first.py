import cv2  #import cv2 (open-cv)

#read the image in 3 different modes
img_1 = cv2.imread("a.png",0)   #grayscale
img_2 = cv2.imread("a.png",1)   #color w/o transparency
img_3 = cv2.imread("a.png",-1)  #color with transparency

#create a window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

#display img_1 in the window
cv2.imshow('image',img_1)
cv2.waitKey(0)

#display img_2 in the window
cv2.imshow('image',img_2)
cv2.waitKey(0)

#display img_3 in the window
cv2.imshow('image',img_3)
cv2.waitKey(0)

cv2.destroyAllWindows()     #destroy all windows
