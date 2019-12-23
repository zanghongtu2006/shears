#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: screen.py

@time: 19-12-20 上午10:38

@desc:

"""
import random


class Screen:
    def __init__(self, d):
        self._d = d
        self._screen_size = d.window_size()

        self._top = [int(self._screen_size[1] / 6), int(self._screen_size[1] * 2 / 6)]
        self._bottom = [int(self._screen_size[1] * 4 / 6), int(self._screen_size[1] * 5 / 6)]
        self._left = [int(self._screen_size[0] / 6), int(self._screen_size[0] * 2 / 6)]
        self._right = [int(self._screen_size[0] * 4 / 6), int(self._screen_size[0] * 5 / 6)]
        self._vert_center = [int(self._screen_size[0] * 3 / 6), int(self._screen_size[0] * 4 / 6)]  # 屏幕纵向中间
        self._horiz_center = [int(self._screen_size[1] * 3 / 6), int(self._screen_size[1] * 4 / 6)]  # 屏幕横向中间

    def page_left(self):
        self._d.swipe(random.randint(self._right[0], self._right[1]),
                      random.randint(self._vert_center[0], self._horiz_center[1]),
                      random.randint(self._left[0], self._left[1]),
                      random.randint(self._vert_center[0], self._horiz_center[1]))

    def page_right(self):
        self._d.swipe(random.randint(self._left[0], self._left[1]),
                      random.randint(self._vert_center[0], self._horiz_center[1]),
                      random.randint(self._right[0], self._right[1]),
                      random.randint(self._vert_center[0], self._horiz_center[1]))

    def page_up(self):
        self._d.swipe(random.randint(self._vert_center[0], self._vert_center[1]),
                      random.randint(self._bottom[0], self._bottom[1]),
                      random.randint(self._vert_center[0], self._vert_center[1]),
                      random.randint(self._top[0], self._top[1]))

    def page_down(self):
        self._d.swipe(random.randint(self._vert_center[0], self._vert_center[1]),
                      random.randint(self._top[0], self._top[1]),
                      random.randint(self._vert_center[0], self._vert_center[1]),
                      random.randint(self._bottom[0], self._bottom[1]))


if __name__ == '__main__':
    pass
