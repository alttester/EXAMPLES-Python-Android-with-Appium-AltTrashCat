from pages.main_page import MainPage
from tests.base_test import TestBase


class TestMainPage(TestBase):

    def setUp(self):
        self.main_page = MainPage(self.altdriver, self.appium_driver)
        self.main_page.load()

    def test_close_ad(self):
        self.main_page.start_game()
        self.main_page.close_ad()
        assert(self.main_page.is_displayed())
