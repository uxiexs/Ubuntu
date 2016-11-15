#!/usr/bin/python3
#coding:utf-8

#*******************************************************************************
# 练习
# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
#*******************************************************************************
import re
from datetime import datetime, timezone, timedelta, tzinfo
def to_timestamp(dt_str,tz_str):
    now = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S') # str转转换datetime
    dt_utc = re.match(r'UTC([+|-]\d+):00$', tz_str) # 正则匹配时区
    now_swich = timezone(timedelta(hours = int(dt_utc.group(1)))) # 创建时区
    z = now.replace(tzinfo=now_swich) # 转换时区
    return z.timestamp() # 返回时间戳

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
print(t1)

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t2)
# assert t2 == 1433121030.0, t2

# print('Pass')
