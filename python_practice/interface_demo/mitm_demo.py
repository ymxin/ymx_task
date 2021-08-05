#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time：2021-07-30 7:56
# @Author：yaomiaoxin
# @Email : murcymurcy@163.com
# @File : mitm_demo.py
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
            # 修改原始数据
            # 获取的text是string类型，需要对数据进行操作，数据转换为字典类型
            print('yaomiaoxin')
            data = json.loads(flow.response.text)
            # 修改数据信息
            data["data"]["items"][0]["quote"]["name"] = "ireaderirader"
            data["data"]["items"][1]["quote"]["name"] = "ireaderirader"
            data["data"]["items"][2]["quote"]["name"] = "ireaderirader"
            # 目前是python对象 ，将其转化为string类型
            flow.response.text = json.dumps(data)


addons = [
    Counter()
]
