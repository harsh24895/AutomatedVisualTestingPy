from selenium.webdriver.common.by import By

from test.chap5.conftest import validate_window
#i will comment below if we want to run the code on line 12 name with region just uncomment it and declare the method name in confest file
#from test.chap7.conftest import validate_element
from test.chap7.conftest import validate_frame


#Here we need to remove the tag parameter but it throws the error or need to add it as we are declaring it in the mehtod


def test_book_by_region(driver, eyes):
    element = driver.find_element(By.ID,'pid3')
    validate_element(driver,eyes,element)


def test_element_in_frame(driver, eyes):
    frame = driver.find_element(By.TAG_NAME, 'iframe')
    validate_frame(driver,eyes,frame,(By.ID,'tinymce'))