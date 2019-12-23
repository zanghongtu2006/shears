#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: operator.py

@time: 19-12-18 下午5:51

@desc:

"""


class Operator:

    def __init__(self, d):
        self._d = d

    def is_resource_exists(self, resource_id, instance=0):
        try:
            return self._d(resourceId=resource_id, instance=instance).exists()
        except Exception as e:
            print('Check resourceId exists failed, return False' + str(e))
            return False

    def click_resource(self, resource_id, instance=0, timeout=2):
        try:
            self._d(resourceId=resource_id, instance=instance).click(timeout=timeout)
            return True
        except Exception as e:
            print('Click resource failed' + str(e))
            return False

    def click_resource_if_exist(self, resource_id, timeout=2):
        if self.is_resource_exists(resource_id):
            try:
                self._d(resourceId=resource_id).click(timeout=timeout)
                return True
            except Exception as e:
                print('Click resource failed' + str(e))
                return False

    def get_resource_length(self, resource_id):
        if self.is_resource_exists(resource_id):
            try:
                return len(self._d(resourceId=resource_id))
            except Exception as e:
                print('Get resource number by resourceId failed' + str(e))
                return 0
        return 0

    def get_resource_text(self, resource_id, instance=0):
        if self.is_resource_exists(resource_id, instance):
            try:
                return self._d(resourceId=resource_id, instance=instance).get_text()
            except Exception as e:
                print('Get resource text by resourceId failed' + str(e))
                return None
        return None

    def go_back(self):
        self._d.press("back")


if __name__ == '__main__':
    pass
