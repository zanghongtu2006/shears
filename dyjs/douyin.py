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


class Douyin:
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

    def close_nonthings(self):
        self._operator.click_resource_if_exist('com.ss.android.ugc.aweme.lite:id/al3')

    def sing_in(self):
        if self._operator.click_resource_if_exist('com.ss.android.ugc.aweme.lite:id/kh'):
            self.close_nonthings()
            # 跳过签到视频
            self._operator.click_xpath_if_exist(
                '//android.app.Dialog/android.view.View[1]/android.view.View[2]/android.view.View[5]')
            # 领取右下角宝箱
            self._operator.click_xpath_if_exist('//*[@resource-id="app"]/android.view.View[3]')
            self._operator.click_xpath_if_exist(
                '//android.app.Dialog/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]')

    def go_to_video(self):
        self._operator.go_back()
        self._operator.click_xpath_if_exist('//*[@text="首页"]')


if __name__ == '__main__':
    device_id = 'JGB9K17A18908832'
    d = u2.connect_usb(device_id)
    douyin = Douyin(d)
    # douyin.sing_in()
    while True:
        douyin.watch()
