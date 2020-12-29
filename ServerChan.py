#!/usr/bin/python3

import requests
import configparser


# 推送Server酱
def ServerChanDlt(redAndBlue, week):
    config = configparser.ConfigParser()
    config.read('config.ini')
    key = config.get('ServerChan', 'key')
    url = f'http://sc.ftqq.com/{key}.send'
    data = {'text': week, 'desp': redAndBlue}
    res = requests.post(url=url, data=data)
    return res.json()


# if __name__ == '__main__':
#     res = ServerChanDlt('123456', '大乐透123期')
#     print(res)
