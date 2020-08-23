# -*- coding=utf-8 -*-

"""
 Verion: 1.0
 Since : 3.6
 Author: zhangjian
 Site: https://github.com/xarrow/
 File: nacos_listener.py
 Time: 2020/8/23
 
 Add New Functional nacos-sdk-python
"""
from abc import abstractmethod
from typing import Optional

from .nacos_base import NacosBaseRequest


class NacosListener(object):
    def __init__(self, listener_name):
        self._listener_name = listener_name

    @property
    def listener_name(self) -> str:
        return self._listener_name

    def before_invoke(self, request: NacosBaseRequest):
        pass

    def after_invoke(self, response: dict):
        pass

    def exception(self, exception: Exception):
        pass

    # ....


class NacosListenerManager(object):
    @abstractmethod
    def all_listeners(self) -> dict:
        pass

    @abstractmethod
    def add(self, nl: NacosListener):
        pass

    @abstractmethod
    def remove(self, nl_name: str):
        pass

    @abstractmethod
    def select(self, nl_name: str):
        pass

    def __iter__(self):
        self.all_listeners().__iter__()


class DefaultNacosListenerManager(NacosListenerManager):
    def __init__(self):
        self._nacos_manager_dict = {}

    def all_listeners(self) -> dict:
        return self._nacos_manager_dict

    def add(self, nl: NacosListener):
        self._nacos_manager_dict[nl.listener_name] = nl
        return self

    def remove(self, nl_name: str):
        self._nacos_manager_dict.pop(nl_name)
        return self

    def select(self, nl_name: str) -> Optional[NacosListener]:
        return self._nacos_manager_dict[nl_name]


class LoggerListener(NacosListener):
    def before_invoke(self, request: NacosBaseRequest):
        print("before invoke")

    def after_invoke(self, response: dict):
        print("after invoke")

    def exception(self, exception: Exception):
        print(exception)


class SnapshotListener(NacosListener):
    def before_invoke(self, request: NacosBaseRequest):
        print("SnapshotListener before invoke")

    def after_invoke(self, response: dict):
        print("SnapshotListener after invoke")

    def exception(self, exception: Exception):
        print("SnapshotListener" + exception)
