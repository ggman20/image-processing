import cv2
import time
from imutils.video import FPS

totalFrames = 0
fps = FPS().start()

# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
i = 0


while (cap.isOpened()):
    #time.sleep(1)
    ret, frame = cap.read()

    # This condition prevents from infinite looping
    # incase video ends.
    if ret == False:
        break
    totalFrames += 1
    fps.update()
    fps.stop()
    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite('Frame' + str(i) + '.jpg', frame)
    i += 1
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cap.release()
cv2.destroyAllWindows()