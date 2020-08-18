# -*- coding:utf-8 -*-

"""
 Author: helixcs
 Site: https://zeit.fun
 File: nacos_base.py.py
 Time: 2020/8/17
 Reference at:https://nacos.io/zh-cn/docs/open-api.html
"""

from typing import Optional
from enum import Enum

NACOS_CONFIG = "/nacos/v1/cs/configs"


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


# todo
class NacosConfiguration(NacosBaseRequest):
  pass


class NacosService(NacosBaseRequest):
  pass
