# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 15:17:02 2022

@author: Gokhan Arman
"""

import numpy as np
from PIL import Image
import math

V = []

M = []

for i in range(0,512):
    
    for j in range(0,512):        
        
        if math.sqrt(((i - 256) * (i - 256)) + ((j - 256) * (j - 256)) ) < 100:
            V.append(255)
        else:
            V.append(0)
            
    V = np.array(V)
    M.append(V)
    
    V = []
    
M = np.array(M)

img = Image.fromarray(M)
img.show()
            
            
        
        
    
    


