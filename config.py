# -*- coding:utf-8 -*-
import psutil

workers = psutil.cpu_count() * 2 + 1
bind = "0.0.0.0:8000"

DEBUG = True

reload = DEBUG
