# @time    : 2017/12/13 15:26
# @Author  : chiew
# @File    : ip_address.py

import requests
import random


def get_ip_address():
    url = "http://ipblock.chacuo.net/down/t_txt=c_CN"
    response = requests.get(url)
    content = response.text
    return content


def split_ip_address(ip_list):
    ips = []
    ip_group = ip_list.split('\n')
    for ip in ip_group:
        ips.append(ip.split('\t')[0])
    return ips[1:-1]


def get_random_ip(ips):
    num = random.randint(0, 99)
    return num, ips[num]

