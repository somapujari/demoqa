import configparser

config = configparser.RawConfigParser()
config.read(r'C:\Users\Dell\PycharmProjects\demoqa\config.ini')


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get('common info', 'rurl')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'password')
        return password