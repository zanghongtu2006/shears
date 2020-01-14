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
from util.util import sleep, get_hour, get_local_time, sleep_random


class Shuabao(object):
    _app_id = 'com.jm.video'

    def __init__(self, d):
        self._d = d
        self._operator = Operator(d)
        self._reader = Reader(d)

        self._bonus_res = 'com.ss.android.ugc.aweme.lite:id/kh'

    def start_app(self):
        self._operator.close_all_app()
        sleep()
        self._operator.close_all_app()
        sleep()
        self._operator.start_app(self._app_id)
        sleep(15)

    # 右下角“我”
    def right_bottom_me(self):
        print("Click 我")
        self._operator.click_xpath_if_exist(
            '//*[@resource-id="com.jm.video:id/tabLayout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[5]')
        sleep()

    def watch_adv(self):
        sleep(35)
        while not self._operator.is_resource_exists('com.jm.video:id/tt_video_ad_close'):
            sleep(1)
        self._operator.click_resource_if_exist('com.jm.video:id/tt_video_ad_close')

    # 提钱
    def withdraw(self):
        if get_hour() < 12:
            return
        adv_finish = False
        while not adv_finish:
            if self._operator.is_xpath_exist('//*[@text="提现"]'):
                self._operator.click_xpath_if_exist('//*[@text="提现"]')
                sleep()
                if self._operator.is_xpath_exist('//*[@text="立即观看"]'):
                    self._operator.click_xpath_if_exist('//*[@text="立即观看"]')
                    self.watch_adv()
                    self._operator.go_back()
                else:
                    adv_finish = True
        if self._operator.is_xpath_exist('//*[@text="提现"]'):
            self._operator.click_xpath_if_exist('//*[@text="提现"]')
            if self._operator.is_xpath_exist('//*[@text="立即提现"]'):
                self._operator.click_xpath_if_exist('//*[@text="立即提现"]')
                self._operator.click_xpath_if_exist('//*[@text="赚更多元宝"]')

    def sign(self):
        self.right_bottom_me()
        # 中间任务
        print("Click 任务")
        self._operator.click_xpath_if_exist(
            '//*[@resource-id="com.jm.video:id/tabLayout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]')
        sleep()
        if self._operator.is_resource_exists('com.jm.video:id/imgClose'):
            self._operator.click_resource_if_exist('com.jm.video:id/imgClose')
            sleep()
        self.withdraw()
        if self._operator.is_xpath_exist('//*[@text="立即签到"]'):
            self._operator.click_xpath_if_exist('//*[@text="立即签到"]')
            sleep()
            if self._operator.is_xpath_exist('//*[@text="放弃签到看视频签到"]'):
                resource = self._d.xpath('//*[@text="放弃签到看视频签到"]')
                resource.click()
                self.watch_adv()
                sleep()
                self._operator.click_xpath_if_exist(
                    '//*[@text="刷宝短视频"]/android.view.View[1]/android.view.View[6]/android.view.View[1]/android.view.View[1]')

    def watch(self):
        i = 0
        while i < 15:
            print(i, '-', get_local_time(), '-', self._operator.get_resource_text('com.jm.video:id/desc'))
            self._reader.page_up()
            sleep_random()
            i += 1

    def is_video(self):
        return self._operator.is_xpath_exist(
            '//*[@resource-id="com.jm.video:id/tabLayout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

    def go_to_video(self):
        while not self.is_video():
            self._operator.go_back()
            sleep()
        self._operator.click_xpath_if_exist(
            '//*[@resource-id="com.jm.video:id/tabLayout"]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]')

    def shuabao(self):
        print("%s Shuabao start ..." % get_local_time())
        self.start_app()
        self.sign()
        self.go_to_video()
        self.watch()
        self._operator.close_all_app()
        print("%s Shuabao end ..." % get_local_time())


if __name__ == '__main__':
    device_id = 'JGB9K17A18908832'
    d = u2.connect_usb(device_id)
    shuabao = Shuabao(d)
    shuabao.shuabao()
