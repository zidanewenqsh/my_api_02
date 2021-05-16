import torch
import numpy as np
from torchvision import transforms
transform = transforms.Compose([
    transforms.ToTensor(),
    # transforms.Normalize((0.5,),(0.5,)),
    # transforms.Normalize((0.5, 0.5, 0.5),(0.5, 0.5, 0.5))
])
# a0 = np.array([[100,200],[50,250]],dtype=np.uint8)
a0 = np.random.randint(0,255,size=(5,5),dtype=np.uint8)
mins = np.min(a0)
maxs = np.max(a0)
inters = maxs - mins
print(mins, maxs, inters)
a = torch.from_numpy(a0.astype(np.float))
print(a)
# a_ = (a - mins)/inters
# print("a_",a_)
a = a/255
print(a)
print("cal")
# print((a-0.5)/0.5)
print("*")
m = torch.mean(a)
s = torch.std(a)
s1 = torch.std(a,unbiased=False)
# print(m)
# print(s)
# print(s1)
t = transform(a0)
print("transform")
print(t)
# img_tensor[0][0] = img_tensor[0][0].sub(0.485).div(0.229);
# img_tensor[0][1] = img_tensor[0][1].sub(0.456).div(0.224);
# img_tensor[0][2] = img_tensor[0][2].sub(0.406).div(0.225);
