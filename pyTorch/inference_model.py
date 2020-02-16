import torch as tc
from network import NN

net = NN()
net.load_state_dict("model.wab")

input_data = tc.rand(10)
out = net(input_data)

if out < 0.5:
    print("Blue team")
    print(out)

else:
    print("Red team")
    print(out)