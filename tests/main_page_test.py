from time import sleep

from pages.main_page import MainPage
from tests.base_test import TestBase


class TestMainPage(TestBase):

    def setUp(self):
        self.main_page = MainPage(self.altdriver, self.appium_driver)
        self.main_page.load()

    def test_main_menu_page_loaded_correctly(self):
        assert self.main_page.is_displayed()
