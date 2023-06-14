# cteate a data set for use
#https://cs231n.github.io-neural-network-case-study/

import numpy as np
np.random.seed(0)

def create_data(points, classes):
	X = np.zeros((points * classes, 2))
	y = np.zeros((points)*classes, dtype='uint8')
	for class_number in range(classes):
		ix = range(points * class_number, points * ( class_number +1))
		r = np.linspace(0.0, 1, points) #radius
		t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
		X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
		y[ix] = class_number
	return X, y
	
import  matplotlib
from matplotlib import pyplot as plt # now it works

print("print plots...")
data_points = 2000
classes = 3
X, y = create_data(data_points,classes)
#print(X,"\ny:\n", y)
#plt.scatter(X[:, 0], X[:, 1])
#plt.show()
colors = np.random.randn(data_points)


plt.scatter(X[:,0], X[:,1], c=colors, cmap="rainbow") #different colors not showing 
plt.show()
print("Plot done")

		
	
	
	