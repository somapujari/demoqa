from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Register:
    first_name_id_input = 'firstname'
    last_name_id_input = 'lastname'
    user_name_id_input = 'userName'
    password_id_input = 'password'
    robot_box_id = 'recaptcha-anchor'
    robot_box_frame_xpath = '//iframe[@title="reCAPTCHA"]'  # Xpath to identify the reCAPTCHA iframe
    robot_box_checkbox_xpath = '//div[@class="recaptcha-checkbox-border"]'  # Xpath to identify the reCAPTCHA checkbox
    register_btn_id = 'register'

    def __init__(self, driver):
        self.driver = driver

    def first_name_enter(self, first_name):
        self.driver.find_element(By.ID, self.first_name_id_input).clear()
        self.driver.find_element(By.ID, self.first_name_id_input).send_keys(first_name)

    def last_name_enter(self, last_name):
        self.driver.find_element(By.ID, self.last_name_id_input).clear()
        self.driver.find_element(By.ID, self.last_name_id_input).send_keys(last_name)

    def user_name_enter(self, username):
        self.driver.find_element(By.ID, self.user_name_id_input).clear()
        self.driver.find_element(By.ID, self.user_name_id_input).send_keys(username)

    def password_enter(self, password):
        self.driver.find_element(By.ID, self.password_id_input).clear()
        self.driver.find_element(By.ID, self.password_id_input).send_keys(password)

    def click_on_robot(self):
        # self.driver.find_element(By.ID, self.robot_box_id).click()
        try:
            # Switch to the reCAPTCHA iframe
            iframe = WebDriverWait(self.driver, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.XPATH, self.robot_box_frame_xpath))
            )
            print("Switched to the reCAPTCHA iframe.")

            # Wait for the reCAPTCHA checkbox to be clickable
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.robot_box_checkbox_xpath))
            )
            print("reCAPTCHA checkbox is clickable.")

            # Click the checkbox using JavaScript
            self.driver.execute_script("arguments[0].click();", checkbox)
            print("Clicked the reCAPTCHA checkbox using JavaScript.")

            # Switch back to the main content
            self.driver.switch_to.default_content()
            print("Switched back to the main content.")

        except Exception as e:
            print(f"Failed to click on reCAPTCHA: {e}")

    def click_on_register(self):
        self.driver.find_element(By.ID, self.register_btn_id).click()

    def click_ok_register(self):
        try:
            self.driver.switch_to.frame.accept()
        except Exception as e:
            print('register not completed ', e)
