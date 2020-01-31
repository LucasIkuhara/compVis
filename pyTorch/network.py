import torch as tc
import torch.nn as nn
import torch.nn.functional as fn
import numpy as np
import pandas as pd
import torch.optim as optim

class NN(nn.Module):
    def __init__(self):
        nn.Module.__init__(self)
        self.input_layer = nn.Linear(10, 32)
        self.hidden_layer1 = nn.Linear(32, 32)
        self.output_layer = nn.Linear(32, 1) #OUT = Chance ot teanm 1 winning the game

    def forward(self, data):
        result = fn.relu(self.input_layer(data))
        result = fn.relu(self.hidden_layer1(result))
        result = self.output_layer(result)
        result = tc.sigmoid(result)
     
        return result


#Loading the dataset
raw_data = pd.read_csv("treated_dataset.csv", 'r')
print(raw_data.iloc[0][0])

# print(raw_data[0])
# dataset = tc.tensor(raw_data[1])
# dataset2 = tc.rand((1, 10))

# #dataset = dataset.view(-1, 10)
# #dataset2 = dataset2.view(-1, 10)

# print(dataset)
# print(dataset2)
# network = NN()

# #Declaring optimizer
# optimizer = optim.Adam(network.parameters(), lr=0.01)
# Epochs = 5
# for epoch in range(Epochs):
#     for data in trainset:
#         X, y = data
#         network.zero_grad()
#         output = network(X.view(-1, 10))
#         loss = fn.nll_loss(output, y)
#         loss.backward()
#         optimizer.step()
#     print("loss:", loss)

#REDUCTION MODEL 
#Based on the models of Generative Adversarial Networks, one must wonder if it's 
#a viable alternative to use the inference model of a trained neural network to 
#train a new network with a smaller number of layers, in order to gain speed-ups