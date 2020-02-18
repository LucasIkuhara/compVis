import torch as tc
import torch.nn as nn
import torch.nn.functional as fn
import numpy as np
import pandas as pd
import torch.optim as optim
from sklearn.model_selection import train_test_split 
from torch.utils.data import Dataset, DataLoader

class NN(nn.Module):
    def __init__(self):
        nn.Module.__init__(self)
        self.input_layer = nn.Linear(10, 15)
        self.hidden_layer1 = nn.Linear(15, 15)
        self.output_layer = nn.Linear(15, 1) #OUT = Chance ot teanm 1 winning the game

    def forward(self, data):
        result = fn.relu(self.input_layer(data))
        result = fn.relu(self.hidden_layer1(result))
        result = self.output_layer(result)
        result = tc.sigmoid(result)
     
        return result


#Loading the dataset
raw_data_x = pd.read_csv("treated_dataset.csv")
raw_data_x["BTC1"]
raw_data_y = pd.read_csv("treated_dataset.csv")
raw_data_x = raw_data_x.drop("WIN", axis=1)
raw_data_y = raw_data_y["WIN"]

class Data(Dataset):

    def __init__(self):
        raw_data_x = pd.read_csv("treated_dataset.csv").dropna()
        raw_data_x["BTC1"]
        raw_data_y = pd.read_csv("treated_dataset.csv").dropna()
        raw_data_x = raw_data_x.drop("WIN", axis=1)
        raw_data_y = raw_data_y["WIN"]

        #self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(raw_data_x, raw_data_y, test_size=0.2, random_state=123)
        self.x_train = tc.tensor(raw_data_x.values, dtype=tc.float)
        self.y_train = tc.tensor(raw_data_y.values, dtype=tc.float)

    def __getitem__(self, index):
        return self.x_train[index], self.y_train[index]

    def __len__(self):
        return len(self.x_train)


dataset = Data()
train_loader = DataLoader(dataset=dataset, batch_size=32, shuffle=True, num_workers=0)


#Declaring network and optimizer
print("Initializing network")
network = NN()
optimizer = optim.Adam(network.parameters(), lr=0.1)
criterion = nn.BCELoss(reduction='mean')


for epoch in range(5):
    for i, data in enumerate(train_loader, 0):
        # get the inputs
        inputs, labels = data

        # Forward pass: Compute predicted y by passing x to the model
        y_pred = network(inputs)

        # Compute and print loss
        loss = criterion(y_pred, labels)
        print(f'Epoch {epoch + 1} | Batch: {i+1} | Loss: {loss.item():.4f}')

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

print("Done training")

tc.save(network.state_dict(), "model.wab")


#REDUCTION MODEL 
#Based on the models of Generative Adversarial Networks, one must wonder if it's 
#a viable alternative to use the inference model of a trained neural network to 
#train a new network with a smaller number of layers, in order to gain speed-ups