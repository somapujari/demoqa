import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options


@pytest.fixture
def setup():
    chrome_option = Options()
    chrome_option.binary_location = r'C:\Users\Dell\AppData\Local\Google\Chrome\Application\chrome.exe'
    service = Service(executable_path=r'C:\Users\Dell\AppData\Local\Programs\Python\Python310\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_option)
    yield driver

    driver.delete_all_cookies()
    driver.quit()
    return driver
