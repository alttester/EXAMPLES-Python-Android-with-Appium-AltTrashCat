import os
import sys
import time
import unittest

from alttester import AltDriver, AltPortForwarding
from appium import webdriver

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
        cls.desired_caps = {}
        cls.desired_caps['platformName'] = os.getenv('APPIUM_PLATFORM', 'Android')
        cls.desired_caps['deviceName'] = os.getenv('APPIUM_DEVICE', 'device')
        cls.desired_caps['app'] = os.getenv("APPIUM_APPFILE", "application.apk")
        cls.desired_caps['automationName'] = os.getenv('APPIUM_AUTOMATION', 'UIAutomator2')
        cls.appium_driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        print("Appium driver started")
        cls.setup_port_forwarding()
        time.sleep(10)
        cls.altdriver = AltDriver()

    @classmethod
    def setup_port_forwarding(cls):
        try:
            AltPortForwarding.remove_all_forward_android()
        except:
            print("No adb forward was present")
        try:
            AltPortForwarding.kill_all_iproxy_process()
        except:
            print("No iproxy forward was present")

        if cls.platform == 'android':
            AltPortForwarding.forward_android()
            print("Port forwarded (Android).")
        else:
            AltPortForwarding.forward_ios()
            print("Port forwarded (iOS).")

    @classmethod
    def tearDownClass(cls):
        print("\nEnding")
        cls.altdriver.stop()
        cls.appium_driver.quit()
