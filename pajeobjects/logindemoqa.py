from selenium.webdriver.common.by import By


class Login:
    username_input_id = 'userName'
    password_input_id = 'password'
    login_btn_id = 'login'

    def __init__(self, driver):
        self.driver = driver

    def username_enter(self, username):
        self.driver.find_element(By.ID, self.username_input_id).clear()
        self.driver.find_element(By.ID, self.username_input_id).send_keys(username)

    def password_enter(self, password):
        self.driver.find_element(By.ID, self.password_input_id).clear()
        self.driver.find_element(By.ID, self.password_input_id).send_keys(password)

    def login_click(self):
        self.driver.find_element(By.ID, self.login_btn_id).click()

    def verify_login(self, expected_url):
        url = self.driver.current_url
        print(url)
        try:
            if url == expected_url:
                assert True
            else:
                assert False
        except Exception as e:
            print(e)
