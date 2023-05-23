import allure
from allure import attachment_type

def test_attach():
    allure.attach("Text", name="Text", attachment_type=attachment_type.TEXT)