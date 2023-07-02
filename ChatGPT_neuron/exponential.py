# exponenrial function and its usage in softmax actvation without using numpy to explain basics

X = [-3, -2, -1, 0, 1, 2, 3, 5, 10, 100] # add 1000 to the list and you may find overflow error in the e**(1000)
## you can test the above value of X  by not using the normalisation of inputs as we will do bwlow to prevent overflow error in e**x
#normalising X by subtracting maximum of all values in X from all values in X so all values are less than or equal to Zero
def find_max(input_list):
	temp_max = input_list[0]
	for item in input_list:
		if item > temp_max:
			temp_max = item
	return temp_max
max_X = find_max(X)
norm_X = [x-max_X for x in X] # input are normalised  with max value as 0 and others less than 0 so that when we find y = e**x then all valyes lie between 0 and 1 for as e**0 is 1 and e**(-infinity) approaches 0
# this way all the outputs of the exponential function are between  0 and 1 and without any overflow error for inputs.

y = []
e = 2.718281828459045 # we can het the same using numpy.e after importing numpy

#for value in X: # commented out as we will now use norm_X
for value in norm_X:
	y.append(e**value) # gwtting y = e to the power x for eaxh value x in X for testing or norm_X finally

# normalise the output by dividing each value by sum of all values
sum_y = (sum(x for x in y)) # using a generator and aumming all valuea
print("sum_y: \n", sum_y)
norm_y = [x/sum_y for x in y] # normalising each y but not the inputs at this stage

## Testing Zone

from custom_print import v_print # my custom print function to peint variable name also
v_print("X", "\n","y") # watch how output increases qith higher powers
v_print("max_X")
v_print("norm_X")
v_print("sum_y")
v_print(type(sum_y))
v_print("norm_y") # chexk if all values are btween 0 and 1