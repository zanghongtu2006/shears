#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: wanqia.py

@time: 20-1-13 下午6:01

@desc:

"""
import uiautomator2 as u2

from util.operator import Operator
from util.reader import Reader
from util.util import get_local_time, sleep


class WanQia:
    _app_id = 'com.yyk.whenchat'

    def __init__(self, d):
        self._d = d
        self._operator = Operator(d)
        self._reader = Reader(d)

    def start_app(self):
        self._operator.close_all_app()
        self._operator.close_all_app()
        self._operator.start_app(self._app_id)
        text = self._operator.get_resource_text('com.yyk.whenchat:id/btnLeft')
        if text is not None and text == '':
            self._operator.click_resource_if_exist('com.yyk.whenchat:id/btnLeft')

    def sign(self):
        self._operator.click_resource_if_exist('com.yyk.whenchat:id/ivTabMine')
        self._operator.click_xpath_if_exist(
            '//*[@resource-id="com.yyk.whenchat:id/vInvite"]/android.widget.ImageView[1]')
        self._operator.click_position(0.561, 0.878)
        while not self._operator.is_resource_exists('com.tencent.mm:id/ln'):
            self._operator.click_xpath_if_exist(
                '//*[@resource-id="com.yyk.whenchat:id/gvBody"]/android.widget.LinearLayout[1]/android.widget.ImageView[1]')
            sleep(30)
        self._operator.go_back()
        return True

    def wanqia(self):
        print("%s WanQia start ..." % get_local_time())
        self.start_app()
        success = self.sign()
        self._operator.close_all_app()
        print("%s WanQia end ..." % get_local_time())
        return success


if __name__ == '__main__':
    device_id = 'JGB9K17A18908832'
    d = u2.connect_usb(device_id)
    wanqia = WanQia(d)
    wanqia.wanqia()
