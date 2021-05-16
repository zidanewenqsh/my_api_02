#!/e/Soft/Python/Python38/python
# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# @File Name:        snstest01.py
# @Author:           wen
# @Version:          ver0_1
# @Created:          2021/4/6 9:35
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
import seaborn as sns

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

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
    x = np.random.randn(100)
    y = np.random.random(100)
    sns.set()
    fig, axes = plt.subplots(2, 3)
    sns.kdeplot(x, shade=False, ax=axes[0, 0])
    sns.kdeplot(x, cut=0, ax=axes[0, 1])
    sns.kdeplot(x, cumulative=True, ax=axes[0, 2])
    sns.kdeplot(x, shade=True, color='g', ax=axes[1, 0])
    sns.kdeplot(x, vertical=True, ax=axes[1, 1])
    # sns.kdeplot(y=x, ax=axes[1, 1])
    sns.kdeplot(x, y, shade=True, ax=axes[1, 2])
    plt.show()
