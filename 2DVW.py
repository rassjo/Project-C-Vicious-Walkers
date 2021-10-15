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
tlist=[]

#Generate grid (matrix) of size LxL. 
print('How large should the sides of the grid be?')
L=int(input())
lattice=np.zeros((L,L))
#Decide how many particles should be put into the grid
print('How many particles should the grid contain? (cannot exceed number of grid points)')
print('Total number of grid points: ', L**2)
N=int(input())
#Prevent program from running if too many particles are given
if N > L**2:
    print('Too many particles, please try again.')
    sys.exit()
#How many time steps the program will take
print('How many time steps should the program use?')
t=int(input())

#Randomly place N particles in the grid
n=N
while n !=0:
    #A random grid position is chosen. If the chosen point is availabe, a particle is placed there. Otherwise, nothing happens and the loop continues
    val1=random.randint(0, L-1)
    val2=random.randint(0, L-1)
    if lattice[val1,val2]==0:
        lattice[val1,val2]=1
        n=n-1
    else:
        pass



#The particles move t times
T=1
while T != t:
    #Make an index array of nonzero points from which we pick a random element. The corresponding partice will then move one step
    #Nonzero creates a tuple of arrays. The first tuple element corresponds to the horizontal componet
    par1=np.nonzero(lattice)[0]
    #The second tuple element corresponds to the vertical componet
    par2=np.nonzero(lattice)[1]


    #random.choice can only be used in 1D so we have to use a different method to pick a random particle.
    #Pick a random number between 0 and the tuple element size - 1
    valr=random.randint(0, len(par1)-1)
    #Use the random number to get the coordinates of a particle. That particle will be allowed to move a step
    val1=par1[valr]
    val2=par2[valr]

    #Use RNG to determine if the particle will decay.
    die=random.randint(1,100)
    if N>0 and die==101:
        #Remove the particles from the system if it decays.
        lattice[val1,val2]=0
        N=N-1
    else:
        #Randomly pick which direction the particle moves
        valm=random.randint(1, 4)
        
        #The particle moves to the left
        if valm==1:
            #If the particle tries to move outside the grid, it remains at the same point as before
            if val1-1<0:
                pass
            #If that grid point is occupied, the particles annihilate each other
            elif lattice[val1-1, val2]==1:
                lattice[val1, val2]=0
                lattice[val1-1, val2]=0
                #Total amount of particles decrease by 2.
                N=N-2
            #If none of the above is true, the particle moves in the chosen direction
            else:
                lattice[val1, val2]=0
                lattice[val1-1, val2]=1
                
        #The particle moves to the right    
        elif valm==2:
            
            if val1+1>L-1:
                pass
            
            elif lattice[val1+1, val2]==1:
                lattice[val1, val2]=0
                lattice[val1+1, val2]=0
                
                N=N-2
            
            else:
                lattice[val1, val2]=0
                lattice[val1+1, val2]=1
                
        #The particle moves down
        elif valm==3:
            if val2-1<0:
                pass
             
            elif lattice[val1, val2-1]==1:
                    lattice[val1, val2]=0
                    lattice[val1, val2-1]=0
                    N=N-2
               
            else:
                lattice[val1, val2]=0
                lattice[val1, val2-1]=1
                
        #The particle moves up
        else:
            
            if val2+1>L-1:
                pass
                
            elif lattice[val1, val2+1]==1:
                lattice[val1, val2]=0
                lattice[val1, val2+1]=0
                N=N-2
               
            else:
                    lattice[val1, val2]=0
                    lattice[val1, val2+1]=1
                
    
    #Append values that we want to plot later
    den.append(N/L**2)
    #tlist.append(math.log(T)/T)
    #Move to the next time step
    T=T+1
        

print('Number of remaining particles: ', N)

#Plot values
plt.figure
plt.plot(den, 'r', label='Particle density in the grid')
#plt.plot(tlist, 'b', label='ln(t)/t')
plt.xlabel('Time')
plt.ylabel('Particles per grid point')
plt.legend()
plt.show()
