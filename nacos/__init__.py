from .client import NacosClient, NacosException, DEFAULTS, DEFAULT_GROUP_NAME
#  todo just for test
from .py3.nacos_base import *
from .py3.nacos_loadbalancer import NacosServer, NacosLoadBalancer
from .py3.nacos_proxy_client import *

__version__ = client.VERSION

__all__ = ["NacosClient", "NacosException", "DEFAULTS", DEFAULT_GROUP_NAME, NacosServer, NacosLoadBalancer]
