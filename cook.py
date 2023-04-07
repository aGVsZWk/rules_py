# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2023/4/7 4:59 PM
# @File    : cook.py
"""
1. 输入想吃的东西+原材料，输出做饭的步骤
2. 输入原材料，输出所有可以制作的东西及步骤
"""
from durable.lang import *
subjects = ["主食", "炒菜", "饮品", "甜品", "油炸食品", "冷冻品"]


class Base(object):
    name = None


class BaseTime(object):
    val = None      # 值
    unit = None     # 单位


class Utensil(Base):    # 炊具
    def __init__(self):
        self.is_container = None    # 是否是容器，锅碗瓢盆


class Ingredient(Base):  # 食材
    def __init__(self):
        self.is_has_skin = None     # 是否有皮


class Condiment(Base):   # 调味品
    def __init__(self):
        self.brand = None    # 品牌


class Action(Base):
    def __init__(self):
        self.action = None  # 煎炒炖炸烤，混合，搅拌


class Step(Base):
    def __init__(self, no, cost):
        self.no = no
        self.cost = cost


class Result(Base):
    def __init__(self):
        pass


class RuleEngine(object):
    def __init__(self, rule_name):
        if not rule_name:
            raise ValueError("rule_name is empty")
        self.rule_name = rule_name

    def get_result(self, data):
        if not data:
            raise ValueError("data is empty")
        output = None
        for _ in range(3):
            output = post(self.rule_name, data)
            if output is not None:
                break
        if output is None:
            print("get_result return None:{}".format(data))
        return output


with ruleset('animal'):
    @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'),
              (m.predicate == 'lives') & (m.object == 'water') & (m.subject == c.first.subject))
    def frog(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': 'is', 'object': 'frog' })

    @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'),
              (m.predicate == 'lives') & (m.object == 'land') & (m.subject == c.first.subject))
    def chameleon(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': 'is', 'object': 'chameleon' })

    @when_all((m.predicate == 'eats') & (m.object == 'worms'))
    def bird(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'bird' })

    @when_all((m.predicate == 'is') & (m.object == 'frog'))
    def green(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'green' })

    @when_all((m.predicate == 'is') & (m.object == 'chameleon'))
    def grey(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'grey' })

    @when_all((m.predicate == 'is') & (m.object == 'bird'))
    def black(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'black' })

    @when_all(+m.subject)
    def output2(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))



# assert_fact('animal', { 'subject': 'Kermit', 'predicate': 'eats', 'object': 'flies' })
# assert_fact('animal', { 'subject': 'Kermit', 'predicate': 'lives', 'object': 'water' })
# assert_fact('animal', { 'subject': 'Greedy', 'predicate': 'eats', 'object': 'flies' })
# assert_fact('animal', { 'subject': 'Greedy', 'predicate': 'lives', 'object': 'land' })
# assert_fact('animal', { 'subject': 'Tweety', 'predicate': 'eats', 'object': 'worms' })


with ruleset("attitude"):
    @when_all(
        (m.age < 30)
        & ((m.salary > 10000) | (m.appearance == "good")) & ((m.job == "teacher") | (m.job == "manong"))
    )
    def like(c):
        c.s.result = {
            'attitude_res': 'like',
        }


    @when_all(
        (m.age < 30)
        & ((m.salary <= 10000) | (m.appearance == "medium")) & ((m.job == "teacher") | (m.job == "manong"))
    )
    def yiban(c):
        c.s.result = {
            'attitude_res': 'yiban',
        }


    @when_all(+m._age)
    def other(c):
        c.s.result = {
            'attitude_res': 'dislike'
        }


attitude_rule = RuleEngine('attitude')
person1 = {"name": "zhangsan", "age": 25, "job": "teacher", "salary": 2000, "appearance": "good"}
attitude_res = attitude_rule.get_result(person1)
print(attitude_res)
person1.update(attitude_res)
print(person1)

print(get_host())
