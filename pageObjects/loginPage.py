from selenium.webdriver.common.by import By

class loginPage:
    textbox_username_id=  "username"
    textbox_username_xpath = "//input[@id='username']"
    textbox_password_id = "password"
    textbox_password_xpath = "//input[@id='password']"
    button_login_xpath =  "//button[@id='submit']"
    link_logout_linktext = "Log out"
    button_login_id = "submit"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(
            By.XPATH, self.textbox_username_xpath
        ).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(
            By.XPATH, self.textbox_password_xpath
        ).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(
            By.XPATH, self.button_login_xpath
        ).click()

    def clickSubmit(self):
        self.driver.find_element(
            By.ID, self.button_login_id
        ).click()

    def clickLogout(self):
        self.driver.find_element(
            By.LINK_TEXT, self.link_logout_linktext
        ).click()
