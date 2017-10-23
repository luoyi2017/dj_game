#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# No module named 'MySQLdb'的解决办法：
# MySQLdb不支持py3，所以py3环境下用PyMySQL代替，先 pip install PyMySQL；
# 然后在 自己的项目 的__init__.py文件下 输入：
import pymysql
pymysql.install_as_MySQLdb()