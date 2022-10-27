from pages.main_page import MainPage
from pages.start_page import StartPage
from tests.base_test import TestBase


class TestStartPage(TestBase):

    def setUp(self):
        self.main_page = MainPage(self.altdriver, self.appium_driver)
        self.start_page = StartPage(self.altdriver, self.appium_driver)
        self.start_page.load()
      
    def test_start_page_loaded_correctly(self):
        assert self.start_page.is_displayed()

    def test_start_button_loads_main_menu(self):
        self.start_page.press_start()
        assert self.main_page.is_displayed()
