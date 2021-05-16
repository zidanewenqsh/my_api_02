import os
import time
def myfork():
    pid = os.fork()
    if pid==0:
        print("child")
    if pid>0:
        print("parent")
    else:
        print("error")
if __name__ == '__main__':
    myfork()