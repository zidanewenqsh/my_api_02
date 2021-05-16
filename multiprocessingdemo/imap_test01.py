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

# 1、apply 和 apply_async 一次执行一个任务，但 apply_async 可以异步执行，因而也可以实现并发。
#
# 2、map 和 map_async 与 apply 和 apply_async 的区别是可以并发执行任务。
#
# 3、starmap 和 starmap_async 与 map 和 map_async 的区别是，starmap 和 starmap_async 可以传入多个参数。
#
# 4、imap 和 imap_unordered 与 map_async 同样是异步，区别是:

# map_async生成子进程时使用的是list，而imap和 imap_unordered则是Iterable，map_async效率略高，而imap和 imap_unordered内存消耗显著的小。
#
# 在处理结果上，imap 和 imap_unordered 可以尽快返回一个Iterable的结果，而map_async则需要等待全部Task执行完毕，返回list。
#
# 而imap 和 imap_unordered 的区别是：imap 和 map_async一样，都按顺序等待Task的执行结果，而imap_unordered则不必。 imap_unordered返回的Iterable，会优先迭代到先执行完成的Task。 不理解的看最下面的一组例子。


def func(msg):
    print("msg: ", msg)
    time.sleep(max(6 - msg, 1))
    return msg


if __name__ == "__main__":
    pool = multiprocessing.Pool(3)
    results = pool.imap(func, range(10))
    # print(f"{results=}")
    for res in results:
        print("res: ", res)

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()

    print("Sub-process(es) done.")

