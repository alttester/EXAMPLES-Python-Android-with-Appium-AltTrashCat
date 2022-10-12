from pages.base_page import BasePage
from alttester import By
from appium.webdriver.common.touch_action import TouchAction
from time import sleep


class MainPage(BasePage):
    def __init__(self, altdriver, appium_driver):
        BasePage.__init__(self, altdriver, appium_driver)

    def load(self):
        self.altdriver.load_scene('Main')

    @property
    def start_button(self):
        return self.altdriver.find_object(By.NAME, 'StartButton')

    @property
    def store_button(self):
        return self.altdriver.find_object(By.NAME, 'StoreButton')

    @property
    def mission_button(self):
        return self.altdriver.find_object(By.NAME, 'MissionButton')

    @property
    def setting_button(self):
        return self.altdriver.find_object(By.NAME, 'SettingButton')

    def is_displayed(self):
        if self.start_button and self.store_button and self.mission_button and self.setting_button:
            return True

    def start_game(self):
        print("StartButton tapping")

        sleep(10)
        self.start_button.tap()
        sleep(5)

    def close_ad(self):
        el = self.appium_driver.find_element_by_xpath(
            '/ hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')
        actions = TouchAction(self.appium_driver)
        actions.tap(el)
        actions.perform()
