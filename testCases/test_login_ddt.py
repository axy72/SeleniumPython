import pytest
from selenium import webdriver
from pageObjects.loginPage import loginPage
from utilities.readProperties import readConfig
from utilities.customLogger import logGen
from utilities import XLUtils

class Test_002_Login_DDT:
    baseURL = readConfig.getbaseURL()
    path = ".//testData/loginData.xlsx"
    logger = logGen.logGenerator()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("***** Test_002_Login_DDT ***** ")
        self.logger.info("***** Starting  test case Log in ***** ")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginpage = loginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'hoja1')
        self.logger.info("Number of rows..."+str(self.rows))
        lst_status = []

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'hoja1', r, 1)
            self.logger.info((self.user))

            self.password = XLUtils.readData(self.path, 'hoja1', r, 2)
            self.logger.info((self.password))

            self.exp = XLUtils.readData(self.path, 'hoja1', r, 3)
            self.logger.info((self.exp))

            self.loginpage.setUserName(self.user)
            self.loginpage.setPassword(self.password)
            self.loginpage.clickSubmit()

            act_title = self.driver.title
            exp_title = "Logged In Successfully | Practice Test Automation"

            login_success = (act_title == exp_title)
            expected_success = (self.exp.lower() == "pass")

            result = "Pass" if login_success == expected_success else "Fail"
            self.logger.info("result:"+ result)
            self.logger.info(f"**** {result.lower()}ed ****")
            lst_status.append(result)
            if login_success:
                self.loginpage.clickLogout()

        if "Fail" not in lst_status:
            self.logger.info("**** DDT TEST PASSED ****")
            self.driver.get_screenshot_as_file(".\\screenshots\\Test_002_Login_test_DDT_PASSED.png")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** DDT TEST FAILED ****")
            self.driver.get_screenshot_as_file(".\\screenshots\\Test_002_Login_test_DDT_FAILED.png")
            self.driver.close()
            assert False









        #self.loginpage.setUserName(self.username)
        #self.logger.info("***** setUserName - Done")

        #self.loginpage.setPassword(self.password)
        #self.logger.info("***** setPassword - Done")

        #self.loginpage.clickSubmit()
        #self.logger.info("***** clickSubmit - Done")

        #act_title = self.driver.title

        #if act_title == "Logged In Successfully | Practice Test Automation":
         #   self.driver.get_screenshot_as_file(".\\screenshots\\Test_001_Login_test_login_PASSED.png")
         #   self.logger.info("***** test case Login - PASSED ******")
         #   assert True

        #else:
           #self.driver.get_screenshot_as_file(".\\screenshots\\Test_001_Login_test_login_FAILED.png")
           #self.logger.error("***** test case Login - FAILED ******")
           #assert False