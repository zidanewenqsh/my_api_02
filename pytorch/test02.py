import torch
def app(x):
    x += 2
    return x
a = torch.arange(24).reshape(3,2,4)
# print(a)
# a = a.permute(1,2,0)
# b = a.reshape(2,-1)
# print(b)
# print(b.flatten())
print(a.T.size())
# print(a.t().size())
print(app(3))