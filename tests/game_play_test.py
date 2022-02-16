from pages.game_play_page import GamePlayPage
from pages.main_page import MainPage
from tests.base_test import TestBase


class TestGamePlayPage(TestBase):

    def setUp(self):
        self.main_page = MainPage(self.altdriver, self.appium_driver)
        self.game_play_page = GamePlayPage(self.altdriver, self.appium_driver)
        self.main_page.load()

    def test_avoiding_obstacles(self):
        self.game_play_page.avoid_obstacles(5)
        assert self.game_play_page.get_current_life() > 0
