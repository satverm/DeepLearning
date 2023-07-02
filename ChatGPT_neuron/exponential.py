# exponenrial function and its usage in softmax actvation without using numpy to explain basics

X = [-3, -2, -1, 0, 1, 2, 3, 5, 10, 100] # add 1000 to the list and you may find overflow error in the e**(1000)
## you can test the above value of X  by not using the normalisation of inputs as we will do bwlow to prevent overflow error in e**x
#normalising X by subtracting all values in X from the max value
def find_max(input_list):
	temp_max = input_list[0]
	for item in input_list:
		if item > temp_max:
			temp_max = item
	return temp_max
max_X = find_max(X)

y = []
e = 2.718281828459045 # we can het the same using numpy.e after importing numpy

for value in X:
	y.append(e**value) # gwtting y = e to the power x for eaxh value x in X

# normalise the output by dividing each value by sum of all values
sum_y = (sum(x for x in y)) # using a generator and aumming all valuea
norm_y = [x/sum_y for x in y] # normalising each y but not the inputs at this stage

## Testing Zone
print(X, "\n",y) # watch how output increases qith higher powers
print(max_X)
print(sum_y)
print(type(sum_y))
print(norm_y) # chexk if all values are btween 0 and 1