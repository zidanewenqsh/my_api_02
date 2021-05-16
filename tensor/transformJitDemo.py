import torch
import numpy as np
from torchvision import transforms
import cv2
from PIL import Image
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,),(0.5,)),
    # transforms.Normalize((0.5, 0.5, 0.5),(0.5, 0.5, 0.5))
])
def transformer(img):
    return transform(img)
if __name__ == '__main__':
    # a = np.random.randint(0, 255, size=(1, 100, 100), dtype=np.uint8)
    img = cv2.imread("cat01.jpg")
    # cv2.imshow("img",img)
    # cv2.waitKey()
    x = transformer(img)
    print(x)
    # module_trace = torch.jit.trace(transformer,img)
