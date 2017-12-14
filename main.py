# @time    : 2017/12/13 21:10
# @Author  : chiew
# @File    : main.py

import threading
from time import ctime, sleep
import requests
import random
import ip_address
import goods
import operation
import users


def get_ip():
    content = ip_address.get_ip_address()
    ips = ip_address.split_ip_address(content)
    return ips


def get_data():
    ips = get_ip()
    i = 0
    while i < 5000:
        n = random.randint(0, 99)
        ip = ips[n]
        user = users.get_random_user(n)
        op = operation.get_op()
        good = goods.get_good("goods3")
        print(ip + ' ' + user + ' ' + ' ' + op + ' ' + good)
        # sleep(1 / (num+1))
        i = i + 1


def get_training_data():
    # 45% 女性，50% 男性，5% 噪点
    woman_num = 100 * 0.45
    man_num = 100 * 0.95
    i = 0
    ips = get_ip()
    while i < 100:
        n = random.randint(0, 99)
        ip = ips[n]
        user = users.get_random_user(n)
        op = operation.get_op()

        if n < woman_num:
            good1 = goods.get_good("goods1")
            print(ip + ' ' + user + ' ' + ' ' + op + ' ' + good1 + ' ' + '0')

        elif (n >= woman_num) and (n < man_num):
            good2 = goods.get_good("goods2")
            print(ip + ' ' + user + ' ' + ' ' + op + ' ' + good2 + ' ' + '1')

        else:
            sex = random.randint(0, 1)
            good3 = goods.get_good("goods3")
            print(ip + ' ' + user + ' ' + ' ' + op + ' ' + good3 + ' ' + str(sex))

        i = i + 1


for j in range(100):
    get_training_data()
