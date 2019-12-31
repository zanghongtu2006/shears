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
import time

import uiautomator2 as u2

from util.operator import Operator
from util.reader import Reader


class MiDu:
    _app_id = 'com.lechuan.mdwz'

    _article_list_res = 'com.lechuan.mdwz:id/gm'
    _article_read_res = 'com.lechuan.mdwz:id/sh'
    _article_advertise_close_res = 'com.lechuan.mdwz:id/g_'

    # _article_save_to_shell_res = 'com.martian.ttbook:id/dialog_close'
    # _article_end_res = 'com.martian.ttbook:id/tv_buy_reading_purcgase'
    # _article_end_text = '余额不足请充值'

    def __init__(self, d):
        self._reader = Reader(d)
        self._operator = Operator(d)

    def get_article_list_length(self):
        return self._operator.get_resource_length(self._article_list_res)

    def next_article_list(self):
        self._reader.page_up()
        time.sleep(3)

    def in_article(self, i):
        self._reader.in_article(self._article_list_res, i)
        time.sleep(3)
        self._operator.click_resource_if_exist(self._article_read_res)
        time.sleep(3)
        self._operator.click_resource_if_exist(self._article_advertise_close_res)

    def out_article(self):
        print(self._operator.get_resource_text('com.martian.ttbook:id/duration_bonus'))
        self._operator.go_back()
        time.sleep(3)
        # self._operator.click_resource_if_exist(self._article_save_to_shell_res)
        # time.sleep(3)
        while 0 == self.get_article_list_length():
            self._operator.go_back()
            time.sleep(3)

    def check_end(self):
        return False
        # text = self._operator.get_resource_text(self._article_end_res)
        # return text is not None and text == self._article_end_text

    def read(self):
        while not midu.check_end():
            now = int(time.time())
            time_struct = time.localtime(now)
            current_hour = int(time.strftime("%H", time_struct))
            if 3 < current_hour < 8:
                time.sleep(600)
                return
            self._reader.page_left()
            time.sleep(random.randint(5, 7))
            self._operator.click_resource_if_exist(self._article_advertise_close_res)


if __name__ == '__main__':
    d = u2.connect_usb('JGB9K17A18908832')
    midu = MiDu(d)
    while True:
        length = midu.get_article_list_length()
        print(length)
        for i in range(0, length):
            midu.in_article(i)
            midu.read()
            midu.out_article()
            midu.next_article_list()
