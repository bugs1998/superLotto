import time
import schedule
from superLotto import superLottoRun
import logging

# 每周1、3、6执行Dtl
schedule.every().monday.at('21:00').do(superLottoRun)
schedule.every().wednesday.at('22:03').do(superLottoRun)
schedule.every().saturday.at('21:00').do(superLottoRun)
schedule.every().thursday.at('17:27').do(superLottoRun)


class LoggerFactory:
    def __init__(self, name=__name__):
        """
        实例化LoggerFactory类时的构造函数
        :param name:
        """
        # 实例化logging
        self.logger = logging.getLogger(name)
        # 输出的日志格式
        self.formatter = formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def create_logger(self):
        """
        构造一个日志对象
        :return:
        """
        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志输出的文件
        handle = logging.FileHandler('run.log')
        # 输出到日志文件的日志级别
        handle.setLevel(logging.INFO)
        handle.setFormatter(self.formatter)
        self.logger.addHandler(handle)
        # 输出到控制台的显示信息
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        console.setFormatter(self.formatter)
        self.logger.addHandler(console)


if __name__ == '__main__':
    factory = LoggerFactory('Test_Main')
    factory.logger.info("项目启动")

while True:
    schedule.run_pending()
    time.sleep(1)
