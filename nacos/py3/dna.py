# -*- coding=utf-8 -*-

"""
 Verion: 1.0
 Since : 3.6
 Author: zhangjian
 Site: https://github.com/xarrow/
 File: dna.py
 Time: 2020/8/28
 
 Add New Functional nacos-sdk-python
"""

import threading


class SimpleNacosTimer(object):
    def __init__(self):
        """
        thread safe since 3.3
        """
        self._task_container = list()
        pass

    def schedular(self, interval: int, func, *args, **kwargs):
        func(*args, **kwargs)
        _timer = threading.Timer(interval, self.schedular, (interval, func, *args,), **kwargs)
        _timer.start()
