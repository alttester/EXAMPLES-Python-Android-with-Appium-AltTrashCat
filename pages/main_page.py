import time
from alttester import By
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, altdriver, appium_driver):
        BasePage.__init__(self, altdriver, appium_driver)

    def load(self):
        self.altdriver.load_scene('Main')

    @property
    def store_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'StoreButton', timeout=2)

    @property
    def leader_board_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'OpenLeaderboard', timeout=2)

    @property
    def settings_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'SettingButton', timeout=2)

    @property
    def mission_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'MissionButton', timeout=2)

    @property
    def run_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'StartButton', timeout=2)

    @property
    def run_button_text(self):
        return self.altdriver.wait_for_object(By.PATH, '//UICamera/Loadout/StartButton/Text', timeout=2)

    @property
    def character_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'CharName', timeout=2)

    @property
    def theme_name(self):
        return self.altdriver.wait_for_object(By.NAME, 'ThemeZone', timeout=2)

    def is_displayed(self):
        return self.store_button \
            and self.leader_board_button \
            and self.settings_button \
            and self.mission_button \
            and self.run_button \
            and self.character_name \
            and self.theme_name

    def press_run(self):
        while self.run_button_text.get_text() != "Run!":
            time.sleep(0.1)

        self.run_button.tap()