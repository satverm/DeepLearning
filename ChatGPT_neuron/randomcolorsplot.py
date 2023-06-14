import numpy as np
import matplotlib.pyplot as plt

# Generate random x and y data
num_points = 50
x = np.random.rand(num_points)
y = np.random.rand(num_points)

# Generate random colors
colors = np.random.rand(num_points)

# Create the plot
plt.scatter(x, y, c=colors, cmap='rainbow')

# Customize the plot
plt.title('Random Data Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Colors')

# Display the plot
plt.show()
