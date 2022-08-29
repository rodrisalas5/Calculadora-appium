from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
import unittest
import time


class CellPhone(unittest.TestCase):
    def __init__(self):
        self.desired_capabilities = desired_capabilities = {
            "appium:platformVersion": "11",
            "appium:UDID": "t8ibyp8xgi95xsga",
            "appium:appPackage": "com.miui.calculator",
            "appium:appActivity": "com.miui.calculator.cal.CalculatorActivity",
            "platformName": "Android",
            "appium:noReset": True,
            "appium:deviceName": "Redmi",
            "appium:ignoreHiddenApiPolicyError": True
        }


    def start_server(self):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_capabilities)
        return driver


    def add(self):
        driver = self.start_server()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_5_s').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'más').click()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_7_s').click()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_equal_s').click()
        result = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView').text
        return result


    def less(self):
        driver = self.start_server()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_7_s').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'menos').click()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_5_s').click()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_equal_s').click()
        result = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView').text
        return result


    def multiplied(self):
        driver = self.start_server()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_5_s').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'multiplicar').click()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_2_s').click()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_equal_s').click()
        result = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView').text
        return result


    def divided(self):
        driver = self.start_server()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_4_s').click()
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'dividir').click()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_2_s').click()
        driver.find_element(AppiumBy.ID, 'com.miui.calculator:id/btn_equal_s').click()
        result = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView').text
        return result