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


class TaoXiaoShuo:
    _app_id = 'com.martian.ttbook'

    _article_list_res = 'com.martian.ttbook:id/bs_list_book_name'
    _article_read_res = 'com.martian.ttbook:id/bd_reading'
    _article_advertise_close_res = 'com.martian.ttbook:id/bt_cancel'
    _article_save_to_shell_res = 'com.martian.ttbook:id/dialog_close'
    _article_end_res = 'com.martian.ttbook:id/tv_buy_reading_purcgase'
    _article_end_text = '余额不足请充值'

    def __init__(self, device_id):
        self._d = u2.connect_usb(device_id)
        self._operator = Operator(self._d)
        self._reader = Reader(self._d)

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
        self._operator.click_resource_if_exist(self._article_save_to_shell_res)
        time.sleep(3)
        while 0 == self.get_article_list_length():
            self._operator.go_back()
            time.sleep(3)

    def check_end(self):
        text = self._operator.get_resource_text(self._article_end_res)
        return text is not None and text == self._article_end_text

    def read(self):
        i = 0
        while not taoxiaoshuo.check_end():
            i += 1
            now = int(time.time())
            time_struct = time.localtime(now)
            print(i, '-', time.strftime("%Y-%m-%d %H:%M:%S", time_struct))
            self._reader.page_left()
            time.sleep(random.randint(5, 7))
            self._operator.click_resource_if_exist(self._article_advertise_close_res)


if __name__ == '__main__':
    taoxiaoshuo = TaoXiaoShuo('JGB9K17A18908832')
    while True:
        length = taoxiaoshuo.get_article_list_length()
        print(length)
        for i in range(0, length):
            taoxiaoshuo.in_article(i)
            taoxiaoshuo.read()
            taoxiaoshuo.out_article()
        taoxiaoshuo.next_article_list()
