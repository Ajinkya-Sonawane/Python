import cv2

# Capture Video from Camera
cap = cv2.VideoCapture(0)   # Create object for video capture

#Define codec and VideoWriter Object
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc,30.0,(640,480))

while True:
    ret, frame = cap.read()     # Read frame by frame
    frame = cv2.flip(frame,1)   # flip the frame horizontally
    cv2.imshow('frame',frame)   # show the frame

    out.write(frame)            # Write the frame to output

    if cv2.waitKey(1) & 0xFF == ord('q'):   # 'q' is pressed stop
        break
cap.release()      # Release capture object
out.release()      # Release the writer object

# Display the recorded video

cap = cv2.VideoCapture('output.avi')

while True:
    ret, frame = cap.read()     # Read frame by frame

    if ret == True:
        cv2.imshow('frame',frame)   # show the frame

        if cv2.waitKey(1) & 0xFF == ord('q'):   # if user wants to stop he/she should press 'q'
            break
    else:
        break
