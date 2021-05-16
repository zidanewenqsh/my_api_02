import multiprocessing
from multiprocessing import shared_memory
import time
# 协程
# 协程(coroutine)最初在1963年被提出，但并没有受到重视，现在重新火起来，很大一部分原因是Web服务的发展，对服务器并发的需求。它是一种比线程更加轻量级的存在， 协程不被操作系统内核所管理，而完全由程序员自己去控制和调度，带来的好处就是性能得到了很大的提升，不会像线程切换那样消耗资源
# https://blog.csdn.net/yingshukun/article/details/89857204
# 原文链接：https://blog.csdn.net/yingshukun/article/details/89857204
def methodA():
    while True:
        print("----A 任务---")
        yield
        print("----A sleep---")
        time.sleep(2)


def methodB(c):
    while True:
        print("----B 任务---")
        next(c)
        print("----B sleep---")
        time.sleep(2)


if __name__ == '__main__':
    a = methodA()
    methodB(a)
