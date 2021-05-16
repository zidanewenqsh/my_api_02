import os
import sys
import time
a = 1
f1 = os.open("b.txt", os.O_RDWR|os.O_CREAT|os.O_APPEND)
print(f1)
# with open("a.txt", "w") as f:
while True:
# for i in range(100):
    # print(a, file=f, flush=True)
    os.write(f1,str(a).encode('utf-8'))
    os.write(f1, bytes("\n",'utf-8'))
    a+=1
    time.sleep(1)
os.close(f1)