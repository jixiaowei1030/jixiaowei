import datetime
import os

from loguru import logger


class SelfLog:
    def __new__(cls, *args, **kwargs):
        root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目的根目录
        log_path = os.path.join(root_path, 'logs')
        filename = os.path.join(log_path, '{}.log'.format(datetime.date.today()))  # 设置日志文件名字，按照时间格式譬如2022-10-10.log命名
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        if not os.path.exists(filename):
            with open(filename, mode='w', encoding='utf-8') as ff:
                print(f"日志文件{ff.name}创建成功！")
        logger.add(sink=filename,
                   format='{time:YYYY-MM-DD hh:mm:ss} | {level} | {file}:{function}:{line} - {message}',
                   rotation='00:00',
                   encoding='utf-8',
                   retention='15 days',
                   compression='zip',
                   enqueue=True)  # 每天0点的时候新建日志文件，保留15天，压缩的形式
        return logger


log = SelfLog()
