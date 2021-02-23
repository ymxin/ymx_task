#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

print(time.asctime())
print(time.time())
print(time.localtime())

print(time.strftime("%Y年%m月%d日 %H:%M:%S", time.localtime()))

# 获取两天前的时间

now_time = time.time()
two_days_before = now_time - 60 * 60 * 24 * 2

time_tuple = time.localtime(two_days_before)

print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))

# 获取三天后的时间

now_time = time.time()
two_days_ofter = now_time + 60 * 60 * 24 * 3

time_tuple = time.localtime(two_days_ofter)

print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))
