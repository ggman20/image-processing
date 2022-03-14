# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:14:03 2022

@author: RACK PC
"""



import cv2
from imutils.video import FPS
import numpy as np
import time

cam = cv2.VideoCapture(1, cv2.CAP_DSHOW)
width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = FPS().start()

Count = 1

while cam.isOpened():

    ret, frame = cam.read()
    ret, thresh = cv2.threshold(frame, 254, 255, cv2.THRESH_TOZERO)
    gray = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)  # framemizi griye dönüştürdük
    gray_blurred = cv2.GaussianBlur(gray, (17, 17), 0)
    
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 60, param1=200, param2=20, minRadius=60, maxRadius=100)
    
    if detected_circles is not None:
        detected_circles = np.round(detected_circles[0, :]).astype("int")
        for (x, y, r) in detected_circles:
            cv2.circle(gray_blurred, (x, y), r, (0, 0, 255), 2)  # çemberin dışı için
            cv2.circle(gray_blurred, (x, y), 1, (0, 0, 255), 2)  # çemberin merkezin için
        
        
    cv2.imshow('frame', frame)
    cv2.imshow('Threshold', thresh)
    cv2.imshow('GaussianBlur', gray_blurred)

    # fps.update()
    # fps.stop()  # zamanlayıcıyı durdurun ve FPS bilgilerini görüntüleyin
    # print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
    # print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
    
    # cv2.imwrite(path + str(Count) + '.jpg',frame)
    
    # Count = Count + 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
