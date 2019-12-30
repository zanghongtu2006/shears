#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: reader.py

@time: 19-12-18 上午10:54

@desc:

"""
import time

import uiautomator2 as u2

from util.operator import Operator
from util.reader import Reader


class QuTouTiao(object):
    _app_id = 'com.jifen.qukan'

    def __init__(self, d):
        self._operator = Operator(d)
        self._reader = Reader(d)

        self._article_list_res = 'com.jifen.qukan:id/am8'

        self._top_left_bonus_res = 'com.jifen.qukan:id/bvi'
        self._top_left_bonus_text = '领取'

        self._comment_res = 'com.jifen.qukan:id/a0o'
        self._comment_text = '全部评论'

    def get_top_left_bonus(self):
        bonus_text = self._operator.get_resource_text(self._top_left_bonus_res)
        if bonus_text is not None and bonus_text == self._top_left_bonus_text:
            self._operator.click_resource_if_exist(self._top_left_bonus_res)

    def check_end(self):
        text = self._operator.get_resource_text(self._comment_res)
        return text is not None and text == self._comment_text

    def get_money(self):
        self._operator.click_resource_if_exist('com.jifen.qukan:id/bpy')
        time.sleep(2)
        self._operator.click_resource_if_exist('com.jifen.qukan:id/a6e')

    def page_up(self):
        self._reader.page_up()

    def get_article_list_length(self):
        length = self._reader.get_article_list_length(self._article_list_res)
        while length == 0:
            self._reader.page_up()
            length = self._reader.get_article_list_length(self._article_list_res)
        return length

    def in_article(self, i):
        if self._reader.in_article(self._article_list_res, i):
            time.sleep(3)
            return True
        else:
            return False

    def out_article(self):
        self._operator.go_back()
        time.sleep(3)

    def read(self):
        up_count = 0
        while not qtx.check_end() and up_count < 10:
            self._reader.read_article('V')
            up_count += 1
            qtx.get_money()


if __name__ == '__main__':
    device_id = 'JGB9K17A18908832'
    d = u2.connect_usb(device_id)
    qtx = QuTouTiao(d)

    total_artical = 0
    while True:
        print("total_artical:", total_artical)
        if total_artical > 50:
            print('end')
            break
        qtx.page_up()
        article_list_length = qtx.get_article_list_length()
        print(article_list_length)
        qtx.get_top_left_bonus()

        for i in range(0, article_list_length):
            if qtx.in_article(i):
                qtx.read()
                total_artical += 1
                qtx.out_article()
