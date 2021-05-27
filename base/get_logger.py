import logging.handlers


class GetLogger:
    logger = None

    # 获取 logger
    @classmethod
    def get_logger(cls):
        # 如果 logger为空
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志器默认级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器 控制台
            sh = logging.StreamHandler()
            # 获取处理 文件（时间）
            th = logging.handlers.TimedRotatingFileHandler(filename="./log/tpshop.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            # 获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            # 将格式器 设置 处理器中
            sh.setFormatter(fmt)
            th.setFormatter(fmt)
            # 将处理器 添加到 日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        # 返回 日志器
        return cls.logger
