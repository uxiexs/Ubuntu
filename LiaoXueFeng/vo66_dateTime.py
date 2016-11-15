#!/usr/bin/python3
# coding:utf-8
from datetime import datetime
#*************************************************************************
# datetime是Python处理日期和时间的标准库。
# 获取当前日期和时间:
#*************************************************************************

now = datetime.now()
print(now)
print(type(now))

#*************************************************************************
# 注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。
# 如果仅导入import datetime，则必须引用全名datetime.datetime。
# datetime.now()返回当前日期和时间，其类型是datetime。
#*************************************************************************
dt = datetime(2015,12,25,14,5)
print(dt)

# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
print(dt.timestamp())
print(datetime.now().timestamp())

# timestamp转换为datetime:
t = 0
print(datetime.fromtimestamp(t)) # 本地时间 东八区
print(datetime.utcfromtimestamp(t)) # UTC时间 格林威治

# str转换为datetime:
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：
cday = datetime.strptime('2016-11-1 11:06:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：

print(now.strftime('%a, %b, %d %H:%M'))

# datetime加减:
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
from datetime import timedelta
print(now+timedelta(hours=24))
print(now+timedelta(hours=-24))

# 本地时间转换为UTC时间:
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
now = datetime.now()
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)
# 如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

# 时区转换
# 我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo2_dt = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo2_dt)
