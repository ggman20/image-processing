import cv2
from imutils.video import FPS
import numpy as np
import time

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = FPS().start()

while cam.isOpened():


    ret, frame = cam.read()
    cv2.imshow('frame', frame)

    fps.update()
    fps.stop()  # zamanlayıcıyı durdurun ve FPS bilgilerini görüntüleyin
    print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()