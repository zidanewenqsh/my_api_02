import os
import sys
import time
a = 1
with open("a.txt", "w") as f:
    while True:
    # for i in range(100):
        # print(a, file=f, flush=True)
        f.write(str(a))
        f.flush()
        sys.stdout.flush()
        a+=1
        time.sleep(0.1)