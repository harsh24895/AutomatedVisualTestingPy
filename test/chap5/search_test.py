from assertpy import assert_that
from time import sleep

from page_objects.search_page import SearchPage
from test.chap5.conftest import validate_window


def test_filter_book(eyes, driver):
    page = SearchPage(driver)
    page.filter_books('Agile')
    #sleep(5)
    # result = page.verify_visible_books_by_title('Agile Testing')
    # assert_that(result).is_equal_to(True)

    #tag is the way to specific unique name for the assertion so that we can visualize in the applitools dashboard
    validate_window(driver,eyes,tag='filter_text')