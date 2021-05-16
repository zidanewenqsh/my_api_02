import ctypes
import time
import torch
dll = ctypes.windll.LoadLibrary("libfunc.dll")
hello = ctypes.windll.LoadLibrary("hello.dll")
# torfunc = ctypes.windll.LoadLibrary("libtorchdll.dll")
# showtensor = torfunc.showtensor
# dll = ctypes.cdll.LoadLibrary("Dll1.dll")
# print(dll)
app_3 = dll.func
app_3.argtypes = [ctypes.c_int]
# app_3.restype = ctypes.c_int
app_3(10)
hello_1 = hello.hello
hello_1()
