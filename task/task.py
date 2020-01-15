#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: task.py

@time: 19-12-26 下午4:16

@desc:

"""

import uiautomator2 as u2

from dyjs.douyin import Douyin
from midu.midu import MiDu
from qtt.qutoutiao import QuTouTiao
from shuabao.shuabao import Shuabao
from util.operator import Operator
from util.util import get_minute, sleep, get_hour
from wanqia.wanqia import WanQia


class Task(object):
    def __init__(self, d):
        self._operator = Operator(d)
        self._douyin = Douyin(d)
        self._shuabao = Shuabao(d)
        self._wanqia = WanQia(d)
        self._wanqia_success = False
        self._qutoutiao = QuTouTiao(d)
        self._midu = MiDu(d)

    def exec_shuabao(self):
        self._shuabao.shuabao()

    def exec_qutoutiao(self):
        self._qutoutiao.qutoutiao()

    def exec_douyin(self):
        self._douyin.douyin()

    def exec_wanqia(self):
        if not self._wanqia_success:
            self._wanqia_success = self._wanqia.wanqia()

    def stop_all_apps(self):
        self._operator.close_all_app()


if __name__ == '__main__':
    device_id = 'JGB9K17A18908832'
    d = u2.connect_usb(device_id)
    task = Task(d)
    wanqia_success = False
    while True:
        if 0 < get_hour() < 7:
            # if get_minute() < 20:
            #     task.exec_wanqia()
            sleep(60)
            continue
        if get_minute() < 10:
            task.exec_douyin()
        elif get_minute() < 20:
            task.exec_shuabao()
        elif get_minute() < 30:
            task.exec_qutoutiao()
        else:
            task.stop_all_apps()
            sleep(300)
            continue
