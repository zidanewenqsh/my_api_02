#!/e/Soft/Python/Python38/python
# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# @File Name:        test01.py
# @Author:           wen
# @Version:          ver0_1
# @Created:          2021/4/6 8:52
# @Description:      Main Function:    xxx
# Function List:     hello() -- print helloworld
# History:
#       <author>    <version>   <time>      <desc>
#       wen         ver0_1      2020/12/15  xxx
# ------------------------------------------------------------------
import os
import numpy as np
import torch
import logging
import argparse
import shutil
import cv2
import time
import threading
import multiprocessing
from pathlib import Path
from tqdm import tqdm
from matplotlib import pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D # 和下面一样
from mpl_toolkits.mplot3d.axes3d import Axes3D
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    torch.set_printoptions(precision=2, threshold=np.inf, sci_mode=False)
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', type=str, default=r'', help='')
    parser.add_argument('-b', type=int, default=0, help='')
    parser.add_argument('-c', nargs='+', type=int, default=[0, 1], help='')
    parser.add_argument('-d', action='store_true', help='')
    parser.add_argument('-e', nargs='?', const=True, default=False, help='')
    opt = parser.parse_args()
    # 绘制3维的散点图
    x = np.random.randint(0, 10, size=100)
    y = np.random.randint(-20, 20, size=100)
    z = np.random.randint(0, 30, size=100)

    # 此处fig是二维
    fig = plt.figure()
    # 将二维转化为三维
    axes3d = Axes3D(fig)

    # axes3d.scatter3D(x,y,z)
    # 效果相同
    axes3d.scatter(x, y, z)

    # ax = plt.axes(projection='3d')
    plt.show()
    plt.pause(0.1)