# @time    : 2017/12/13 20:26
# @Author  : chiew
# @File    : goods.py

import random


def get_good(goods):
    goods1 = ['女鞋', '牙刷', '毛巾', '香水', '口红', '香水', '口红', '女帽', '皮带', '男鞋']
    goods2 = ['男鞋', '牙刷', '毛巾', '烟斗', '男帽', '皮带', '男鞋', '剃须刀', '剃须刀', '口红']
    goods3 = list(set(goods1 + goods2))
    switcher = {
        "goods1": goods1,
        "goods2": goods2,
        "goods3": goods3
    }
    num = random.randint(0, len(goods) - 1)
    return switcher[goods][num]
