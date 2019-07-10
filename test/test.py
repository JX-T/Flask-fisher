# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


import os
from flask import Flask, current_app


"""
经典错误：Working outside of application context
此时由于_app_ctx_stack为空，因此current_app所指的核心对象为空
"""


# app = Flask(__name__)

# a = current_app

# d = current_app.config['DEBUG']

# os.path.basename 返回 path 最后的文件名
# print(os.path.basename('vi/statics'))


st_ab = '/gifts/book/9787544247269/'

flag = st_ab.startswith('/')

print(flag)