import torch as tc
from network import NN

net = NN()
net.load_state_dict("model.wab")

