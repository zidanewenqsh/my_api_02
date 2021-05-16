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
    time.sleep(2)
    print("end")
# apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，apply(func[, args[, kwds]])是阻塞的（理解区别，看例1例2结果区别）
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

    pool = multiprocessing.Pool(processes=2)
    for i in range(4):
        msg = "hello %d" % (i)
        pool.apply_async(func, (msg,))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~") # 先执行这句
    pool.close()
    pool.join()  # 调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("Sub-process(es) done.")
