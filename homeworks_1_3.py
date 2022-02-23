# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 17:38:36 2022

@author: Gokhan Arman
"""
#%%Libraries
import cv2
import numpy as np
from pytictoc import TicToc
#%%Read Image
path = "road.jpg"
img = cv2.imread(path)
#%%Resized Image
width, height = 500, 500
imgResize = cv2.resize(img,(width, height))
gray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
#%% Manipulation
t = TicToc()
t.tic()
I = np.argwhere(gray)
for i in range(0,len(I)):     
    if gray[I[i,0], I[i,1]] % 10 == 1:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] - 1
    elif gray[I[i,0], I[i,1]] % 10 == 2:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] - 2
    elif gray[I[i,0], I[i,1]] % 10 == 3:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] - 3
    elif gray[I[i,0], I[i,1]] % 10 == 4:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] - 4
    elif gray[I[i,0], I[i,1]] % 10 == 5:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] + 5
    elif gray[I[i,0], I[i,1]] % 10 == 6:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] + 4
    elif gray[I[i,0], I[i,1]] % 10 == 7:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] + 3
    elif gray[I[i,0], I[i,1]] % 10 == 8:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] + 2
    elif gray[I[i,0], I[i,1]] % 10 == 9:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]] + 1
    else:
        gray[I[i,0], I[i,1]] = gray[I[i,0], I[i,1]]
t.toc()   
K = np.argwhere(imgResize <= 160)
for i in range(len(K)):
    imgResize[K[i,0], K[i,1]] = 150
#%%Show Image
cv2.imshow("road Gray", gray)
cv2.imshow("road Resized", imgResize)

cv2.waitKey(0)

