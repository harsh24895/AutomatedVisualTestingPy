from unittest import TestCase
from selenium import webdriver

from applitools.selenium import Eyes
from config.base import APPLITOOLS_API_KEY


class BaseTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.initialize_eyes()
        self.driver.get('https://applitools.com/helloworld')

    def tearDown(self):
        self.driver.quit()

    def initialize_eyes(self):
        self.eyes = Eyes()
        self.eyes.api_keys = APPLITOOLS_API_KEY

        return self.eyes