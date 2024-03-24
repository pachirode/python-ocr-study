import logging
import time


class OCRLogging:
    @staticmethod
    def start(level=logging.INFO,
              log_format='%(asctime)s %(message)s',
              date_format='%y-%m-%d %H:%M:%S'):
        logging.Formatter.converter = time.gmtime
        logger = logging.getLogger('OCR')
        for h in logger.handlers:
            if isinstance(h, logging.StreamHandler):
                logger.handlers.remove(h)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(log_format, datefmt=date_format)
        handler.setFormatter(formatter)
        logger.setLevel(level)
        logger.addHandler(handler)

        return logger

    @staticmethod
    def logger():
        return logging.getLogger('OCR')
