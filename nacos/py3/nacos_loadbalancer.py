# -*- coding=utf-8 -*-

"""
 Verion: 1.0
 Since : 3.6
 Author: zhangjian
 Site: https://github.com/xarrow/
 File: nacos_loadbalancer.py
 Time: 2020/8/22
 
 Add New Functional nacos-sdk-python
"""

from nacos.exception import NacosException


class NacosServer(object):
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @classmethod
    def uri(cls, uri: str):
        if uri == '' or ':' not in uri:
            raise NacosException("NacosServer uri is illegal")

        uri_split_array = uri.split(":")
        _host = uri_split_array[0]
        _port = uri_split_array[1]
        if not _host:
            raise NacosException("NacosServer host in uri is illegal")
        try:
            _port = int(_port)
        except Exception:
            raise NacosException("NacosServer port in uri is illegal")
        return cls(_host, _port)


# todo
class NacosLoadBalancer(object):
    __slots__ = ['_sever_pool']

    def __init__(self, *args, **kwargs):
        self._sever_pool = set()

    def all_servers(self) -> set:
        return self._sever_pool

    def select(self) -> NacosServer:
        pass

    def policy(self):
        pass

    def reject(self):
        pass
