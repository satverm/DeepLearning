# ver 6_0_2 softmax activation: ReLU would clip all negative values 
# so we use sofmax activation function which used exponential function and then normalises it by dividing each value by sum of all values
# but the problem is that the outputs of the exponnetial function may grow too big to throw an overflow error
# so to prevent that we normalise the inputs itself before softmax activation where we subtract all values from biggest value so all inputs lie between -infinity to 0 and  as e**0 is 1
# all inputs lie between 0 and 1 
# the exponenrial function is explained in a separate code in the dolder 
# ver 5_0_1 using spiral data as input
# Basic Layer Model using classes and numpy
import numpy as np
import nnfs
from nnfs_dataset import  spiral_data
nnfs.init()
#np.random.seed(0)  # to have same random values
# X is taken as the batch of input vaues, here we are taking 3 batches
X =  [[1, 2, 3, 2.5 ],  # 4 inputs in each batch taken here
[2.0, 5.0, -1.0, 2.0],
[-1.5, 2.7, 3.3, -0.8]
]

X,y = spiral_data(100,3)
#print("X:\n", X.shape)
#print("y:\n", y)
class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))
	def forward(self, inputs):
		self.output = np.dot(inputs, self.weights) + self.biases
		
class Activation_ReLU:
		def forward(self, inputs):
			self.output= np.maximum(0, inputs)
			
class Activation_Softmax:
		def forward(self, inputs):
			exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims= True))
			probabilities = exp_values / np.sum(exp_values, axis=1, keepdims= True)
			self.output = probabilities
		
layer1 = Layer_Dense(2,3) # 1st argumnet is the number of inputs in each batch, 2nd is the number of neurons desired in layer one
layer1.forward(X)
#print("Layer1 output:\n", layer1.output)
activation1 = Activation_ReLU()

activation1.forward(layer1.output)
#print("Activation1 output:\n", activation1.output)
layer2 = Layer_Dense(3,3) # 1st argument  is the outputs from the first layer which would be equal to the neurons in the 1st layer, 2nd argument is the neurons desired in second layer
layer2.forward(activation1.output)
activation2 = Activation_Softmax()
activation2.forward(layer2.output)
#probabilities = activation2.output
print("probabilities:\n", activation2.output[:5])
#layer1.forward(X)

#layer2.forward(layer1.output)


## Testing Outputs

'''

print("Number of inputs: ", len(X[0]))
print("Number of input Batches:", len(X))
for (index,item) in enumerate(X):
	print("Batch :",index, "\n",item)

print("\nlayer1 weights:\n",layer1.weights)
print("\nLayer1 neurons: ",len(layer1.biases[0]))
print("\nlayer1  biases:\n", layer1.biases)

print("\nlayer1 forward(X) output\n",layer1.output)

print("\nlayer2 weights:\n",layer2.weights)
print("\nLayer2 neurons: ", len(layer2.biases[0]))
print("\nlayer2  biases:\n", layer2.biases)

print("\nlayer2 output after and taking layer 1 output as input:\n",layer2.output)

'''