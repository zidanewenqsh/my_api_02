import time
from functools import wraps


def timefn(fn):
    """计算性能的修饰器"""

    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1: .5f} s")
        return result

    return measure_time


# 在定义函数前进行装饰
@timefn
def test():
    s = 0
    for i in range(1000000):
        s += 1
    return s


test()
print(timefn)
print(timefn.__name__)
print(test)
print(test.__name__)