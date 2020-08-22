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
from urllib.error import HTTPError, URLError
from ..client import NacosClient, logger
from .nacos_base import NacosBaseRequest, RequestMethods


class NacosProxyClient(NacosClient):
    def __init__(self, *args, **kwargs):
        super(NacosProxyClient, self).__init__(*args, **kwargs)

    # todo多构造
    def tmp(self):
        pass

    def _do_sync_req_proxy(self, request: NacosBaseRequest) -> Optional[str]:
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
            if e.code == HTTPStatus.NOT_FOUND:
                NOT_FOUND_TEMPLATE = \
                    "[{tag}-{method_type}/{api_name}] {tag_name} not found for namespace:{namespace},params={payload}".format(
                        tag=request.tag(),
                        tag_name=request.tag(),
                        method_type=request.request_method,
                        api_name=request.request_api_name,
                        namespace=request.namespace,
                        payload=params
                    )
                # todo check snapshot
                if request.tag() == 'CONFIGURATION':
                    NOT_FOUND_TEMPLATE += ", try to delete snapshot"
                logger.warning(NOT_FOUND_TEMPLATE)
                # delete_file(self.snapshot_base, cache_key)
                return None
            elif e.code == HTTPStatus.CONFLICT:
                CONFLICT_TEMPLATE = \
                    "[{tag}-{method_type}/{api_name}] {tag_name} not found for namespace:{namespace},params={payload}".format(
                        tag=request.tag(),
                        tag_name=request.tag(),
                        method_type=request.request_method,
                        api_name=request.request_api_name,
                        namespace=request.namespace,
                        payload=params
                    )
                logger.error(
                    "[get-config] config being modified concurrently for data_id:%s, group:%s, namespace:%s" % (
                        data_id, group, self.namespace))
            elif e.code == HTTPStatus.FORBIDDEN:
                logger.error("[get-config] no right for data_id:%s, group:%s, namespace:%s" % (
                    data_id, group, self.namespace))
                raise NacosException("Insufficient privilege.")
            else:
                logger.error("[get-config] error code [:%s] for data_id:%s, group:%s, namespace:%s" % (
                    e.code, data_id, group, self.namespace))
                if no_snapshot:
                    raise
            # todo snapshot handle
            pass
        except Exception as ex:
            raise ex

    def _do_pulling_proxy(self, ):
        pass
