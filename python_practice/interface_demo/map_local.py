#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-07-31 8:46
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : map_local.py

import json

from mitmproxy import ctx, http


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)

    def response(self, flow: http.HTTPFlow):
        # 判断是否是想要的请求信息，通过url判断
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
            # 打开文件，读取文件数据，作为响应给返回
            with open("map_local_data.json", encoding="utf-8") as f:
                data = json.load(f)
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]
