#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: douyin.py

@time: 19-12-22 下午2:38

@desc:

"""
import uiautomator2 as u2

from util.operator import Operator
from util.reader import Reader
from util.util import get_local_time, sleep, get_hour, sleep_random


class Douyin:
    _app_id = 'com.ss.android.ugc.aweme.lite'

    def __init__(self, d):
        self._operator = Operator(d)
        self._reader = Reader(d)

        self._bonus_res = 'com.ss.android.ugc.aweme.lite:id/kh'

    def start_app(self):
        self._operator.close_all_app()
        sleep()
        self._operator.close_all_app()
        sleep()
        self._operator.start_app(self._app_id)
        sleep()

    # 右下角“我”
    def right_bottom_me(self):
        print("Click 我")
        self._operator.click_xpath_if_exist('//*[@text="我"]')
        sleep()

    # 提钱
    def withdraw(self):
        if get_hour() < 12:
            return
        if self._operator.is_xpath_exist('//*[@text="去提现"]'):
            self._operator.click_xpath_if_exist('//*[@text="去提现"]')
            self._operator.click_xpath_if_exist('//*[@resource-id="app"]/android.view.View[4]/android.view.View[1]')
            self._operator.click_xpath_if_exist('//*[@text="立即提现"]')
            self._operator.click_xpath_if_exist('//android.app.Dialog/android.view.View[1]/android.view.View[4]')

    def watch_adv(self):
        sleep(15)
        self._operator.click_xpath_if_exist('//*[@text="关闭广告"]')
        sleep()

    def sign(self):
        self.right_bottom_me()
        # 中间取钱
        print("Click 赚钱")
        self._operator.click_resource_if_exist('com.ss.android.ugc.aweme.lite:id/kh')
        sleep()
        if self._operator.is_xpath_exist('//*[@text="看视频再赚"]'):
            self._operator.click_xpath_if_exist('//*[@text="看视频再赚"]')
            self.watch_adv()
        self._operator.click_xpath_if_exist('//*[@resource-id="app"]/android.view.View[3]')
        self.watch_adv()
        self.withdraw()
        # 第二行整点广告领取金币
        if self._operator.is_xpath_exist('//*[@text="去领取"]'):
            self._operator.click_xpath_if_exist('//*[@text="去领取"]')
        self._operator.click_resource_if_exist('com.ss.android.ugc.aweme.lite:id/yv')

    def watch(self):
        i = 0
        while i < 15:
            print(i, '-', get_local_time())
            self._reader.page_up()
            sleep_random()
            i += 1

    def is_video(self):
        return self._operator.is_xpath_exist('//*[@text="首页"]')

    def go_to_video(self):
        while not self.is_video():
            self._operator.go_back()
            sleep()
        self._operator.click_xpath_if_exist('//*[@text="首页"]')

    def douyin(self):
        print("%s Douyin start ..." % get_local_time())
        self.start_app()
        self.sign()
        self.go_to_video()
        self.watch()
        self._operator.close_all_app()
        print("%s Douyin end ..." % get_local_time())


if __name__ == '__main__':
    device_id = 'JGB9K17A18908832'
    d = u2.connect_usb(device_id)
    douyin = Douyin(d)
    douyin.douyin()
