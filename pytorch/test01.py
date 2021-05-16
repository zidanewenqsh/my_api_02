import torch
import numpy as np
a = torch.Tensor([[256,128,127],[-128,5,6]])
print(a.shape)
print(a.flatten().size())
a1 = a.numpy()
print(a1.size)
print(np.size(a1))
print(torch.numel(a))
print(float(a[0][0]))
c = a.char()
d = a.byte()
print(c)
print(d)
b = torch.tensor([127,128,255,256],dtype=torch.uint8)
print(b)
b1 = torch.tensor([127,128,255,256],dtype=torch.int8)
print(b1)

