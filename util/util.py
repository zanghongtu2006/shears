#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: util.py

@time: 20-1-13 下午4:44

@desc:

"""
import random
import time


def sleep(second=10):
    print("Sleep %d seconds" % second)
    time.sleep(second)


def sleep_random(min=20, max=25):
    second = random.randint(min, max)
    print("Sleep %d seconds" % second)
    time.sleep(second)


def get_hour():
    now = int(time.time())
    time_struct = time.localtime(now)
    return int(time.strftime("%H", time_struct))


def get_minute():
    now = int(time.time())
    time_struct = time.localtime(now)
    return int(time.strftime("%M", time_struct))


def get_local_time():
    now = int(time.time())
    time_struct = time.localtime(now)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_struct)


if __name__ == '__main__':
    pass
