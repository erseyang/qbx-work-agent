import logging
import os.path

import colorlog

def get_logger(name):
    ## 日志设置
    # 创建一个Logger对象
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    ## 清除掉默认的streamhandler...
    if logger.hasHandlers():
        logger.handlers.clear()

    # 设置文件输出
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), f'{name}.log'), encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(filename)s:%(lineno)d - %(funcName)s() - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    ## 日志输入不同的颜色
    color_formatter = colorlog.ColoredFormatter('%(log_color)s[%(levelname)-8s] %(message)s',
                                                log_colors={
                                                    'DEBUG': 'cyan',
                                                    'INFO': 'green',
                                                    'WARNING': 'yellow',
                                                    'ERROR': 'red',
                                                    'CRITICAL': 'red, bg_white',
                                                })
    console_handler.setFormatter(color_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def get_record_logger(name):
    """
    用于记录一些可以用来作为处理的日志，比如任务的中断后，记录在日志中的内容则表示已经完成
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(os.path.join(os.getcwd(), f'{name}.log'), encoding='utf-8')
    formatter = logging.Formatter(
        '%(message)s')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    return logger

def get_console_logger(name):
    """
    打印出原来的内容
    :param name:
    :return:
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

