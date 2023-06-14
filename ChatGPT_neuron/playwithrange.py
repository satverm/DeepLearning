#testing some np functions
# creating ranges to use in lists , matrix
import numpy as np
pt =10
cl = 3
print(f"The points are {pt} and classes are {cl}")
def cr(p,c):
	rg = range(p*c, p * (c+1))
	return rg
for i in range(0,cl):
	ix = cr(pt*i, pt*(i+1))
	print(f"The ix value is {ix}")
	r = np.linspace(0.0,1.0, pt)
	print("r:\n",r)
	t= np.linspace(cl*4, (cl +1)*4, pt)
	print("\nt:\n", t)
	for i in r:
		print(i)