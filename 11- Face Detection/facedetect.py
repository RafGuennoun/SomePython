import cv2

# Download the haarcascade_frontalcatface.xml from this link
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml

# Cascade file that contains all what we need to detect faces
face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

def detect():

    # Setting the webcam of our pc
    cap = cv2.VideoCapture(0)

    while True:
        _,img = cap.read()

        # Setting the gray
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        # Face detected
        # face = face_cascade.detectMultiScale(gray, scale_factor, nb_faces )
        face = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Create a rectangle for faces
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 2)

        cv2.imshow("Face Detect", img)

        if cv2.waitKey(1)==27:
            break

    cap.release()

detect()