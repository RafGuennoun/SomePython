import cv2
import numpy as np
from PIL import ImageGrab

def screenrecord():
    # Create a video writer object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Output
    # out = cv2.VideoWriter("output.avi", fourcc, frames, (resolution))
    out = cv2.VideoWriter("output.avi", fourcc, 30.0, (1366, 768))

    while True:
        # Get the image
        img = ImageGrab.grab()

        # Convert the image to a numpy array
        img_np = np.array(img)

        # Convert the color contrast because we want the image in RGB format
        frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        # Create an output in which we can see the screen recorder
        cv2.imshow("Screen Recorder", frame)

        # Save the video
        out.write(frame)

        # if the user press the "Q" in the keyboard it will stop the program
        if cv2.waitKey(1) == 27:
            break

    out.release()

    # Destry the windows that we've created like Screen Recorder
    cv2.destroyAllWindows()


screenrecord()