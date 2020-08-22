# -*- coding:utf-8 -*-

"""
 Author: helixcs
 Site: https://zeit.fun
 File: nacos_base.py.py
 Time: 2020/8/17
 Reference at:https://nacos.io/zh-cn/docs/open-api.html
"""
from abc import abstractmethod, ABC
from enum import Enum
from typing import Optional

from nacos.exception import NacosRequestException

NACOS_CONFIG = "/nacos/v1/cs/configs"

JSON_TYPE = Optional[dict]


class RequestMethods(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    HEAD = "HEAD"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"


class NacosBaseRequest(object):
    __slots__ = ['_request_api_name', '_request_method', '_request_headers', '_request_timeout', '_namespace']

    def __init__(self,
                 request_api_name: Optional[str],
                 request_method: RequestMethods,
                 request_headers: Optional[dict] = None,
                 request_timeout: Optional[int] = None,
                 namespace: Optional[str] = None,
                 ):
        self._request_api_name = request_api_name
        self._request_method = request_method
        self._request_headers = request_headers
        self._request_timeout = request_timeout
        self._namespace = namespace

    @property
    def request_api_name(self) -> Optional[str]:
        return self._request_api_name

    @property
    def request_method(self) -> RequestMethods:
        return self._request_method

    @property
    def request_headers(self) -> Optional[dict]:
        return self._request_headers

    @request_api_name.setter
    def request_api_name(self, request_api_name: str):
        self._request_api_name = request_api_name

    @request_method.setter
    def request_method(self, request_method: RequestMethods):
        self._request_method = request_method

    @request_headers.setter
    def request_headers(self, request_headers: Optional[dict]):
        self._request_headers = request_headers

    @property
    def request_timeout(self) -> Optional[int]:
        return self._request_timeout

    @request_timeout.setter
    def request_timeout(self, request_timeout: Optional[int]):
        self._request_timeout = request_timeout

    @property
    def namespace(self) -> Optional[str]:
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self._namespace = namespace

    @abstractmethod
    def to_payload(self) -> JSON_TYPE:
        raise NacosRequestException('to_payload is abstract method,not implemented.')


class NacosConfiguration(NacosBaseRequest, ABC):
    #  do nothing for expand
    pass


class NacosPostConfiguration(NacosConfiguration):
    """
    发布配置
    发布 Nacos 上的配置。

    请求类型
    POST

    请求 URL
    /nacos/v1/cs/configs

    请求参数
    名称	类型	是否必须	描述
    tenant	string	否	租户信息，对应 Nacos 的命名空间ID字段
    dataId	string	是	配置 ID
    group	string	是	配置分组
    content	string	是	配置内容
    type	String	否	配置类型
    """

    def __init__(self,
                 data_id: str,
                 group: str,
                 content: str,
                 appName: Optional[str] = None,
                 tenant: Optional[str] = None,
                 type: Optional[str] = None):
        super(NacosPostConfiguration, self).__init__(NACOS_CONFIG, RequestMethods.POST)
        self._tenant = tenant
        self._data_id = data_id
        self._group = group
        self._content = content
        self._appName = appName
        self._type = type

    def to_payload(self) -> JSON_TYPE:
        payload = {"dataId": self._data_id, "group": self._group, "content": self._content,
                   'tenant': self._tenant if self._tenant else self.namespace}
        if self._type:
            payload['type'] = self._type
        if self._appName:
            payload['appName'] = self._appName
        return payload


class NacosGetConfiguration(NacosConfiguration):
    """
    描述
    获取Nacos上的配置。

    请求类型
    GET

    请求URL
    /nacos/v1/cs/configs

    请求参数
    名称	类型	是否必须	描述
    tenant	string	否	租户信息，对应 Nacos 的命名空间ID字段。
    dataId	string	是	配置 ID。
    group	string	是	配置分组。
    """

    def __init__(self,
                 data_id: str,
                 group: str,
                 tenant: Optional[str] = None, ):
        super(NacosGetConfiguration, self).__init__(NACOS_CONFIG, RequestMethods.GET)
        self._tenant = tenant
        self._data_id = data_id
        self._group = group

    def to_payload(self) -> JSON_TYPE:
        payload = {"dataId": self._data_id, "group": self._group,
                   'tenant': self._tenant if self._tenant else self.namespace}
        return payload


# Nacos Service

class NacosService(NacosBaseRequest, ABC):
    pass


# ResponseErrorCode

class ResponseErrorCode(object):
    def __init__(self, code, desc, meaning):
        self._code = code
        self._desc = desc
        self._meaning = meaning

    @property
    def code(self) -> int:
        return self._code
