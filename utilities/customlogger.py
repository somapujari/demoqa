import logging


class Loggen:

    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        file = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\demoqa\logs\demoqalog.log')
        format = logging.Formatter('  %(message)s, %(asctime)s, %(funcName)s, %(levelname)s : %(levelno)s')
        file.setFormatter(format)
        logger.addHandler(file)
        return logger
