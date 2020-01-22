#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: reader.py

@time: 19-12-18 上午10:54

@desc:

"""
import random

import uiautomator2 as u2

from util.operator import Operator
from util.reader import Reader
from util.util import sleep, sleep_random, get_local_time


class MiDu:
    _app_id = 'com.lechuan.mdwz'
    _resource_id = _app_id + ":id/"

    _res_article_list = _resource_id + 'gm'
    _res_article_read = _resource_id + 're'
    _res_article_advertise_close = _resource_id + 'p6'
    _btn_adv_in_adv = _resource_id + 'pe'
    _btn_adv_close_adv = _resource_id + 'tt_video_ad_close'
    # _article_save_to_shell_res = 'com.martian.ttbook:id/dialog_close'
    # _article_end_res = 'com.martian.ttbook:id/tv_buy_reading_purcgase'
    # _article_end_text = '余额不足请充值'

    def __init__(self, d):
        self._d = d
        self._reader = Reader(d)
        self._operator = Operator(d)
        self._reader = Reader(d)

    def page_up(self):
        self._reader.page_up()

    def start_app(self):
        self._operator.close_all_app()
        self._operator.start_app(self._app_id)
        while not (self._operator.is_xpath_exist('//*[@text="我的"]') and
                   self._operator.is_xpath_exist('//*[@text="福利"]')):
            self._operator.go_back()

    def into_me(self):
        print("Into 我")
        return self._operator.into_page_xpath('//*[@text="我的"]', None, None)

    def get_article_list_length(self):
        return self._operator.get_resource_length(self._article_list_res)

    def next_article_list(self):
        self.page_up()
        sleep()

    def in_article(self, i):
        self._reader.in_article(self._article_list_res, i)
        sleep()
        self._operator.click_resource_if_exist(self._article_read_res)
        sleep()
        self._operator.click_resource_if_exist(self._article_advertise_close_res)

    def out_article(self):
        print(self._operator.get_resource_text('com.martian.ttbook:id/duration_bonus'))
        self._operator.go_back()
        sleep()
        # self._operator.click_resource_if_exist(self._article_save_to_shell_res)
        # time.sleep(3)
        while 0 == self.get_article_list_length():
            self._operator.go_back()
            sleep()

    def check_end(self):
        return False
        # text = self._operator.get_resource_text(self._article_end_res)
        # return text is not None and text == self._article_end_text

    def read(self):
        i = 0
        while not self.check_end():
            i += 1
            print(i, '-', get_local_time())
            self._d.click(0.988, round(random.uniform(0.3, 0.7), 3))
            sleep_random(7, 10)
            self._operator.click_resource_if_exist('com.lechuan.mdwz:id/pb')
            # 看视频翻倍金币
            # if self._operator.is_resource_exists(self._btn_adv_in_adv):
            #     self._operator.click_resource_if_exist(self._btn_adv_in_adv)
            #     while self._operator.is_resource_exists(self._btn_adv_close_adv):
            #         sleep()
            #     self._operator.click_resource_if_exist(self._btn_adv_close_adv)

            # self._operator.click_resource_if_exist(self._res_article_advertise_close)
            # self._operator.click_resource_if_exist('com.lechuan.mdwz:id/g_')
            # s = self._operator.get_resource_text('com.lechuan.mdwz:id/nz')
            # if s is not None and s == '立即领取':
            #     self._operator.click_resource_if_exist('com.lechuan.mdwz:id/nz')
            #     time.sleep(1)
            #     self._operator.click_resource('com.lechuan.mdwz:id/g_')
            # self._operator.click_resource_if_exist('com.lechuan.mdwz:id/gy')

    def midu(self):
        self.start_app()


if __name__ == '__main__':
    d = u2.connect_usb('JGB9K17A18908832')
    midu = MiDu(d)
    midu.read()
    # length = midu.get_article_list_length()
    # print(length)
    # for i in range(0, length):
    #     midu.in_article(i)
    #     midu.read()
    # midu.out_article()
    # midu.next_article_list()
