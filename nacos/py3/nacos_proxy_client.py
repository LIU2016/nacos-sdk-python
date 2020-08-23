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
from http import HTTPStatus
from typing import Optional
from urllib.error import HTTPError

from .nacos_base import NacosBaseRequest, RequestMethods
from ..client import NacosClient, logger


class NacosProxyClient(NacosClient):
    def __init__(self, *args, **kwargs):
        super(NacosProxyClient, self).__init__(*args, **kwargs)

    # todo多构造
    def tmp(self):
        pass

    def _do_sync_req_proxy(self, request: NacosBaseRequest, exception_callback=None) -> Optional[str]:
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
            return response.read().decode('utf-8')
        except HTTPError as e:
            BASE_LOG_TEMPLATE = \
                """
                [{tag} {method_type} {api_name}] {message_detail} namespace:{namespace},params={payload}.{after_action}
                """
            if e.code == HTTPStatus.NOT_FOUND:
                message_detail = "{tag} not found".format(tag=request.tag()),
            elif e.code == HTTPStatus.CONFLICT:
                message_detail = "{tag} config being modified concurrently for".format(tag=request.tag()),
            elif e.code == HTTPStatus.FORBIDDEN:
                message_detail = "{tag} no right for".format(tag=request.tag()),
            elif e.code == HTTPStatus.INTERNAL_SERVER_ERROR:
                message_detail = "{tag} internal server error for".format(tag=request.tag()),
            else:
                message_detail = "{tag} {error} for".format(tag=request.tag(), error=e.code),
            ERROR_TEMPLATE = BASE_LOG_TEMPLATE.format(
                tag=request.tag(),
                method_type=request.request_method,
                api_name=request.request_api_name,
                message_detail=message_detail,
                namespace=request.namespace,
                payload=params,
                after_action=""
            )
            logger.error(ERROR_TEMPLATE)
            raise e
        except Exception as ex:
            raise ex
        finally:
            exception_callback(request)
            pass

    def _do_pulling_proxy(self, ):
        pass
