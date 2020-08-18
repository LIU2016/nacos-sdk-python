# -*- coding:utf-8 -*-

"""
 Author: helixcs
 Site: https://zeit.fun
 File: nacos_base.py.py
 Time: 2020/8/17
 Reference at:https://nacos.io/zh-cn/docs/open-api.html
"""
from abc import abstractmethod, ABC
from typing import Optional
from nacos.exception import NacosRequestException
from enum import Enum

NACOS_CONFIG = "/nacos/v1/cs/configs"

JSON_TYPE = dict


class RequestMethods(Enum):
  GET = "GET"
  POST = "POST"
  PUT = "PUT"
  HEAD = "HEAD"
  DELETE = "DELETE"
  OPTIONS = "OPTIONS"


class NacosBaseRequest(object):
  __slots__ = ['_api_name', '_request_method']

  def __init__(self,
      api_name: Optional[str],
      request_method: RequestMethods = RequestMethods.GET):
    self._api_name = api_name
    self._request_method = request_method

  @property
  def api_name(self) -> Optional[str]:
    return self._api_name

  @property
  def request_method(self) -> RequestMethods:
    return self._request_method

  @abstractmethod
  def request(self) -> str:
    raise NacosRequestException('request is abstract method,not implemented.')


# todo
class NacosConfiguration(NacosBaseRequest, ABC):
  pass


class NacosGetConfiguration(NacosConfiguration):

  def __init__(self, tenant: Optional[str], data_id: str, group: str):
    super().__init__(NACOS_CONFIG, RequestMethods.GET)
    # 租户信息，对应 Nacos 的命名空间ID字段
    self._tenant = tenant
    # 配置 ID
    self._data_id = data_id
    # 配置分组
    self._group = group

  # ...
  def request(self) -> str:
    pass


class NacosService(NacosBaseRequest):
  pass
