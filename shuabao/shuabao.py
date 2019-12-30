#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: douyin.py

@time: 19-12-22 下午2:38

@desc:

"""
import random
import time

import uiautomator2 as u2

from util.operator import Operator
from util.reader import Reader


class Shuabao(object):
    _app_id = 'com.ss.android.ugc.aweme.lite'

    def __init__(self, d):
        self._operator = Operator(d)
        self._reader = Reader(d)

        self._bonus_res = 'com.ss.android.ugc.aweme.lite:id/kh'

    def watch(self):
        i = 0
        while i < 2000:
            print(i)
            self._reader.page_up()
            time.sleep(random.randint(20, 25))
            i += 1


if __name__ == '__main__':
    device_id = 'JGB9K17A18908832'
    d = u2.connect_usb(device_id)
    douyin = Shuabao(d)
    while True:
        douyin.watch()
