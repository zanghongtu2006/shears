#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: reader.py

@time: 19-12-18 上午10:54

@desc:

"""
import uiautomator2 as u2

from util.operator import Operator
from util.reader import Reader
from util.util import sleep, sleep_random, get_hour, get_local_time


class QuTouTiao(object):
    _app_id = 'com.jifen.qukan'

    def __init__(self, d):
        self._d = d
        self._operator = Operator(d)
        self._reader = Reader(d)

        self._article_list_res = 'com.jifen.qukan:id/aly'

        self._top_left_bonus_res = 'com.jifen.qukan:id/bwg'
        self._top_left_bonus_text = '领取'

        self._comment_res = 'com.jifen.qukan:id/a0o'
        self._comment_text = '全部评论'

    def start_app(self):
        self._operator.close_all_app()
        self._operator.close_all_app()
        self._operator.start_app(self._app_id)

    # 右下角“我”
    def right_bottom_me(self):
        print("Click 我的")
        self._operator.click_xpath_if_exist('//*[@text="我的"]')

    def sign(self):
        self.right_bottom_me()
        self.withdraw()
        print("Click 去签到")
        self._operator.click_xpath_if_exist('//*[@text="去签到"]')
        self._operator.click_xpath_if_exist('//*[@text="任务"]')
        print("60天超长签到")
        while not self._operator.is_xpath_exist('//*[@text="挑战60天超长签到"]'):
            self._reader.page_up()
        self._operator.click_xpath_if_exist('//*[@text="挑战60天超长签到"]')
        self._operator.go_back()

    def current_position(self):
        if self._operator.is_resource_exists('com.jifen.qukan:id/nz') and self._operator.is_resource_exists(
                'com.jifen.qukan:id/bpq'):
            return 'ARTICLE'
        else:
            return 'LIST'

    def withdraw(self):
        print("提现")
        # if get_hour() < 12:
        #     return
        self._operator.click_xpath_if_exist('//*[@text="我的"]')
        self._operator.click_resource_if_exist('com.jifen.qukan:id/auv')
        self._operator.click_xpath_if_exist('//*[@text="提现"]')
        self._operator.click_resource_if_exist('alipay_quick')
        self._operator.click_xpath_if_exist('//*[@text="我知道了"]')
        self._operator.go_back()
        self._operator.go_back()
        self._operator.go_back()

    def read(self):
        print("阅读文章")
        self._operator.click_xpath_if_exist('//*[@text="我的"]')
        self._operator.click_xpath_if_exist('//*[@text="头条"]')
        self._operator.click_xpath_if_exist('//*[@text="刷新"]')
        total_artical = 0
        while total_artical < 5:
            self._reader.page_up()
            article_list_length = self.get_article_list_length()
            self.get_top_left_bonus()
            for i in range(0, article_list_length):
                if self.in_article(i):
                    self.read_article()
                    total_artical += 1
                    self._operator.go_back()
                    print("total_artical: ", total_artical)

    def watch(self):
        print("观看视频")
        self._operator.click_xpath_if_exist('//*[@text="我的"]')
        self._operator.click_xpath_if_exist('//*[@text="视频"]')
        self._operator.click_xpath_if_exist('//*[@text="刷新"]')
        total_video = 0
        while total_video < 6:
            print("total_video: ", total_video)
            self._operator.click_resource_if_exist('com.jifen.qukan:id/qy')
            total_video += 1
            self.get_money()
            if self._operator.is_resource_exists('com.jifen.qukan:id/ud'):
                text = self._operator.get_resource_text('com.jifen.qukan:id/ud')
                if text is not None and text == '继续观看':
                    self._operator.click_resource_if_exist('com.jifen.qukan:id/ud')
            sleep_random()
            self._reader.page_up()

    def get_top_left_bonus(self):
        bonus_text = self._operator.get_resource_text(self._top_left_bonus_res)
        if bonus_text is not None and bonus_text == self._top_left_bonus_text:
            self._operator.click_resource_if_exist(self._top_left_bonus_res)

    def check_end(self):
        text = self._operator.get_resource_text(self._comment_res)
        return text is not None and text == self._comment_text

    def get_money(self):
        if self._operator.is_resource_exists('com.jifen.qukan:id/brl'):
            self._operator.click_resource_if_exist('com.jifen.qukan:id/brl')
            self._operator.click_resource_if_exist('com.jifen.qukan:id/a66')

    def get_article_list_length(self):
        length = self._reader.get_article_list_length(self._article_list_res)
        while length == 0:
            self._reader.page_up()
            length = self._reader.get_article_list_length(self._article_list_res)
        return length

    def in_article(self, i):
        if self._reader.in_article(self._article_list_res, i):
            sleep()
            return True
        else:
            return False

    def read_article(self):
        up_count = 0
        while not self.check_end() and up_count < 10:
            self._reader.read_article('V')
            up_count += 1
            self.get_money()

    def qutoutiao(self):
        print("%s Qutoutiao start ..." % get_local_time())
        self.start_app()
        self.sign()
        self.read()
        self.watch()
        self._operator.close_all_app()
        print("%s Qutoutiao end ..." % get_local_time())


if __name__ == '__main__':
    device_id = 'JGB9K17A18908832'
    d = u2.connect_usb(device_id)
    qtt = QuTouTiao(d)
    qtt.qutoutiao()

    # total_artical = 0
    # while True:
    #     print("total_artical:", total_artical)
    #     if total_artical > 30:
    #         print('end')
    #         break
    #     qtx.page_up()
    #     article_list_length = qtx.get_article_list_length()
    #     print(article_list_length)
    #     qtx.get_top_left_bonus()
    #
    #     for i in range(0, article_list_length):
    #         if qtx.in_article(i):
    #             qtx.read()
    #             total_artical += 1
    #             qtx.out_article()
