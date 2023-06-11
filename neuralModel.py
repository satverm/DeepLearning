import torch
import torch.nn as nn
import torch.nn.functional as F

# we can use iris dataset from google
# Now we will create a Model Class that inherits nn.Module

class Model(nn.Module):
	super().__init__()
	def __init__(self, in_features=4, h1=8, h2=9, out_features=3):
		self.fc1 = nn.Linear(in_features, h1)
		self.fc2 = nn.Linear(h1, h2)
		self.out= nn.Linear(h2, out_features)
		
	def forward(self, x):
		x= F.relu(self.fc1(x))
		x= F.relu(self.fc2(x))
		x = self.out(x)
		
		return x
torch.manual.seed(41)

model = Model(in_features=(1,2,3,4), out_features=("red", "yellow", "green"))
print(model.out())

		