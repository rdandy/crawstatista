# -*- coding:utf-8 -*-
import psutil


class Config(object):
    workers = psutil.cpu_count() * 2 + 1
    bind = "0.0.0.0:8000"


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    reload = DEBUG
