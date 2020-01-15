#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

@author: Hongtu Zang

@contact: zanghongtu2006@gmail.com

@file: operator.py

@time: 19-12-18 下午5:51

@desc:

"""
from util.util import sleep


class Operator:

    def __init__(self, d):
        self._d = d

    def close_all_app(self):
        print("Closing all apps...")
        self._d.app_stop_all(excludes=['com.github.uiautomator'])
        self._d.app_stop_all(excludes=['com.github.uiautomator'])
        sleep()
        print("All apps are closed.")

    def start_app(self, app_id):
        print("Starting app %s ..." % app_id)
        self._d.app_start(app_id)
        sleep(60)
        print("App %s ... is started." % app_id)

    def is_resource_exists(self, resource_id, instance=0):
        try:
            return self._d(resourceId=resource_id, instance=instance).exists()
        except Exception as e:
            print('Check resourceId exists failed, return False' + str(e))
            return False

    def click_position(self, x, y):
        try:
            print('Click position: ', x, y)
            self._d.click(x, y)
            sleep()
            return True
        except Exception as e:
            print('Click position failed' + str(e))
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
                print('Click resource: ', resource_id)
                self._d(resourceId=resource_id).click(timeout=timeout)
                sleep()
                return True
            except Exception as e:
                print('Click resource failed' + str(e))
                return False
        else:
            print('Resource %s not exist' % resource_id)
            return False

    def click_xpath_if_exist(self, xpath, timeout=2):
        if self._d.xpath(xpath).exists:
            try:
                print('Click xpath: ', xpath)
                self._d.xpath(xpath).click(timeout=timeout)
                sleep()
                return True
            except Exception as e:
                print('Click xpath failed' + str(e))
                return False
        else:
            print('XPath %s not exist' % xpath)
            return False

    def is_xpath_exist(self, xpath):
        resource = self._d.xpath(xpath)
        return resource.exists

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
        sleep()

    def into_page_xpath(self, xpath, page_cursor_res, page_cursor_xpath):
        print("Into xpath: ", xpath)
        i = 0
        while not self.is_xpath_exist(xpath):
            i += 1
            if i > 10:
                return False
            self.go_back()
        i = 0
        if page_cursor_res is not None:
            while not self.is_resource_exists(page_cursor_res):
                i += 1
                if i > 10:
                    return False
                self.click_xpath_if_exist(xpath)
        i = 0
        if page_cursor_xpath is not None:
            while not self.is_xpath_exist(page_cursor_xpath):
                i += 1
                if i > 10:
                    return False
                self.click_xpath_if_exist(xpath)
        return True

    def into_page_resource(self, resource_id, page_cursor_res, page_cursor_xpath):
        print("Into resource: ", resource_id)
        i = 0
        while not self.is_resource_exists(resource_id):
            i += 1
            if i > 10:
                return False
            self.go_back()
        i = 0
        if page_cursor_xpath is not None:
            while not self.is_xpath_exist(page_cursor_xpath):
                i += 1
                if i > 10:
                    return False
                self.click_resource_if_exist(resource_id)
        i = 0
        if page_cursor_res is not None:
            while not self.is_resource_exists(page_cursor_res):
                i += 1
                if i > 10:
                    return False
                self.click_resource_if_exist(resource_id)

        return True


if __name__ == '__main__':
    pass
