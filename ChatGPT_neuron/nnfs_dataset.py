#nnfs datasets
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X, y = spiral_data(1000,3)
print(X)
print(y)

import  matplotlib
from matplotlib import pyplot as plt


print("print plots...")
print(X,"\ny:\n", y)
plt.scatter(X[:,0], X[:,1])
plt.show() # somehow pydroid not showing plot¿

plt.scatter(X[:,0], X[:,1], c=y, cmap='brg')
plt.show()
print("Plot done")