# Basic Layer Model using classes and numpy
import numpy as np



X =  [[1, 2, 3, 2.5 ],
[2.0, 5.0, -1.0, 2.0],
[-1.5, 2.7, 3.3, -0.8]
]

class Layer_Dense:
	def __init__(self, n_inputs, n_neurons):
		self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
		self.biases = np.zeros((1, n_neurons))
	def forward(self, inputs):
		self.output = np.dot(inputs, self.weights) + self.biases
		
layer1 = Layer_Dense(4,5)

print("\nlayer1 weights:\n",layer1.weights)
print("\nlayer1  biases:\n", layer1.biases)

layer2 = Layer_Dense(5,6)

print("\nlayer2 weights:\n",layer2.weights)
print("\nlayer2  biases:\n", layer2.biases)


layer1.forward(X)
print("\nlayer1 forward(X) output\n",layer1.output)
print("\nlayer1 weights:\n",layer1.weights)
print("\nlayer1  biases:\n", layer1.biases)

layer2.forward(layer1.output)
print("\nlayer2 output after forward and taking layer 1 output as input:\n",layer2.output)
print("\nlayer2 weights:\n",layer2.weights)
