# @time    : 2017/12/14 12:05
# @Author  : chiew
# @File    : training_data.py


import random
import ip_address
import goods
import operation
import time
import requests


def get_ip():
    content = ip_address.get_ip_address()
    ips = ip_address.split_ip_address(content)
    return ips


def get_training_data(size, n_range):
    # 45% 女性，50% 男性，5% 噪点
    # woman_num = size * 0.45
    # man_num = size * 0.95
    i = 0
    ips = get_ip()
    while i < size:
        n = random.randint(0, n_range - 1)
        ip = ips[n]
        # user = users.get_user(size, n)
        op = operation.get_op()

        if n % 2:
            good = goods.get_good("goods1")
            sex = "false"
            # print(ip + ' ' + ' ' + ' ' + op + ' ' + good + ' ' + 'false')

        else:
            # sex = random.randint(0, 1)
            good = goods.get_good("goods2")
            sex = "true"
            # print(ip + ' ' + ' ' + ' ' + op + ' ' + good + ' ' + 'true')

        url = "http://localhost:52587/Home/Create"
        headers = {'X-Forwarded-For': ip}
        params = {'Operation': op, 'Good': good, 'Sex': sex}

        html = requests.post(url, headers=headers, params=params)
        print(html)
        # print(ip + ' ' + user + ' ' + ' ' + op + ' ' + good
        # time.sleep(1 / (n + 1))
        i = i + 1

print(get_training_data(5000, 500))  # 5000次操作,500名用户
