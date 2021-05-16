import time
# 1、获取当前时间
t1 = time.time()  # 获取当前时间戳
# >1500252381.100721

t2 = time.localtime()  # 当前时间的 struct_time 形式
# >time.struct_time(tm_year=2017, tm_mon=7, tm_mday=17, tm_hour=9, tm_min=6, tm_sec=29, tm_wday=0, tm_yday=198, tm_isdst=0)

# time.ctime() == time.asctime()  # 当前时间的字符串形式
# >'Mon Jul 17 09:08:20 2017'


# 2、把当前时间戳转化为字符格式
t3 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# >'2017-07-17 09:10:24'
print(t1)
print(t2)
print(t3)
print(time.ctime())
print(time.mktime(t2))
