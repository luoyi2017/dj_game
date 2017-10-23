from django.conf.urls import url,include
import api.common.views as views

urlpatterns = [
    url(r'^captcha/',views.captcha,name='common_captcha'),
]