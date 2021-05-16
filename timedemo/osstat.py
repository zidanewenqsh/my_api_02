import os
import time
a = './osstat.py'
print(os.stat(a))
print(os.stat(a).st_atime)
print(os.stat(a).st_ctime)
print(os.stat(a).st_mtime)
t1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(a).st_atime))
t2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(a).st_ctime))
t3 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(a).st_mtime))
print(t1)
print(t2)
print(t3)

for roots, dirs, files in os.walk(r"D:\Ubuntu\PycharmProjects\my_api_02\timedemo"):
    print(roots)
    print(dirs)
    print(files)
