# -*- coding:utf-8 -*-

"""
 Author: helixcs
 Site: https://zeit.fun
 File: __init__.py.py
 Time: 2020/8/17

 Describe: Just support Python3+
"""
import sys

try:
  assert sys.version_info.major >= 3
except Exception as ex:
  raise AssertionError("nacos py3 module only support 3+ !")
