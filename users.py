# @time    : 2017/12/13 20:52
# @Author  : chiew
# @File    : users.py


def user_generator(size):
    username = "user"
    users = []
    for i in range(size):
        users.append(username + str(i))
    return users


def get_user(size, num):
    users = user_generator(size)
    return users[num]
