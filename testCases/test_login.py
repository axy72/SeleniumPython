import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from utilities.readProperties import readConfig
from utilities.customLogger import logGen


class Test_001_Login:
    baseURL = readConfig.getbaseURL()
    username = readConfig.getUserName()
    password = readConfig.getPassword()

    logger = logGen.logGenerator()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("***** Test_001_Login ***** ")
        self.logger.info("***** Starting  test case Home Page Title ***** ")

        self.driver = setup
        self.driver.get(self.baseURL)

        act_title = self.driver.title

        if act_title == "Test Login | Practice Test Automation":
            assert True
            self.driver.get_screenshot_as_file(".\\screenshots\\Test_001_Login_test_homePageTitle_PASSED.png")
            self.logger.info("***** test case Home Page Title PASSED ***** ")

        else:
            self.driver.get_screenshot_as_file(".\\screenshots\\Test_001_Login_test_homePageTitle_FAILED.png")
            self.logger.error("***** test case Home Page Title FAILED ***** ")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("***** Test_001_Login ***** ")
        self.logger.info("***** Starting  test case Log in ***** ")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginpage = loginPage(self.driver)

        self.loginpage.setUserName(self.username)
        self.logger.info("***** setUserName - Done")

        self.loginpage.setPassword(self.password)
        self.logger.info("***** setPassword - Done")

        self.loginpage.clickSubmit()
        self.logger.info("***** clickSubmit - Done")

        act_title = self.driver.title

        if act_title == "Logged In Successfully | Practice Test Automation":
            self.driver.get_screenshot_as_file(".\\screenshots\\Test_001_Login_test_login_PASSED.png")
            self.logger.info("***** test case Login - PASSED ******")
            assert True

        else:
            self.driver.get_screenshot_as_file(".\\screenshots\\Test_001_Login_test_login_FAILED.png")
            self.logger.error("***** test case Login - FAILED ******")
            assert False