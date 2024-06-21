from pajeobjects.logindemoqa import Login
from utilities.readproperty import ReadConfig
from utilities.customlogger import Loggen


class Test_Login:
    rurl = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    expected_url = 'https://demoqa.com/profile'
    logger = Loggen.loggen()

    def test_login(self, setup):
        self.logger.info('* test_login started * ')
        self.driver = setup
        self.logger.info('** opening  url ** ')
        self.driver.get(self.rurl)
        self.driver.implicitly_wait(10)
        self.lg = Login(self.driver)
        self.logger.info(' ** entering username')
        self.lg.username_enter(self.username)
        self.logger.info('** entering password** ')
        self.lg.password_enter(self.password)
        self.logger.info(' ** click on login  button ** ')
        self.lg.login_click()
        self.logger.info('** taking screenshots')
        self.driver.save_screenshot(r'C:\Users\Dell\PycharmProjects\demoqa\screenshots\login.png')
        self.logger.info('** verifying  login ** ')
        self.lg.verify_login(self.expected_url)
        self.logger.info('** test login completed **')

