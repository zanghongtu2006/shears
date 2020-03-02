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
from util.util import get_local_time, sleep_random


class Watcher:
    _app_ids = ['com.kuaishou.nebula',  # 快手
                'com.ss.android.ugc.aweme.lite',  # 抖音
                'com.jm.video',  # 刷宝
                'com.yuncheapp.android.pearl',  # 快点看
                ]

    def __init__(self, d):
        self._operator = Operator(d)
        self._reader = Reader(d)
        self._d = d

    def watch(self):
        i = 0
        while True:
            try:
                package_name = self._d.app_current()['package']
            except Exception as e:
                print('Get package name failed', e)
                package_name = None
            if package_name is None or package_name not in self._app_ids:
                print(package_name)
                sleep_random(1, 7)
                continue
            print(i, '-', get_local_time())
            self._reader.page_up()
            sleep_random(5, 15)
            i += 1


if __name__ == '__main__':
    device_id = '192.168.168.8:5555'
    d = u2.connect(device_id)
    print(d.current_app)
    watcher = Watcher(d)
    # d.session(douyin._app_id, attach=True)
    while True:
        watcher.watch()
        # sleep(600)
