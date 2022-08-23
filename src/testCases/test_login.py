import pytest
from selenium import webdriver
from src.pageObjects.LoginPage import LoginPage
from src.utilities.readproperties import ReadConfig
from src.utilities.customLogger import  LogGen
import time


class Test_Faru01_Login:
    baseURL = ReadConfig.getAppUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()


    def test_homePageTitle(self,setup):

        self.driver=setup
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        if actual_title == "Faru":
            assert True
            self.driver.close()
            
        else:
            self.driver.save_screenshot("..\\ScreenShots\\"+"test_homePagetitle.png")
            self.driver.close()
            assert False
            
    #valid credentials
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.login = LoginPage(self.driver)
        self.login.setEmail(self.email)
        self.login.setPassword(self.password)
        self.login.click_login()
        page_title =self.driver.title
        if page_title == "Faru":
            assert True
            time.sleep(3)
            self.driver.close()
            

        else:
            self.driver.save_screenshot("..\\ScreenShots\\"+"test_login.png")
            self.driver.close()
            assert False
            
