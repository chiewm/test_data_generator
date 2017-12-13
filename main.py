# @time    : 2017/12/13 21:10
# @Author  : chiew
# @File    : main.py

import threading
from time import ctime, sleep
import ip_address
import goods
import operation
import users

i = 0
content = ip_address.get_ip_address()
ips = ip_address.split_ip_address(content)

while i < 1000:
    num = ip_address.get_random_ip(ips)[0]
    ip = ip_address.get_random_ip(ips)[1]
    user = users.get_random_user(num)
    op = operation.get_op()
    good = goods.get_good()
    print(ip + ' ' + user + ' ' + ' ' + op + ' ' + good)
    i = i + 1

