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


class TestClient(unittest.TestCase):
    def test_nacos_server(self):
        nacos_server = nacos.NacosServer(SERVER_HOST, SERVER_PORT)
        self.assertEqual(SERVER_HOST, nacos_server.host)
        self.assertEqual(SERVER_PORT, nacos_server.port)

        nacos_server = nacos.NacosServer.uri(SERVER_URI)
        self.assertEqual(SERVER_HOST, nacos_server.host)
        self.assertEqual(SERVER_PORT, nacos_server.port)
