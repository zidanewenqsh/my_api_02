#!/e/Soft/anaconda3/python2
# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# @File Name:        apply_test01.py
# @Author:           wen
# @Version:          ver0_1
# @Created:          2021/4/23 9:51
# @Description:      Main Function:    imap
# @Note:             xxx
# Function List:     hello() -- print helloworld
# History:
#       <author>    <version>   <time>      <desc>
#       wen         ver0_2      2020/12/15  lambda
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
from itertools import repeat
from multiprocessing.pool import ThreadPool
# def func(msg):
#     print("msg: ", msg)
#     time.sleep(max(6 - msg, 1))
#     return msg
def func(msg1, msg2):
    print("msg: ", msg1+msg2)
    time.sleep(max(6 - msg2, 1))
    return msg1+msg2

if __name__ == "__main__":
    # pool = multiprocessing.Pool(3) # 进程池
    pool = multiprocessing.pool.ThreadPool(3) # 线程池
    # results = pool.imap(lambda x:func(*x), range(10))
    # results = ThreadPool(3).imap(lambda x:func(*x), zip(repeat(10), range(10)))
    results = pool.imap(lambda x:func(*x), zip(repeat(10), range(10)))
    # print(f"{results=}")
    for res in results:
        print(f"{res=}")

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    # pool.close()
    # pool.join()

    print("Sub-process(es) done.")

