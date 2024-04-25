import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Define the range of n values from 3 to 50 (inclusive)
n_values = np.arange(3,51,1,dtype = int)

# Initialize empty arrays to store data for plotting
n_axis = np.array([])
k_axis = np.array([])
r_axis = np.array([])

# Loop over each value of n
for n in n_values:
  for k in range(1,n-1):   # Loop over each value of k from 1 to n-2
    a = 0  #without switching
    b = 0  #while switching
    for i in range(10000):
      arr = np.ones(n) #array of ones
      #selecting n-k random indicies
      indices = np.random.choice(n, size = n-k,replace = False)
      #assigning them to zero
      arr[indices]=0

      #so if arr[i] == 1 then it has car otherwise goat
      #fixing for door one always

      if arr[0] == 1:
        a = a+1
      dan = [i for i in indices if i!=0] #doors other than one in goats
      d = np.random.choice(dan)  #random door other than one
      can = [i for i in range(1, n) if i != d] #doors other than d and other than one
      e = np.random.choice(can) #random door other than one and d
      if arr[e] == 1:
        b = b+1
    n_axis = np.concatenate((n_axis,[n]))
    k_axis = np.concatenate((k_axis,[k]))
    r_axis = np.concatenate((r_axis,[b/a]))
    
      
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(n_axis, k_axis,r_axis, cmap='viridis')

plt.savefig('Monty.png')
ax1 = fig.add_subplot(111, projection='3d')
ax1.plot_trisurf(n_axis, k_axis,r_axis, cmap='viridis')
ax1.view_init(elev=0,azim=-90)


ax.set_xlabel('n')
ax.set_ylabel('k')
ax.set_zlabel('ratio')

ax.set_title('Surface Plot of n, k vs. P(win|W)/P(win|T)')

ax1 = fig.add_subplot(111, projection='3d')
ax1.plot_trisurf(n_axis, k_axis,r_axis, cmap='viridis')
ax1.view_init(elev=0,azim=-90)

plt.savefig('sideview.png')

plt.show()
