# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 10:55:53 2021

@author: rassj
"""

import numpy as np
import matplotlib.pyplot as plt
import random
#The amount of times the program will run.
t=100
#Number of particles in the grids
N=0
#Generate grid (matrix) of size n. 0 represents an empty space
n=int(input('How large should the grid be? '))
lattice=np.zeros(n)
for i in range(n):
    val=random.randint(1, 10)
    if val <= 3:
        lattice[i]=1
        N=N+1
#Check if particles have neighbors and eliminate them if so


print(lattice)
print(N)
print(N/n)