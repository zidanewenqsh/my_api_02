#!/e/Soft/anaconda3/python2
# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# @File Name:        apply_test01.py
# @Author:           wen
# @Version:          ver0_1
# @Created:          2021/4/23 9:51
# @Description:      Main Function:    xxx
# @Note:             xxx
# Function List:     hello() -- print helloworld
# History:
#       <author>    <version>   <time>      <desc>
#       wen         ver0_1      2020/12/15  xxx
# ------------------------------------------------------------------
import os
import sys
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
import multiprocessing
import time


def func(msg):
    print("msg:", msg)
    time.sleep(max(6 - msg, 1))
    return msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(3)
    results = pool.imap_unordered(func, range(6))
    for res in results:
        print("res: ", res)

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()

