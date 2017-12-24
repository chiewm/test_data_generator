# @time    : 2017/12/14 22:41
# @Author  : chiew
# @File    : connect.py

import requests

# api_url = "http://ip.taobao.com/service/getIpInfo.php?ip="
for i in range(100):
    url = "http://localhost:52587/Default/Index"
    headers = {'user-agent': 'my-app/0.0.1'}
    params = {'Ip': str(i), 'Operation': str(i), 'Good': str(i)}

    html = requests.post(url, headers=headers, params=params)
