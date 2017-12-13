# @time    : 2017/12/13 20:26
# @Author  : chiew
# @File    : goods.py

import random


def get_good():
    goods = ['男鞋', '女鞋', '牙刷', '毛巾', '香水', '烟斗', '口红', '女士帽子', '男士帽子', '皮带']
    num = random.randint(0, len(goods)-1)
    return goods[num]

