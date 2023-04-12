# -*- coding: utf-8 -*-
# @Author  : HeLei
# @Time    : 2023/4/7 4:59 PM
# @File    : cook.py
"""
1. 输入想吃的东西+原材料，输出做饭的步骤
2. 输入原材料，输出所有可以制作的东西及步骤
"""
import click
from durable.lang import *

from durable.lang import *

with ruleset('attributes'):
    @when_all(pri(3), m.amount < 300)
    def first_detect(c):
        print('attributes P3 ->{0}'.format(c.m.amount))


    @when_all(pri(2), m.amount < 200)
    def second_detect(c):
        print('attributes P2 ->{0}'.format(c.m.amount))


    @when_all(pri(1), m.amount < 100)
    def third_detect(c):
        print('attributes P1 ->{0}'.format(c.m.amount))

assert_fact('attributes', {'amount': 50})
assert_fact('attributes', {'amount': 150})
assert_fact('attributes', {'amount': 250})



subjects = ["主食", "炒菜", "饮品", "甜品", "油炸食品", "冷冻品"]

with ruleset("土豆"):
    @when_all(m.subject == "酸辣土豆丝" & m.utensil == "菜刀")
    def potato(c):
        click.echo(click.style("去皮土豆用刀切丝", bg="green", fg="red", bold=True, dim=True))
        c.s.state = "step1"


    @when_all(m.subject == "酸辣土豆丝")
    def potato2(c):
        click.echo(click.style("土豆擦丝", bg="green", fg="red", bold=True, dim=True))


    @when_all(m.subject == "炸薯条")
    @to()
    def potato3(c):
        click.echo(click.style("土豆用刀切7~8cm宽", bg="green", fg="red", bold=True, dim=True))


    @when_all(m.subject == "炸薯条")
    def potato4(c):
        click.echo(click.style("土豆用水洗两遍，把淀粉洗掉，再把水沥干", ))

    @when_all(m.subject == "酸辣土豆丝")
    def potato5(c):
        click.echo(click.style("再放点醋防止氧化", ))

    @when_all(m.subject == "酸辣土豆丝")
    def potato6(c):
        click.echo(click.style("锅中水烧开，倒入土豆丝，焯水十秒钟，过凉后倒出，控干水分", bold=True))


with ruleset("青椒"):
    @when_all(m.subject == "酸辣土豆丝")
    def green_pepper(c):
        click.echo(click.style("一个青椒切成丝", ))


with ruleset("葱姜蒜"):
    @when_all(m.subject == "葱")
    def scallion(c):
        click.echo(click.style("适量小葱切成段", ))


    @when_all(m.subject == "姜")
    def gin(c):
        click.echo(click.style("生姜切成片", ))


    @when_all(m.subject == "蒜")
    def graleac(c):
        click.echo(click.style("三个蒜切成片", ))

    @when_all(m.subject == "干辣椒")
    def chillies(c):
        click.echo(click.style("干辣椒放水中泡一下，这样炒的时候不容易糊，而且更加入味", ))


with ruleset("炒"):
    @when_all(m.subject == "酸辣土豆丝")
    def fire(c):
        click.echo(click.style("锅烧热，加油", ))
        click.echo(click.style("油热后下入葱姜蒜 干辣椒，小火炒出香味", ))
        click.echo(click.style("炒出香味后倒入青椒", ))
        click.echo(click.style("然后倒入土豆丝，翻炒均匀", ))

    @when_all(m.subject == "酸辣土豆丝")
    def fire2(c):
        click.echo(click.style("大火烧至十秒钟", ))


with ruleset("调味"):
    @when_all(m.subject == "酸辣土豆丝")
    def season(c):
        click.echo(click.style("加入盐", ))
        click.echo(click.style("白醋", ))


class Base(object):
    name = None


class BaseTime(object):
    val = None  # 值
    unit = None  # 单位


class Utensil(Base):  # 炊具
    def __init__(self):
        self.is_container = None  # 是否是容器，锅碗瓢盆


class Ingredient(Base):  # 食材
    def __init__(self):
        self.is_has_skin = None  # 是否有皮


class Condiment(Base):  # 调味品
    def __init__(self):
        self.brand = None  # 品牌


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
        c.assert_fact({'subject': c.first.subject, 'predicate': 'is', 'object': 'frog'})


    @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'),
              (m.predicate == 'lives') & (m.object == 'land') & (m.subject == c.first.subject))
    def chameleon(c):
        c.assert_fact({'subject': c.first.subject, 'predicate': 'is', 'object': 'chameleon'})


    @when_all((m.predicate == 'eats') & (m.object == 'worms'))
    def bird(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'bird'})


    @when_all((m.predicate == 'is') & (m.object == 'frog'))
    def green(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'green'})


    @when_all((m.predicate == 'is') & (m.object == 'chameleon'))
    def grey(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'grey'})


    @when_all((m.predicate == 'is') & (m.object == 'bird'))
    def black(c):
        c.assert_fact({'subject': c.m.subject, 'predicate': 'is', 'object': 'black'})


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

# attitude_rule = RuleEngine('attitude')
# person1 = {"name": "zhangsan", "age": 25, "job": "teacher", "salary": 2000, "appearance": "good"}
# attitude_res = attitude_rule.get_result(person1)
# print(attitude_res)
# person1.update(attitude_res)
# print(person1)
#
# print(get_host())
