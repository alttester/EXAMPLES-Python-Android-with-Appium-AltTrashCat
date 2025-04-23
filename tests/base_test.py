import os
import sys
import time
import unittest

from alttester import AltDriver, AltReversePortForwarding
from appium import webdriver
from appium.options.common import AppiumOptions

sys.path.append(os.path.dirname(__file__))


class TestBase(unittest.TestCase):
    platform = None

    @classmethod
    def setUpClass(cls):
        if os.getenv("APPIUM_PLATFORM", "android") == 'android':
            cls.platform = 'android'
        else:
            cls.platform = 'ios'
        print("Running on " + cls.platform)

        cls.options = AppiumOptions()
        cls.options.platform_name = os.getenv('APPIUM_PLATFORM', 'Android')
        cls.options.automation_name = os.getenv('APPIUM_AUTOMATION', 'UIAutomator2')
        cls.options.set_capability('appium:deviceName', os.getenv('APPIUM_DEVICE', 'device'))
        cls.options.set_capability('appium:app', os.getenv("APPIUM_APPFILE", "application.apk"))
        cls.appium_driver = webdriver.Remote(os.getenv('APPIUM_URL', 'http://localhost:4723'), options=cls.options)
        print("Appium driver started")
        cls.setup_reverse_port_forwarding()
        time.sleep(10)
        cls.altdriver = AltDriver()

    @classmethod
    def setup_reverse_port_forwarding(cls):
        try:
            AltReversePortForwarding.remove_reverse_port_forwarding_android()
        except:
            print("No adb forward was present")
        if cls.platform == 'android':
            AltReversePortForwarding.reverse_port_forwarding_android()
            print("Port forwarded (Android).")
        else:
            print("Reverse port forwarding is available only for Android")

    @classmethod
    def tearDownClass(cls):
        print("\nEnding")
        try:
            AltReversePortForwarding.remove_reverse_port_forwarding_android()
            print("Reverse port forwarding removed")
        except:
            print("No adb forward was present")
        cls.altdriver.stop()
        cls.appium_driver.quit()
