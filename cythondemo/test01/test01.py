# coding: utf-8
# 这个import会先找hello.py，找不到就会找hello.so
import hello  # 导入了hello.so
import add_c
import func3
import time
def app_python(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum
hello.say_hello_to('tom')
t1 = time.time()
a = func3.app(50000)
t2 = time.time()
print(a)
print(t2-t1)
t1 = time.time()
b = app_python(50000)
t2 = time.time()
print(t2-t1)
print(b)