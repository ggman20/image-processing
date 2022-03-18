# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 15:52:22 2021

@author: proje7
"""

import cv2
import numpy as np

def callback(x):
    pass
def Resizing(img,scale_percent):
    
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_original = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    return img_original
img = cv2.imread("lama1.jpg")
scale_percent = 18

img = Resizing(img,scale_percent)



 
result = img.copy()
 
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
 
# lower boundary RED color range values; Hue (0 - 10)
lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])
 
# upper boundary RED color range values; Hue (160 - 180)
lower2 = np.array([160,100,20])
upper2 = np.array([179,255,255])

lower_gray = np.array([0, 0, 0])
upper_gray = np.array([255, 10, 255])
 
lower_mask = cv2.inRange(img, lower1, upper1)
upper_mask = cv2.inRange(img, lower2, upper2)

mask2 = cv2.inRange(img, lower_gray, upper_gray)
# Bitwise-AND mask and original image
res = cv2.bitwise_and(img, img, mask=mask2)
 
full_mask = lower_mask + upper_mask;
 
result = cv2.bitwise_and(result, result, mask=full_mask)
 
cv2.imshow('mask', full_mask)
cv2.imshow('result', result)
cv2.imshow('mask2', mask2)
cv2.imshow('res', res)
 
cv2.waitKey(0)
cv2.destroyAllWindows()



