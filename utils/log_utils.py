import logging
import configparser
import os
from logging.handlers import RotatingFileHandler


#读取日志配置文件
def init_logger():
    config = configparser.ConfigParser()
    config.read('./config/log_config.ini',encoding='utf-8')
    log_level = config.get('log','level')
    log_path = config.get('log','log_path')
    max_size = int(config.get('log','max_size')) * 1024 * 1024
    backup_count = int(config.get('log','backup_count'))

    #创建日志目录
    os.makedirs(os.path.dirname(log_path),exist_ok=True)
    
    #配置日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    #配置文件处理器
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=max_size,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    #配置控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    #初始化logger
    logger = logging.getLogger('security_scan_tool')
    logger.setLevel(getattr(logging,log_level.upper()))
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

#全局logger实例
logger = init_logger()
