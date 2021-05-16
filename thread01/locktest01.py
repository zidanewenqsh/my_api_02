import threading
import os
import time
x = 0
mLock = threading.Lock()
def a(i):

    mLock.acquire()
    print("i:",i)
    global x
    # print("a start")
    time.sleep(0.1)
    # print("x=", x)
    # print("a end")
    x += 1
    mLock.release()
# def b():
#     global x
#     # print("b start")
#     time.sleep(1)
#     # print("x=", x)
#     # print("b end")
#     x += 1
if __name__ == '__main__':
    print(0)
    t1 = time.time()
    ths = []
    for i in range(10):
        th = threading.Thread(target=a, args=[i])
        ths.append(th)
    for i in ths:
        i.start()
    for i in ths:
        i.join()
    t2 = time.time()
    print("time:",t2-t1, "x=",x)