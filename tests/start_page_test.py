from pages.start_page import StartPage
from tests.base_test import TestBase


class TestStartPage(TestBase):

    def setUp(self):
        self.start_page = StartPage(self.altdriver, self.appium_driver)
        self.start_page.load()

    # def test_start_page_loaded_correctly_after_background(self):
    #     print("Running the app in background with Appium")
    #     self.start_page.put_app_in_background(5)
    #     print("Checking if the app could be resumed successfully")
    #     assert(self.start_page.is_displayed())
