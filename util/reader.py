#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: reader.py

@time: 19-12-19 下午2:02

@desc:

"""

from util.operator import Operator
from util.screen import Screen
from util.util import sleep_random


class Reader:
    def __init__(self, d):
        self._d = d
        self._operator = Operator(self._d)
        self._screen = Screen(self._d)

    def get_article_list_length(self, article_list_resource_id):
        article_list_length = self._operator.get_resource_length(article_list_resource_id)
        while article_list_length == 0:
            self.page_up()
            article_list_length = self._operator.get_resource_length(article_list_resource_id)
            if article_list_length > 0:
                return article_list_length
        return article_list_length

    def page_left(self):
        self._screen.page_left()

    def page_up(self):
        self._screen.page_up()

    def in_article(self, article_list_resource_id, article_index):
        title = self._operator.get_resource_text(article_list_resource_id, article_index)
        if title is None:
            return False
        print("INTO: " + title)
        if not self._operator.click_resource(article_list_resource_id, article_index):
            return False
        return True

    def read_article(self, direction='HORIZON'):
        if direction == 'HORIZON' or direction == 'H':
            self._screen.page_left()
        else:
            self._screen.page_up()
        sleep_random(3, 6)

    def exit_article(self):
        self._operator.go_back()


if __name__ == '__main__':
    pass
