# @time    : 2017/12/13 20:52
# @Author  : chiew
# @File    : users.py

import random


def user_generator():
    username = "user"
    users = []
    for i in range(100):
        users.append(username + str(i))
    return users


def get_random_user(num):
    users = user_generator()
    return users[num]

