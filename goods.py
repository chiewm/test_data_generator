# @time    : 2017/12/13 20:26
# @Author  : chiew
# @File    : goods.py

import random


def get_good(goods):
    goods1 = ['女鞋', '牙刷', '毛巾', '香水', '口红', '女士帽子', '皮带']
    goods2 = ['男鞋', '牙刷', '毛巾', '烟斗', '男士帽子', '皮带', '剃须刀']
    goods3 = list(set(goods1 + goods2))
    switcher = {
        "goods1": goods1,
        "goods2": goods2,
        "goods3": goods3
    }
    num = random.randint(0, len(goods)-1)
    return switcher[goods][num]



