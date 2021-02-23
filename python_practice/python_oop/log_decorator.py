#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-02-21 20:38
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : log_decorator.py

import logging

# 设置基本配置
logging.basicConfig(level=logging.DEBUG)
# 自定义logger
logger = logging.getLogger('log')


# 定义装饰器
def log_decorator(func):
    def wrapper(*args, **kwargs):
        # 加上log信息
        logger.debug(f"装饰器：{log_decorator.__name__}->传入函数：{func.__name__}")
        # 调用传入的函数对象
        return func(*args, **kwargs)

    return wrapper
