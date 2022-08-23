import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import  LogGen
import time


class Test_Faru02_Login:
    baseURL = ReadConfig.getAppUrl()
    email = ReadConfig.getEmail()
    password = ReadConfig.getPassword()
    

            
            
#Invalid Credentials test


def test_invalid_login(self,setup):
    self.driver=setup
    self.driver.get(self.baseURL)
    self.login = LoginPage(self.driver)
    self.login.setEmail(self.email_dammy)
    self.login.setPassword(self.password_invalid)
    self.login.click_login()