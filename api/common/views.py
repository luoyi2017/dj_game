#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from utils.captcha.xtcaptcha import Captcha
from django.core.cache import cache
from PIL import Image
try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

def captcha(request):
    text,image = Captcha.gene_code()
    # image.save('text.png','png') # I/0
    #需要通过StringIO这个类来把图片当成流的形式返回给客户端
    out = StringIO() #获取"管道"
    image.save(out,'png') #把图片保存到管道中
    out.seek(0) #移动文件指针到\第0个位置
    response = HttpResponse(content_type='image/png')
    response.write(out.read())
    return response