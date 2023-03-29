import logging
import os
import time

log_path = "D:\\Python\\Python36\\demo"
class Log:
    # def __init__(self):
    #     # 文件的命名
    #     # self.logname = os.path.join(log_path, '%s.log'%time.strftime('%Y_%m_%d'))
    #     self.log = logging.getLogger('测试')
    #     self.log.setLevel(logging.DEBUG)
    #     # 日志输出格式
    #     self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')

    # def __console(self, level, message):
    #     # 创建一个FileHandler，用于写到本地
    #     fh = logging.FileHandler('test', 'a')  # 追加模式
    #     fh.setLevel(logging.DEBUG)
    #     fh.setFormatter(self.formatter)
    #     self.log.addHandler(fh)
    #
    #     # 创建一个StreamHandler,用于输出到控制台
    #     ch = logging.StreamHandler()
    #     ch.setLevel(logging.DEBUG)
    #     ch.setFormatter(self.formatter)
    #     self.log.addHandler(ch)
    #
    #     if level == 'info':
    #         self.log.info(message)
    #     elif level == 'debug':
    #         self.log.debug(message)
    #     elif level == 'warning':
    #         self.log.warning(message)
    #     elif level == 'error':
    #         self.log.error(message)
    #     # 这两行代码是为了避免日志输出重复问题
    #     # self.log.removeHandler(ch)
    #     # self.log.removeHandler(fh)
    #     # 关闭打开的文件
    #     fh.close()
    #
    # def debug(self, message):
    #     self.__console('debug', message)
    #
    # def info(self, message):
    #     self.__console('info', message)
    #
    # def warning(self, message):
    #     self.__console('warning', message)
    #
    # def error(self, message):
    #     self.__console('error', message)

    def __init__(self):
        self.logname = os.path.join(log_path, 'test.log')
        self.logger = logging.getLogger('测试')
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')



    def __console(self, level, message):
        if not self.logger.handlers:
            self.fh = logging.FileHandler(self.logname)
            self.fh.setLevel(logging.DEBUG)
            self.fh.setFormatter(self.formatter)
            self.logger.addHandler(self.fh)

            self.ch = logging.StreamHandler()
            self.ch.setLevel(logging.DEBUG)
            self.ch.setFormatter(self.formatter)
            self.logger.addHandler(self.ch)
        if level == 'info':
            self.logger.info(message)


    def info(self, message):
        self.__console('info', message)
