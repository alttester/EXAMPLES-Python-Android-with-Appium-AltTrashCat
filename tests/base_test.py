import os
import sys
import time

sys.path.append(os.path.dirname(__file__))

from altunityrunner import AltUnityDriver
import unittest
import pytest
import os
from appium import webdriver
from altunityrunner.alt_unity_port_forwarding import AltUnityPortForwarding


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
        cls.desired_caps['app'] = os.getenv("APPIUM_APPFILE", "TrahCat.apk")
        cls.desired_caps['automationName'] = os.getenv('APPIUM_AUTOMATION', 'UIAutomator2')
        cls.appium_driver = webdriver.Remote('http://localhost:4723/wd/hub', cls.desired_caps)
        print("Appium driver started")
        cls.setup_port_forwarding()
        time.sleep(10)
        cls.altdriver = AltUnityDriver()

    @classmethod
    def setup_port_forwarding(cls):
        try:
            AltUnityPortForwarding.remove_forward_android()
        except:
            print("No adb forward was present")
        try:
            AltUnityPortForwarding.kill_all_iproxy_process()
        except:
            print("No iproxy forward was present")

        if cls.platform == 'android':
            AltUnityPortForwarding().forward_android()
            print("Port forwarded (Android).")
        else:
            AltUnityPortForwarding().forward_ios()
            print("Port forwarded (iOS).")

    @classmethod
    def tearDownClass(cls):
        print("Ending")
        cls.altdriver.stop()
        cls.appium_driver.quit()

