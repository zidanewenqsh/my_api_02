#!/e/Soft/Python/Python38/python
# -*- coding: utf-8 -*- #
# ------------------------------------------------------------------
# @File Name:        threadpooltest2.py
# @Author:           wen
# @Version:          ver0_1
# @Created:          2021/5/10 22:13
# @Description:      Main Function:    xxx
# Function List:     hello() -- print helloworld
# History:
#       <author>    <version>   <time>      <desc>
#       wen         ver0_1      2020/12/15  xxx
# ------------------------------------------------------------------
import socket
import threading
from threading import Thread
import threading
import sys
import time
import random
from Queue import Queue


# 创建队列实例， 用于存储任务
queue = Queue()


# 定义需要线程池执行的任务
def do_job():
    while True:
        i = queue.get()
        time.sleep(1)
        print
        'index %s, curent: %s' % (i, threading.current_thread())
        queue.task_done()


if __name__ == '__main__':
    # 创建包括3个线程的线程池
    for i in range(3):
        t = Thread(target=do_job)
        t.daemon = True  # 设置线程daemon  主线程退出，daemon线程也会推出，即时正在运行
        t.start()
    # 模拟创建线程池3秒后塞进10个任务到队列
    time.sleep(3)
    for i in range(10):
        queue.put(i)


