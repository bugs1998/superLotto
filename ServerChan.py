#!/usr/bin/python3
import logging

import requests
import configparser

logFile = open("run.log", encoding="utf-8", mode="a")
logging.basicConfig(stream=logFile, format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)


# 推送Server酱
def ServerChanDlt(redAndBlue, week):
    config = configparser.ConfigParser()
    config.read('config.ini')
    key = config.get('ServerChan', 'key')
    url = f'http://sc.ftqq.com/{key}.send'
    data = {'text': week, 'desp': redAndBlue}
    try:
        res = requests.post(url=url, data=data)
        son = res.json()
        if son['errno'] == 0:
            logging.info('微信推送成功')
        elif son['errno'] == 1024:
            logging.info('微信推送内容重复')
    except TypeError as t:
        logging.error(f'接口调用异常：{t}-{res}')
    except Exception as e:
        logging.error(f'未知异常{e}')

# if __name__ == '__main__':
#     res = ServerChanDlt('123456', '大乐透123期')
#     print(res)
