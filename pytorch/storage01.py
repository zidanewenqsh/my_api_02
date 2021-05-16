import torch
a = torch.arange(24)
# print(a.storage())
b = a.view(6,4)
# print(b.storage())
print(id(a.storage())==id(b.storage()))
a[1] = 10
print(b)
print(id(a.storage()),id(b.storage()))
a = a.float()
# a[1] = 2

print(id(a.storage()),id(b.storage()))
print(a.data_ptr(), a.element_size(), b.element_size())
print(a.dtype, b.dtype)
print(id(a.storage())==id(b.storage()))
# c = torch.Tensor(a.storage())
# c = torch.Tensor(b.storage()) # RuntimeError: Expected Storage of type Float but got type Long for argument 1 'storage'
c = a[2:]
print(id(a.storage()), id(c.storage()), a.data_ptr(), c.data_ptr())
print(a.storage_offset(),c.storage_offset())
d = b[::2,::2]
print(b)
print(d)
print(b.stride(), d.stride())
print(b.is_contiguous(), d.is_contiguous())