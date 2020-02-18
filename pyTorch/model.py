import torch as tc
import torch.nn as nn
import torch.nn.functional as fn

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