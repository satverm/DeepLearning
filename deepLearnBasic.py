
# The basics of deep learnjng models
# This codw sgows how deep learning is done using
# inputs: for a neuron/s in any layer
# weights: (a kind of multiplication factor for each neuron)
# biases: an addition/offset for the neuron whixh is applied after the input is multiplied by the weight
## So its like using line equation mx + b
    # where m is the input, x is weight and b is the bias
inputs = [1.0, 2.5, 3.1]

weights = [2.0, 1.5, 2.2]

bias = 3.6

# Lets find the result or output
output = (
inputs[0] * weights[0] +
inputs[1] * weights[1] +
inputs[2] * weights[2] 
) + bias

print(output)

## Lets do the same by using numpy dot products
import numpy as np

op = np.dot(weights, inputs) + bias

print("This is the output using np dot product ", op)



