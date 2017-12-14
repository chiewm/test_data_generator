# @time    : 2017/12/14 12:05
# @Author  : chiew
# @File    : training_data.py


import random
import ip_address
import goods
import operation
import users


def get_ip():
    content = ip_address.get_ip_address()
    ips = ip_address.split_ip_address(content)
    return ips


def get_training_data(size, n_range):
    # 45% 女性，50% 男性，5% 噪点
    woman_num = size * 0.45
    man_num = size * 0.95
    i = 0
    ips = get_ip()
    while i < size:
        n = random.randint(0, n_range - 1)
        ip = ips[n]
        user = users.get_user(size, n)
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

print(get_training_data(5000, 100))  # 5000次操作,100名用户
