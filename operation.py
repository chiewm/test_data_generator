# @time    : 2017/12/13 21:02
# @Author  : chiew
# @File    : operation.py


import random


def get_op():
    operations = [
        'add',
        'add',
        'add',
        'collect',
        'collect',
        'collect',
        'buy',
        'buy',
        'search',
        'search',
        'search',
        'search',
    ]
    num = random.randint(0, len(operations) - 1)
    return operations[num]
