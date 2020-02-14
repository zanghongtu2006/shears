#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: huoshan.py

@time: 19-12-22 下午2:38

@desc:

"""
import uiautomator2 as u2

from util.operator import Operator
from util.reader import Reader
from util.util import get_local_time, sleep, get_hour, sleep_random


class Kuaishou:
    _app_id = 'com.ss.android.ugc.aweme.lite'
    _resource_id = _app_id + ":id/"
    _res_my_name = _resource_id + 'rd'
    _btn_laizhuanqian = _resource_id + 'ke'  # 下方中间钱包按钮
    _btn_continue_adv = _resource_id + 'a_g'  # 继续观看视频按钮
    _xpath_watch = '//*[@resource-id="app"]/android.view.View[2]/android.view.View[3]'  # 宝箱观看视频领更多金币
    _res_video_desc = _resource_id + 'tt'

    def __init__(self, d):
        self._d = d
        self._operator = Operator(d)
        self._reader = Reader(d)

    def start_app(self):
        self._operator.close_all_app()
        # self._operator.start_app(self._app_id)
        # if self._operator.is_resource_exists('com.ss.android.ugc.aweme.lite:id/al3'):
        #     self._operator.click_resource_if_exist('com.ss.android.ugc.aweme.lite:id/al3')
        # if self._operator.is_resource_exists('com.ss.android.ugc.aweme.lite:id/tc'):
        #     self._operator.click_resource_if_exist('com.ss.android.ugc.aweme.lite:id/tc')

    # 右下角“我”
    def into_me(self):
        print("Into 我")
        return self._operator.into_page_xpath('//*[@text="我"]', self._btn_laizhuanqian, None)

    def into_zhuanqian(self):
        print("Into 赚钱")
        return self._operator.into_page_resource(self._btn_laizhuanqian, None, '//*[@text="金币收益"]')

    def into_video(self):
        i = 0
        while not self._operator.is_resource_exists(self._res_video_desc):
            i += 1
            if i > 10:
                return False
            self.into_me()
            self._operator.click_xpath_if_exist('//*[@text="首页"]')
        return True

    def task(self):
        if self._operator.is_xpath_exist('//*[@text="看视频再赚"]'):
            self._operator.click_xpath_if_exist('//*[@text="看视频再赚"]')
            self.watch_adv()
        self._operator.go_back()
        # if self._operator.is_xpath_exist('//*[@text="开宝箱得金币"]'):
        #     self._operator.click_xpath_if_exist('//*[@text="开宝箱得金币"]')
        #     if self._operator.is_xpath_exist(self._xpath_watch):
        #         self._operator.click_xpath_if_exist(self._xpath_watch)
        #         self.watch_adv()

    # 提钱
    def withdraw(self):
        if get_hour() < 11:
            return
        if self._operator.is_xpath_exist('//*[@text="去提现"]'):
            self._operator.click_xpath_if_exist('//*[@text="去提现"]')
            if self._operator.is_xpath_exist('//*[@text="天天提"]'):
                self._operator.click_xpath_if_exist('//*[@text="天天提"]')
                self._operator.click_xpath_if_exist('//*[@text="立即提现"]')
                self._operator.click_xpath_if_exist('//android.app.Dialog/android.view.View[1]/android.view.View[4]')

    def sign(self):
        if not self.into_me():
            return False
            # 中间取钱
        if not self.into_zhuanqian():
            return False
        self.withdraw()
        self.task()
        if not self.into_me():
            return False
        # self._operator.click_xpath_if_exist('//*[@resource-id="app"]/android.view.View[3]')
        # self.watch_adv()
        # 第二行整点广告领取金币
        # if self._operator.is_xpath_exist('//*[@text="去领取"]'):
        #     self._operator.click_xpath_if_exist('//*[@text="去领取"]')
        # self._operator.click_resource_if_exist('com.ss.android.ugc.aweme.lite:id/yv')
        return True

    def watch_advs(self):
        i = 0
        while i < 20:
            self.watch_adv()
            i += 1

    def watch_adv(self):
        while True:
            try:
                self._d.xpath('//*[@text="看视频赚海量金币"]').click()
                break
            except Exception as e:
                print('Click resource failed' + str(e))
        count = 0
        while not self._operator.is_resource_exists('com.ss.android.ugc.livelite:id/rk'):
            sleep(5)
            count += 1
            if count > 8:
                self._operator.click_xpath_if_exist('//*[@text="关闭广告"]')
                return
        self._operator.click_resource_if_exist('com.ss.android.ugc.livelite:id/rk')

    def watch(self):
        i = 0
        while i < 150:
            print(i, '-', get_local_time())
            self._reader.page_up()
            sleep_random(20, 30)
            i += 1

    def is_video(self):
        return self._operator.is_xpath_exist('//*[@text="首页"]')

    def douyin(self):
        print("%s Douyin start ..." % get_local_time())
        # self.start_app()
        if not self.sign():
            return
        if not self.into_video():
            return
        self.watch()
        self._operator.close_all_app()
        print("%s Douyin end ..." % get_local_time())


if __name__ == '__main__':
    device_id = '192.168.168.10:5555'
    d = u2.connect(device_id)
    kuaishou = Kuaishou(d)
    # d.session(douyin._app_id, attach=True)
    while True:
        kuaishou.watch_advs()
        # kuaishou.watch()
        break
        # sleep(600)
