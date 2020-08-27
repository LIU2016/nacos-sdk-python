# -*- coding=utf-8 -*-

"""
 Verion: 1.0
 Since : 3.6
 Author: zhangjian
 Site: https://github.com/xarrow/
 File: nacos_snapshot.py
 Time: 2020/8/22
 
 Add New Functional nacos-sdk-python
 本地缓存策略

 那些情况需要缓存策略？
 只缓存在本地？ 可不可以开放缓存接口，接入redis，db，file
"""
from abc import abstractmethod


class NacosSnapshot(object):
    def __init__(self, snapshot_name: str):
        self._snapshot_name = snapshot_name

    @abstractmethod
    def add_snapshot(self):
        pass

    @abstractmethod
    def select_snapshot(self):
        pass
    # ....
