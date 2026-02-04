import os
import sys
import time
import unittest

from alttester import AltDriver, AltReversePortForwarding
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.dirname(__file__))


class TestBase(unittest.TestCase):
    platform = None

    @classmethod
    def setUpClass(cls):
        # Read configuration from environment variables
        platform = os.getenv('APPIUM_PLATFORM', 'Android').lower()
        appium_automation = os.getenv('APPIUM_AUTOMATION', 'UIAutomator2')
        device_name = os.getenv('APPIUM_DEVICE', 'device')
        app_file = os.getenv('APPIUM_APPFILE', 'app/application.apk')

        print(f"Starting tests on platform: {platform}, device: {device_name}")

        # Initialize Appium driver
        cls.platform = 'android' if platform == 'android' else 'ios'
        cls.options = AppiumOptions()
        cls.options.platform_name = platform
        cls.options.automation_name = appium_automation
        cls.options.set_capability('appium:deviceName', device_name)
        cls.options.set_capability('appium:app', app_file)
        cls.options.set_capability('appium:autoGrantPermissions', True)

        # Uncomment for Android Unreal build, ensure Appium waits for the correct activity
        # if platform == 'android':
        #     cls.options.set_capability('appium:appActivity', 'com.epicgames.unreal.GameActivity')
        #     cls.options.set_capability('appium:appWaitActivity', 'com.epicgames.unreal.GameActivity, com.epicgames.unreal.SplashActivity')

        cls.appium_driver = webdriver.Remote(os.getenv('APPIUM_URL', 'http://localhost:4723'), options=cls.options)
        
        print(f"Appium driver initialized with session id: {cls.appium_driver.session_id}")

        # Setup reverse port forwarding for Android
        if cls.platform == 'android':
            print("Setting up reverse port forwarding for Android")
            cls.setup_reverse_port_forwarding()
        else:
            print("Reverse port forwarding is available only for Android. Skipping this step.")

        # Set connection data in the app
        app_name = "my_app"
        cls.set_connection_data(host="127.0.0.1", port="13000", app_name=app_name)

        # Initialize AltDriver
        cls.altdriver = AltDriver(app_name=app_name)
    
    @classmethod
    def set_connection_data(cls, host, port, app_name):
        # Set XPath based on platform
        host_xpath = '//XCUIElementTypeTextField[@value="Host"]' if cls.platform == 'ios' else '//android.widget.EditText[@text="Host"]'
        port_xpath = '//XCUIElementTypeTextField[@value="Port"]' if cls.platform == 'ios' else '//android.widget.EditText[@text="Port"]'
        app_name_xpath = '//XCUIElementTypeTextField[@value="App Name"]' if cls.platform == 'ios' else '//android.widget.EditText[@text="App Name"]'
        ok_button_xpath = '//XCUIElementTypeButton[@name="OK"]' if cls.platform == 'ios' else '//android.widget.Button[@resource-id="android:id/button1"]'

        # Wait for the connection dialog to be present
        wait = WebDriverWait(cls.appium_driver, 60)
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, host_xpath)))

        # Find elements
        host_field = cls.appium_driver.find_element(AppiumBy.XPATH, host_xpath)
        port_field = cls.appium_driver.find_element(AppiumBy.XPATH, port_xpath)
        app_name_field = cls.appium_driver.find_element(AppiumBy.XPATH, app_name_xpath)
        ok_button = cls.appium_driver.find_element(AppiumBy.XPATH, ok_button_xpath)
        
        # Set values
        host_field.clear()
        host_field.send_keys(host)

        port_field.clear()
        port_field.send_keys(port)

        app_name_field.clear()
        app_name_field.send_keys(app_name)

        # Press OK button
        ok_button.click()

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
