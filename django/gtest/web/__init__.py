# -*- coding: utf-8 -*-
from os import path
from django.apps import AppConfig

# add by chr 20160719
VERBOSE_APP_NAME = u"测试用例集合"

def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]

class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME
default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'
