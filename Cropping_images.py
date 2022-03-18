# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:13:07 2022

@author: Gokhan Arman
"""

import cv2
import numpy as np
import os


path = "C:\\Users\\proje7.PROTON\\Desktop\\Python Projects\\Image Processing\\GOKHAN\Photos\\GaussianBlur.png" 
record_path = "C:\\Users\\proje7.PROTON\\Desktop\\Python Projects\\Image Processing\\GOKHAN\Photos\\"
img = cv2.imread(path)

cropped_img = img[100:400, 200:1400]

cv2.imshow("cropped", cropped_img)

# cv2.imwrite("Cropped_img_Detected_circles_in_the_frame.jpg", cropped_img)
cv2.imwrite(os.path.join(record_path , 'Cropped_img_GaussianBlur.jpg'), cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
