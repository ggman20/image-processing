# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 16:06:12 2022

@author: Gokhan Arman
"""

import numpy as np
from PIL import Image
import numpy as np

V = []

M = []

for i in range(0,256):
    
    for j in range(0,256):
        
        V.append(j)
    
    V = np.array(V)
    M.append(V)
    
    V = []
    
M = np.array(M)

img = Image.fromarray(M)
img.save("homeworks_1_2.png")
img.show()

          

        

