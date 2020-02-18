import torch as tc
from model import NN
from champion_dictionary import *

net = NN()
net.load_state_dict(tc.load("model.wab"))

input_data = tc.rand((10), dtype=tc.float)
out = net(input_data)
print(input_data)

if out < 0.5:
    print("Blue team")
    print(out)

else:
    print("Red team")
    print(out)