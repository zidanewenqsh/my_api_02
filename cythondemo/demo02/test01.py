import loop
import time

import math
def looptest1(num=10000):
    for i in range(num):
        for j in range(num):
            a = math.sqrt(math.log2(i+1)+math.log10(j+1))

num = 10000
t1 = time.time()
loop.looptest(num)
t2 = time.time()
print(t2-t1)

t1 = time.time()
looptest1(num)
t2 = time.time()
print(t2-t1)