from alttester import By

from .base_page import BasePage


class PauseOverlayPage(BasePage):

    def __init__(self, altdriver, appium_driver):
        super().__init__(altdriver, appium_driver)

    @property
    def resume_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'Resume', timeout=2)

    @property
    def main_menu_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'Exit', timeout=2)

    @property
    def title(self):
        return self.altdriver.wait_for_object(By.PATH, '//Game/PauseMenu/Text', timeout=2)

    def is_displayed(self):
        return self.resume_button and self.main_menu_button and self.title

    def press_resume(self):
        self.resume_button.tap()

    def press_main_menu(self):
        self.main_menu_button.tap()
