import torch
import torch.nn as nn
import shutil
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv2d(1,1,3,1,1),
            nn.ReLU()
        )
    def forward(self, x):
        y = self.layer(x)
        return y
if __name__ == '__main__':
    net = Net().cuda()
    net.eval()
    x = torch.randn(1,1,5,5).cuda()
    y = net(x)
    print(y.size())
    module = torch.jit.script(net)
    # modulefile = "module.pt"
    # module.save(moudlefile)
    # dstdir = r"D:\CLionProjects\libtorchapi\cmake-build-release"
    # shutil.copy(modulefile,dstdir)
    print(module.graph)
