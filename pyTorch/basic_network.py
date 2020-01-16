import torch as tc
import torch.nn as nn
import torch.nn.functional as fn


class NN(nn.Module):
    def __init__(self):
        super().__init__()
        self.input_layer = nn.Linear(5*2, 32)
        self.hidden_layer1 = nn.Linear(32, 32)
        self.hidden_layer2 = nn.Linear(32, 32)
        self.output_layer = nn.Linear(32, 1) #OUT = Chance ot teanm 1 winning the game


    def foward_data(self, data):
        result = fn.relu(self.input_layer(data))
        result = fn.relu(self.hidden_layer1(data))
        result = fn.relu(self.hidden_layer2(data))
        result = self.output_layer(data)

        return fn.sigmoid(result, dim=1)


Network = NN()
print(Network)

