# @time    : 2017/12/13 15:26
# @Author  : chiew
# @File    : get_ip_address.py

import requests
import random


def get_ip_address():
    url = "http://ipblock.chacuo.net/down/t_txt=c_CN"
    response = requests.get(url)
    content = response.text
    return content


def split_ip_address():
    ips = []
    ip_list = get_ip_address()
    ip_group = ip_list.split('\n')
    for ip in ip_group:
        ips.append(ip.split('\t')[0])
    return ips[1:-1]


def get_random_ip():
    ips = split_ip_address()
    num = random.randint(0, len(ips))
    return ips[num]

