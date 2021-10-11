# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:43:57 2021

@author: rassj
"""
import numpy as np
import matplotlib.pyplot as plt
import random


#2D vicious walkers

n=int(input('How large should the sides of the grid be? '))
lattice2=np.zeros((n, n))
#Put particles in grid. Each point has a 30% chance of spawning a particle. 1 represents a grid point with a particle.
for i in range(n):
    for j in range(n):
        val=random.randint(1, 10)
        if val <= 3:
            lattice2[i, j]=1
#If an invalid input is given, the program wont run.
