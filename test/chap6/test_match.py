from test.chap5.conftest import validate_window

#Here we need to remove the tag parameter but it throws the error or need to add it as we are declaring it in the mehtod
def test_match(driver,eyes,tag=None):
    validate_window(driver,eyes,tag=tag)