import os
import time
import threading
def test(p):
    time.sleep(1)
    print(p)
    time.sleep(1)
t1 = time.time()
ths = []
for i in range(3):
    th = threading.Thread(target=test,args=[i])
    ths.append(th)
for i in ths:
    i.start()
for i in ths:
    i.join()
t2= time.time()
print("time:", t2-t1)