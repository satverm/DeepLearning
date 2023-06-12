import  matplotlib
from matplotlib import pyplot as plt


print("print plots...")
X = [1, 2,3,4,5]
y = [10,20,30,40, 50]
#X, y = create_data(100,1)
print(X,"\ny:\n", y)
plt.scatter(X,y)
plt.show() # somehow pydroid not showing plot¿

#plt.scatter(X[:,0], X[:,1], c=y, cmap="brg")
#plt.show()
print("Plot done")