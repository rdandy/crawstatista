# -*- coding:utf-8 -*-
import random
import re

from lxml import etree

import requests

from .browsers import BROWSERS, XPATH_REVENUE, XPATH_REVENUE_YOY, XPATH_ARPC, XPATH_ARPC_YOY, XPATH_HIGHLIGHT_LI,\
    XPATH_USERS, XPATH_USERS_YOY


class Crawler(object):
    # selector = None

    def __init__(self, url):
        headers = {'user-agent': random.choice(BROWSERS)}
        r = requests.get(url, headers=headers)
        self.s = etree.HTML(r.content)

    def revenue(self):
        l = self.s.xpath(XPATH_REVENUE)
        if len(l) > 0:
            return re.sub("\D", "", l[0].text.strip())
        return None

    def revenue_yoy(self):
        l = self.s.xpath(XPATH_REVENUE_YOY)
        if len(l) > 0 and "%" in l[0].text:
            return l[0].text.split("%")[0].strip()
        return None

    def arpc(self):
        l = self.s.xpath(XPATH_ARPC)
        if len(l) > 0 and l[0].text is not None and "$" in l[0].text:
            return l[0].text.split("$")[1].strip()
        return None

    def arpc_yoy(self):
        l = self.s.xpath(XPATH_ARPC_YOY)
        if len(l) > 0 and l[0].text is not None and "%" in l[0].text:
            return l[0].text.split('%')[0].strip()
        return None

    def cagr(self):
        value = None
        lis = self.s.xpath(XPATH_HIGHLIGHT_LI)
        for li in lis:
            c = " ".join(li.text.strip().lower().split(" "))
            if "cagr" in c and "%" in c:
                value = c.split("%")[0].split(" ")[-1]
                break
        return value

    def user_penetration(self):
        value = None
        lis = self.s.xpath(XPATH_HIGHLIGHT_LI)
        for li in lis:
            c = " ".join(li.text.strip().lower().split(" "))
            if "user penetration will be" in c and "%" in c:
                value = c.split("%")[0].split(" ")[-1]
                break
        return value

    def arpu(self):
        value = None
        lis = self.s.xpath(XPATH_HIGHLIGHT_LI)
        for li in lis:
            c = " ".join(li.text.strip().lower().split(" "))
            if "arpu" in c and "$" in c:
                value = c.split("$")[1].strip()
                if "." in value:
                    value = value.rsplit(".", 1)[0].strip()
                break
        return value

    def users(self):
        l = self.s.xpath(XPATH_USERS)
        if len(l) > 0 and l[0].text is not None and "m" in l[0].text.lower():
            return l[0].text.lower().split("m")[0].replace(",", "").strip()
        return None

    def users_yoy(self):
        l = self.s.xpath(XPATH_USERS_YOY)
        if len(l) > 0 and l[0].text is not None and "%" in l[0].text:
            return l[0].text.split('%')[0].strip()
        return None

    def data(self):
        return {
            "revenue": self.revenue(),
            "revenue_yoy": self.revenue_yoy(),
            "arpc": self.arpc(),
            "arpc_yoy": self.arpc_yoy(),
            "cagr": self.cagr(),
            "user_penetration": self.user_penetration(),
            "arpu": self.arpu(),
            "users": self.users(),
            "users_yoy": self.users_yoy()
        }
