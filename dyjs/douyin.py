#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: douyin.py

@time: 19-12-22 下午2:38

@desc:

"""
import time
import uiautomator2 as u2

from util.reader import Reader


class Douyin:
    def __init__(self, device_id):
        self._d = u2.connect_usb(device_id)
        self._reader = Reader(self._d)

    def watch(self):
        self._reader.page_up()
        time.sleep(30)


if __name__ == '__main__':
    douyin = Douyin('JGB9K17A18908832')
    while True:
        douyin.watch()
