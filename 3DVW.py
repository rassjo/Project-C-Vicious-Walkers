# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
import sys



#In this program, the grid is represented by a 0 array. 
#Elements in the matrix that correspond to particles will be replaced by a 1.
#Particles that occupy the same point will annihilate each other and be removed from the system.
#There's a 1 % chance that any time a particle tries to move, it decays and is removed from the system.


#List that holds the densities to be plotted later.
den=[]
denmatrix=[]
ave=[]
tlist=[]

#Generate grid (matrix) of size LxL. 
print('How large should the sides of the grid be?')
L=int(input())
lattice=np.zeros((L,L,L))
#Decide how many particles should be put into the grid
print('How many particles should the grid contain? (cannot exceed number of grid points)')
print('Total number of grid points: ', L**3)
Ntemp=int(input())
#Prevent program from running if too many particles are given
if Ntemp > L**3:
    print('Too many particles, please try again.')
    sys.exit()
#How many time steps the program will take
print('How many time steps should the program use?')
t=int(input())


C=10
for i in range(C):
    #Generate new empty grid each time the program is run
    lattice=np.zeros((L,L,L))
    N=Ntemp
    #Randomly place N particles in the grid
    n=N
    #Pick a random availabe grid positions and put a particle there until all particles are placed.
    while n !=0:
            #Find each matrix element that is zero.
            par1=np.where(lattice==0)[0]
            par2=np.where(lattice==0)[1]
            par3=np.where(lattice==0)[2]
            #Randomly pick a a point from among them
            val=random.randint(0, len(par1)-1)
            val1=par1[val]
            val2=par2[val]
            val3=par3[val]
            #Put a particle in the chosen spot
            lattice[val1,val2,val3]=1
            n=n-1
    #The particles move t times. If no particles are left, the loop ends early.
    T=1
    while T != t+1 and N>0:
            #Make an index array of nonzero points from which we pick a random element. The corresponding partice will then move one step
            #Nonzero creates a tuple of arrays. The first tuple element corresponds to the horizontal componet
            par1=np.nonzero(lattice)[0]
            #The second tuple element corresponds to the vertical componet
            par2=np.nonzero(lattice)[1]
            #The third tuple element corresponds to the forwards/backwards componet
            par3=np.nonzero(lattice)[2]
        
            #random.choice can only be used in 1D so we have to use a different method to pick a random particle.
            #Pick a random number between 0 and the tuple element size - 1
            valr=random.randint(0, len(par1)-1)
            #Use the random number to get the coordinates of a particle. That particle will be allowed to move a step
            val1=par1[valr]
            val2=par2[valr]
            val3=par3[valr]
            #Check if the random grid point contains a particle. If it does, make it move once or decay. Otherwise nothing happens and the loop continues 
            #Randomly pick which direction the particle moves
            valm=random.randint(1, 6)
            
            #The particle moves to the left
            if valm==1:
               #If the particle tries to move outside the grid, it remains at the same point as before
                if val1-1<0:
                    pass
                #If that grid point is occupied, the particles annihilate each other
                elif lattice[val1-1, val2, val3]==1:
                    lattice[val1, val2, val3]=0
                    lattice[val1-1, val2, val3]=0
                    #Total amount of particles decrease by 2.
                    N=N-2
                #If none of the above is true, the particle moves in the chosen direction
                else:
                    lattice[val1, val2, val3]=0
                    lattice[val1-1, val2, val3]=1
            #The particle moves to the right    
            elif valm==2:
                if val1+1>L-1:
                    pass
                elif lattice[val1+1, val2, val3]==1:
                    lattice[val1, val2, val3]=0
                    lattice[val1+1, val2, val3]=0
                    N=N-2
                else:
                    lattice[val1, val2, val3]=0
                    lattice[val1+1, val2, val3]=1
            #The particle moves down
            elif valm==3:
                if val2-1<0:
                    pass
                elif lattice[val1, val2-1, val3]==1:
                    lattice[val1, val2, val3]=0
                    lattice[val1, val2-1, val3]=0
                    N=N-2
                else:
                    lattice[val1, val2, val3]=0
                    lattice[val1, val2-1, val3]=1
            #The particle moves up
            elif valm==4:
                if val2+1>L-1:
                    pass
                elif lattice[val1, val2+1, val3]==1:
                    lattice[val1, val2, val3]=0
                    lattice[val1, val2+1, val3]=0
                    N=N-2
                else:
                    lattice[val1, val2, val3]=0
                    lattice[val1, val2+1, val3]=1
            #The particle moves backwards
            elif valm==5:
                if val3-1<0:
                    pass
                elif lattice[val1, val2, val3-1]==1:
                    lattice[val1, val2, val3]=0
                    lattice[val1, val2, val3-1]=0
                    N=N-2
                else:
                    lattice[val1, val2, val3]=0
                    lattice[val1, val2, val3-1]=1
            #The particle moves forwards
            else:
                if val3+1>L-1:
                    pass
                elif lattice[val1, val2, val3+1]==1:
                    lattice[val1, val2, val3]=0
                    lattice[val1, val2, val3+1]=0
                    N=N-2
                else:
                    lattice[val1, val2, val3]=0
                    lattice[val1, val2, val3+1]=1
        
            #Append values that we want to plot later
            den.append(N/L**3)
            #Average density of the system
            #Move to the next time step
            T=T+1
        
    #This part ensures that values are recorded for each time step, even if the previous loop terminates early.
    if N<=0:
        while T<=t:
            den.append(N/L**3)
            T=T+1
    #Append the denisty list in a new list and empty it afterwards
    denmatrix.append(den)
    den=[]

#Append thermodynamic limit in a list to plot later
for b in range(t):
    tlist.append(1/(b+1))

# Calculate and append the ensemble average of the densities in each time step
# Loop through each column
for j in range(t-1):
    sum=0
    #Sum the elements in the column and divide by the column length to get average density in each time step.
    for i in range(C):
        sum=sum + denmatrix[i][j]
        # print(j)
    ave.append(sum/C)
        
#Plot values
plt.figure
plt.plot(ave, 'r', label='Ensemble average particle density')
plt.plot(tlist, 'b', label='Thermodynamic limit, two dimensions')
plt.title('Vicious Walkers in Three Dimensions')
plt.xlabel('Time')
plt.ylabel('Particles per grid point')
plt.legend()
plt.show()