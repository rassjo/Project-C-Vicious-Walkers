# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import sys

#List that holds the densities to be plotted later.
den=[]
ave=[]
tlist=[]

#In this program, the grid is represented by a 0 array. 
#Elements in the matrix that correspond to particles will be replaced by a 1.
#Particles that occupy the same point will annihilate each other and be removed from the system.
#There's a 1 % chance that any time a particle tries to move, it decays and is removed from the system.

print('How large should the grid be? ')
L=int(input())
lattice=np.zeros(L)
#Decide how many particles should be put into the grid
print('How many particles should the grid contain? (cannot exceed number of grid points)')
N=int(input())
#Prevent program from running if too many particles are given
if N > L:
    print('Too many particles, please try again.')
    sys.exit()
else:
    pass
#How many time steps the program will take
print('How many time steps should the program use?')
t=int(input())



#Randomly place N particles in the grid
n=N
while n !=0:
    #A random grid position is chosen. If the chosen point is availabe, a particle is placed there. Otherwise, nothing happens and the loop continues
    val=random.randint(1, L)-1
    if lattice[val]==0:
        lattice[val]=1
        n=n-1
    else:
        pass

#Make an index array of nonzero points from which we pick a random element. The corresponding partice will then move one step


#The particles move t times
T=1
sum=0
while T != t and N>0:
        par=np.array(np.nonzero(lattice))[0]
        #We pick a random particle that will be allowed to move one step.
        val=np.random.choice(par)
        #Randomly pick which direction the particle moves
        valm=random.randint(1, 2)
        #The particle moves to the left
        if valm==1:
            #If the particle tries to move outside the grid, it remains at the same point as before
            if val-1<0:
                pass
            elif lattice[val-1]==1:
                lattice[val]=0
                lattice[val-1]=0
                #Total amount of particles decrease by 2.
                N=N-2
            #If that grid point is occupied, the particles annihilate each other
            else:
                lattice[val]=0
                lattice[val-1]=1
            #The particle moves to the right    
        else:
            
            if val+1>L-1:
                pass
            
            elif lattice[val+1]==1:
                lattice[val]=0
                lattice[val+1]=0
                #Total amount of particles decrease by 2.
                N=N-2
               
            else:
                lattice[val]=0
                lattice[val+1]=1
        
        #Append values we want to plot later
        den.append(N/L)
        #Averege density of the system
        sum=sum+(N/L)
        ave.append(sum/T)
        #Move to the next time step
        
        tlist.append()
        T=T+1


#If the grid is empty, this part fills the 
if N==0:
    while T!=t:
        den.append(N/L)
        ave.append(sum/T)
        T=T+1
print('Number of remaining particles: ', N)

#Plot the recorded values
plt.figure
plt.plot(den, 'r', label='Particle density')
plt.plot(ave, 'g', label='Ensemble verage particle density')
plt.title('Vicious Walkers in One Dimension')
plt.xlabel('Time')
plt.ylabel('Particles per grid point')
plt.legend()
plt.show()