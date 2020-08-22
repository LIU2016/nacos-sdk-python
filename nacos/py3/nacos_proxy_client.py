# -*- coding=utf-8 -*-

"""
 Verion: 1.0
 Since : 3.6
 Author: zhangjian
 Site: https://github.com/xarrow/
 File: nacos_proxy_client.py
 Time: 2020/8/22
 
 Add New Functional nacos-sdk-python
"""
from urllib.error import HTTPError, URLError
from ..client import NacosClient, logger
from .nacos_base import NacosBaseRequest, RequestMethods


class NacosProxyClient(NacosClient):
    def __init__(self, *args, **kwargs):
        super(NacosProxyClient, self).__init__(*args, **kwargs)

    # todo多构造
    def tmp(self):
        pass

    def _do_sync_req_proxy(self, request: NacosBaseRequest):
        # public fields padding
        # 租户信息，对应 Nacos 的命名空间ID字段
        if not request.namespace:
            request.namespace = self.namespace
        uri = request.request_api_name
        headers = request.request_headers if request.request_headers is not None else {}
        params = request.to_payload()
        data = None
        timeout = request.request_timeout if request.request_timeout is not None else 1000
        method = request.request_method.value if request.request_method is not None else RequestMethods.GET

        # invoker
        try:
            response = super()._do_sync_req(url=uri,
                                            headers=headers,
                                            params=params,
                                            data=data,
                                            timeout=timeout,
                                            method=method)
            return response
        except HTTPError as error:

            # todo snapshot handle
            pass
        except Exception as ex:
            pass

    def _do_pulling_proxy(self, ):
        pass
