#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-04-11 14:07
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : conftest.py
# 日志信息收集
import logging

logging.basicConfig(level=logging.INFO,
                    # 日志格式
                    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    # 打印日志的时间
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # 日志文件存放的目录（目录必须存在）及日志文件名
                    filename='result/report.log',
                    # 打开日志文件的方式
                    filemode='a'
                    )

root_log = logging.getLogger(__name__)
