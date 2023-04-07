# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2023/3/27 5:02 PM
# @File    : test_durable.py
from durable.lang import *

with ruleset("test"):
    @when_all(m.subject == "World")
    def say_hello(c):
        print("Hello {0}".format(c.m.subject))

post("test", {"subject": "World"})
