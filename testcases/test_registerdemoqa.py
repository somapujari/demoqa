from selenium import webdriver
from pajeobjects.register import Register
import time


class Test_Register:
    url = 'https://demoqa.com/register'
    first_name = 'soma'
    last_name = 'pujari'
    username = 'soma123'
    password = 'Soma@1234'

    def test_register(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.re = Register(self.driver)
        self.re.first_name_enter(self.first_name)
        self.re.last_name_enter(self.last_name)
        self.re.user_name_enter(self.username)
        self.re.password_enter(self.password)
        self.re.click_on_robot()
        self.re.click_on_register()
        self.re.click_ok_register()
        time.sleep(5)
        self.driver.quit()
