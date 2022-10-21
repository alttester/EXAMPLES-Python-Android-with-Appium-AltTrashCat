from alttester import By

from .base_page import BasePage


class GetAnotherChancePage(BasePage):

    def __init__(self, altdriver, appium_driver):
        super().__init__(altdriver, appium_driver)

    @property
    def game_over_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'Game/DeathPopup/GameOver', timeout=2)

    @property
    def premium_button(self):
        return self.altdriver.wait_for_object(By.NAME, 'Game/DeathPopup/ButtonLayout/Premium Button', timeout=2)

    @property
    def available_currency(self):
        return int(self.altdriver.wait_for_object(By.NAME, 'Game/DeathPopup/PremiumDisplay/PremiumOwnCount', timeout=2).get_text())

    def is_displayed(self):
        return self.game_over_button and self.premium_button

    def press_game_over(self):
        self.game_over_button.tap()

    def press_premium_button(self):
        self.premium_button.tap()
