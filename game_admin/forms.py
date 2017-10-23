#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from utils.captcha.xtcaptcha import Captcha
import json

class LoginForm(forms.Form):
    username = forms.CharField(max_length=10,min_length=4)
    password = forms.CharField(max_length=20,min_length=6)
    captcha = forms.CharField(max_length=4, min_length=4)
    remember = forms.BooleanField(required=False)  # 用户有可能不需要记住我,那么这个参数有可能就没有

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha',None)
        if not Captcha.check_captcha(captcha):
            raise forms.ValidationError(u'验证码错误!')
        return captcha

    def get_error(self):
        # 转换成json字符串类型
        errors = self.errors.as_json()
        # 转换成字典类型
        error_dict = json.loads(errors)
        message = ''
        # 只取字典中的第一个值
        # {u'captcha': [{u'message': u'xxx', u'code': u''}]}
        for k, v in error_dict.items():
            message = v[0].get('message', None)
        return message