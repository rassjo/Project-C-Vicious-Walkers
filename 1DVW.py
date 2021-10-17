# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import sys

#List that holds the densities to be plotted later.
den=[]
denmatrix=[]
ave=[]
tlist=[]

#In this program, the grid is represented by a 0 array. 
#Elements in the matrix that correspond to particles will be replaced by a 1.
#Particles that occupy the same point will annihilate each other and be removed from the system.

#User determines grid size
print('How large should the grid be? ')
L=int(input())
#User determines how many particles should be put into the grid
print('How many particles should the grid contain? (cannot exceed number of grid points)')
Ntemp=int(input())
#Prevent program from running if too many particles are given
if Ntemp > L:
    print('Too many particles, please try again.')
    sys.exit()
else:
    pass
#User desides How many time steps the program will take
print('How many time steps should the program use?')
t=int(input())

#The simulation is run 10 times
C=10

for i in range(C):
    lattice=np.zeros(L)
    N=Ntemp
    #Randomly place N particles in the grid
    n=N
    while n !=0:
        #Pick a random availabe grid position and put a particle there.
        par=np.array(np.where(lattice==0))[0]
        val=random.choice(par)
        lattice[val]=1
        n=n-1

    #Run the simulation 10 times

    T=1
    #The particles move t times
    while T <= t and N>0:
            #Make an index array of nonzero points from which we pick a random element. The corresponding partice will then move one step
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
            #Move to the next time step
            T=T+1
            

    #If the grid is empty, this part fills the 
    if N<=0:
        while T<=t:
            den.append(N/L)
            T=T+1
    #Append the denisty list in a new list and empty it afterwards
    denmatrix.append(den)
    den=[]
    
#Append thermodynamic limit in a list to plot later
for b in range(t):
    tlist.append(1/np.sqrt(b+1))

#Calculate and append the ensemble average of the densities in each time step
#Loop through each column
for j in range(t):
    sum=0
    #Sum the elements in the column and divide by the column length to get average density in each time step.
    for i in range(C):
        sum=sum + denmatrix[i][j]
    ave.append(sum/C)
        
#Plot the recorded values
plt.figure
plt.plot(ave, 'r', label='Ensemble average particle density')
plt.plot(tlist, 'b', label='Thermodynamic limit, one dimension')
plt.title('Vicious Walkers in One Dimension')
plt.xlabel('Time')
plt.ylabel('Particles per grid point')
plt.legend()
plt.show()