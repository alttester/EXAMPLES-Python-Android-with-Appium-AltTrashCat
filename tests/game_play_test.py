from pages.game_play_page import GamePlayPage
from pages.get_another_chance_page import GetAnotherChancePage
from pages.main_page import MainPage
from pages.pause_overlay_page import PauseOverlayPage
from tests.base_test import TestBase


class TestGamePlay(TestBase):

    def setUp(self):
        self.main_page = MainPage(self.altdriver, self.appium_driver)
        self.main_page.load()
        self.main_page.press_run()

        self.game_play_page = GamePlayPage(self.altdriver, self.appium_driver)
        self.pause_overlay_page = PauseOverlayPage(self.altdriver, self.appium_driver)
        self.get_another_chance_page = GetAnotherChancePage(self.altdriver, self.appium_driver)

    def test_game_play_page_displayed_correctly(self):
        assert self.game_play_page.is_displayed()

    def test_game_can_be_paused_and_resumed(self):
        self.game_play_page.press_pause()
        assert self.pause_overlay_page.is_displayed()

        self.pause_overlay_page.press_resume()
        assert self.game_play_page.is_displayed()

    def test_game_can_be_paused_and_stopped(self):
        self.game_play_page.press_pause()
        self.pause_overlay_page.press_main_menu()
        assert self.main_page.is_displayed()

    def test_avoiding_obstacles(self):
        self.game_play_page.avoid_obstacles(5)
        assert self.game_play_page.get_current_life() > 0

    def test_player_dies_when_obstacles_not_avoided(self):
        timeout = 10
        while timeout > 0:
            try:
                self.get_another_chance_page.is_displayed()
                break
            except Exception:
                timeout -= 1

        assert self.get_another_chance_page.is_displayed()
