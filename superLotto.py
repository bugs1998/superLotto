#!/usr/bin/python3
import logging

import ServerChan
import requests
from bs4 import BeautifulSoup

logFile = open("run.log", encoding="utf-8", mode="a")
logging.basicConfig(stream=logFile, format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.INFO)


def superLottoRun():
    logging.info('进入方法')
    target = 'https://kaijiang.500.com/dlt.shtml'
    text = requests.get(url=target)
    html = BeautifulSoup(text.text, features='lxml')
    br = html.find_all('li', {'class': 'ball_red'})
    texts = ''
    week = ''

    # 处理红区
    for inx, val in enumerate(br):
        if inx < len(br) - 1:
            texts += val.text.replace('\xa0' * 8, ',') + '|'
        else:
            texts += val.text.replace('\xa0' * 8, ',') + ' '

    # 处理蓝区
    bb = html.find_all('li', {'class': 'ball_blue'})
    for inx, val in enumerate(bb):
        if inx < len(bb) - 1:
            texts += val.text.replace('\xa0' * 8, ',') + '|'
        else:
            texts += val.text.replace('\xa0' * 8, ',')
    print(texts)
    # 获取当前期
    bs = html.find_all('font', {'class': 'cfont2'})
    for i in bs:
        week = i.text.replace('\xa0' * 8, ',')
    week = '大乐透第' + week + '期'

    # 推送微信
    ServerChan.ServerChanDlt(texts, week)

# if __name__ == '__main__':
#     superLottoRun()
