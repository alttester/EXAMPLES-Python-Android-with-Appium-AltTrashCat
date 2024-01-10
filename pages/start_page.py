from alttester import By

from pages.base_page import BasePage


class StartPage(BasePage):
    def __init__(self, altdriver, appium_driver):
        super().__init__(altdriver, appium_driver)

    def load(self):
        self.altdriver.load_scene('Start')

    @property
    def start_button(self):
        return self.altdriver.find_object(By.NAME, 'StartButton')

    @property
    def start_text(self):
        return self.altdriver.find_object(By.NAME, 'StartText')

    @property
    def logo_image(self):
        return self.altdriver.find_object(By.NAME, 'LogoImage')

    @property
    def unity_url_button(self):
        return self.altdriver.find_object(By.NAME, 'UnityURLButton')

    def is_displayed(self):
        return self.start_button \
            and self.start_text \
            and self.logo_image \
            and self.unity_url_button

    def press_start(self):
        self.start_button.tap()

    def get_start_button_text(self):
        return self.start_text.get_text()

    def get_status_with_appium_driver(self):
        # example method for using appium in code
        return self.appium_driver.get_status()