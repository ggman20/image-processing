# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 17:17:58 2021

@author: proje7
"""

import argparse
import cv2
# construct the argument parser and parse the arguments
def Resizing(img,scale_percent):
    
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    img_original = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return img_original


# load the image, convert it to grayscale, and blur it slightly
image = cv2.imread("lama1.jpg")
scale_percent = 30

image = Resizing(image,scale_percent)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# show the original and blurred images


# compute a "wide", "mid-range", and "tight" threshold for the edges
# using the Canny edge detector
wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 100, 200)
contours, _ = cv2.findContours(mid,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print("Contours = " + str(len(contours)))
print(contours[0]) 


cv2.drawContours(image, contours, -1, (0, 0, 255), 2)
# show the output Canny edge maps
cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)