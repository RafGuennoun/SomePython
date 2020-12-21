# This program takes pictures with your pc webcam

# Install the package opencv-python with the command
# pip install opencv-python

import cv2

# Setting te webcam of our pc
imgcapture = cv2.VideoCapture(0)

result = True

while(result):

    # Read the image
    ret, frame = imgcapture.read()

    # Save the image
    cv2.imwrite("test.jpg", frame)

    # Set result to false to stop the programm
    result = False

    print("Image Captured !!")

imgcapture.release()