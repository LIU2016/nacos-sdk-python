# -*- coding=utf-8 -*-

"""
 Verion: 1.0
 Since : 3.6
 Author: zhangjian
 Site: https://github.com/xarrow/
 File: nacos_loadbalancer_test.py
 Time: 2020/8/22
 
 Add New Functional nacos-sdk-python
"""
import unittest
import nacos

SERVER_HOST = "localhost"
SERVER_PORT = 8848
SERVER_URI = SERVER_HOST + ":" + str(SERVER_PORT)
NAMESPACE = ""

# Set the following values if authentication mode is enabled on the server
USERNAME = None
PASSWORD = None


class TestClient(unittest.TestCase):
    def test_nacos_server(self):
        nacos_server = nacos.NacosServer(SERVER_HOST, SERVER_PORT)
        self.assertEqual(SERVER_HOST, nacos_server.host)
        self.assertEqual(SERVER_PORT, nacos_server.port)

        nacos_server = nacos.NacosServer.uri(SERVER_URI)
        self.assertEqual(SERVER_HOST, nacos_server.host)
        self.assertEqual(SERVER_PORT, nacos_server.port)

    def test_nacos_py3_publish_configuration(self):
        client = nacos.NacosProxyClient(server_addresses=SERVER_URI,
                                        namespace=NAMESPACE,
                                        username=USERNAME,
                                        password=PASSWORD)

        client.set_debugging()
        resp = client._do_sync_req_proxy(
            nacos.NacosPostConfiguration(
                # tenant=client.namespace,
                data_id="nacos-python-sdk-py31",
                group="Py3Group",
                content="Py3配置内容测试",
                type="Py3测试Type",
                appName="NacosPython3Sdk"
            ))
        print(resp)

    def test_nacos_py3_get_configuration(self):
        client = nacos.NacosProxyClient(server_addresses=SERVER_URI,
                                        namespace=NAMESPACE,
                                        username=USERNAME,
                                        password=PASSWORD)

        client.set_debugging()
        resp = client._do_sync_req_proxy(
            nacos.NacosGetConfiguration(
                data_id="nacos-python-sdk-py31",
                group="Py3Group"
            ))
        print(resp)
