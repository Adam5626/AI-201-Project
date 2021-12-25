import cv2
import numpy

capture = cv2.VideoCapture(0)

while True:
    check, frame = capture.read()
    cv2.imshow('webcam', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

capture.release()
cv2.destroyAllWindows()
