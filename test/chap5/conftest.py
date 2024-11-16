import pytest
from applitools.selenium import Eyes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver

from config.base import APPLITOOLS_API_KEY

APP_NAME = 'automation_bookstore'
APP_UNDER_TEST = 'C:/Users/Harsh/Downloads/automated-visual-testing-master/automated-visual-testing-master/website/index.html'

@pytest.fixture(scope='function')
def driver():
    #if they throw chrome version error just check the autual chrome version and install the new chromedriver and paste autual C location
    driver = webdriver.Chrome()
    driver.get(APP_UNDER_TEST)
    yield driver
    driver.quit()
@pytest.fixture(scope='function')
def eyes():
    eyes = initialize_eyes()
    yield eyes

def initialize_eyes():
    eyes = Eyes()
    eyes.api_key = APPLITOOLS_API_KEY
    return  eyes
def get_test_name():
    import  inspect
    return  inspect.stack()[3].function


def open_eyes(driver,eyes):
    eyes.open(driver,APP_NAME,test_name=get_test_name())


def close_yes(eyes):
    eyes.close()


def validate_window(driver, eyes, tag):
    open_eyes(driver,eyes)
    eyes.check_window(tag=tag)
    close_yes(eyes)
