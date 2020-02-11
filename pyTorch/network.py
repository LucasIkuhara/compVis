import torch as tc
import torch.nn as nn
import torch.nn.functional as fn
import numpy as np
import pandas as pd
import torch.optim as optim
from sklearn.model_selection import train_test_split 

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
raw_data_x = pd.read_csv("treated_dataset.csv")
print(raw_data_x.tail(5))
print(raw_data_x.columns)
raw_data_x["BTC1"]
raw_data_y = pd.read_csv("treated_dataset.csv")
raw_data_x.drop("WIN", axis=1)
raw_data_y = raw_data_y.filter('WIN', axis=1)


x_train, x_test, y_train, y_test = train_test_split(raw_data_x, raw_data_y, test_size=0.2, random_state=123)

network = NN()

#Declaring optimizer
optimizer = optim.Adam(network.parameters(), lr=0.01)
Epochs = 5
for epoch in range(Epochs):
    for data in x_train:
        x_train, y_train = data
        network.zero_grad()
        output = network(X.view(-1, 10))
        loss = fn.nll_loss(output, y)
        loss.backward()
        optimizer.step()
    print("loss:", loss)

#REDUCTION MODEL 
#Based on the models of Generative Adversarial Networks, one must wonder if it's 
#a viable alternative to use the inference model of a trained neural network to 
#train a new network with a smaller number of layers, in order to gain speed-ups