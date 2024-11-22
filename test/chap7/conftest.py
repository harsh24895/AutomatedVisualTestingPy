import pytest
from applitools.common import MatchLevel
from applitools.selenium import Eyes
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.drivers.chrome import ChromeDriver

from config.base import APPLITOOLS_API_KEY

APP_NAME = 'automation_bookstore'
#Here we are using APP_NAMEE and APP_UNDER_TESTt for another example if need to test on local find then just comment thsi two
APP_NAMEE = 'the-internet'
APP_UNDER_TEST = 'C:/Users/Harsh/Downloads/automated-visual-testing-master/automated-visual-testing-master/website/index.html'
APP_UNDER_TESTt = 'https://the-internet.herokuapp.com/iframe'
@pytest.fixture(scope='function')
def driver():
    #if they throw chrome version error just check the actual chrome version and install the new chromedriver and paste autual C location
    driver = webdriver.Chrome()
    driver.get(APP_UNDER_TESTt)
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

#Ch-6 to set the match level for particular assertions
def validate_window(driver,eyes,tag=None):
    open_eyes(driver,eyes) #MatchLevel.EXACT : this will pixel by pixel comparison with two images and not recommend
    #MatchLevel.content: this will focus on the content
    #Ch-7 this will take the screenshots for the content
    eyes.force_full_page_screenshot = True
    eyes.check_window(tag=tag)
    close_yes(eyes)

#Ch-7 To verify specific region within a frame
def validate_frame(driver,eyes, frame_reference,region,tag=None):
    open_eyes(driver,eyes) #MatchLevel.EXACT : this will pixel by pixel comparison with two images and not recommend
    #MatchLevel.content: this will focus on the content
    eyes.force_full_page_screenshot = True
    eyes.check_region_in_frame(frame_reference,region, tag=tag)
    close_yes(eyes)

def open_eyes(driver,eyes):
    eyes.open(driver,APP_NAMEE,test_name=get_test_name())


def close_yes(eyes):
    eyes.close()


# def validate_window(driver, eyes, tag=None):
#     open_eyes(driver,eyes)
#     eyes.check_window(tag=tag)
#     close_yes(eyes)
