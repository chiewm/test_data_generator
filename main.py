# @time    : 2017/12/13 21:10
# @Author  : chiew
# @File    : main.py

import random
import ip_address
import goods
import operation
import users
import requests
import time


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
        op = operation.get_op()
        if n % 2:
            good = goods.get_good("goods2")
            print(ip + ' ' + ' ' + ' ' + op + ' ' + good + ' ' + '1')
        else:
            good = goods.get_good("goods1")
            print(ip + ' ' + ' ' + ' ' + op + ' ' + good + ' ' + '1')

        # user = users.get_user(100, n)


        # url = "http://localhost:52587/Home/Create"
        # headers = {'X-Forwarded-For': ip}
        # params = {'Operation': op, 'Good': good, 'Sex': "true"}
        #
        # html = requests.post(url, headers=headers, params=params)
        # print(html)
        # # print(ip + ' ' + user + ' ' + ' ' + op + ' ' + good
        # time.sleep(1 / (n + 1))
        i = i + 1


get_data()
