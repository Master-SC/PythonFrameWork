
import time
from base.basepage import BasePage
import utilities.custom_logger as cl
import logging
import utilities.StorageUtil as st


class login_page(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    '''
    Locator
    '''
    _signIn_link = "//a[text()='Sign In']"
    _login_email_field = "//input[@placeholder='Email Address']"
    _login_pwd_field = "//input[@placeholder='Password']"
    _login_button = "//input[@type='submit']"
    _invalid_login_message = "//span[contains(text(), 'Your username or password is invalid. Please try again.')]"
    _home_page_header = "//h1[text()='All Courses']"

    '''
    Method for basic Actions.
    '''
    def clickSignInLink(self):
        self.elementClick(self._signIn_link, locatorType='xpath')

    def enterEmail(self, email):
        self.sendKeys(email, self._login_email_field, locatorType='xpath')

    def enterPwd(self, pwd):
        self.sendKeys(pwd, self._login_pwd_field, locatorType='xpath')

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType='xpath')

    def clearEmailPassword(self):
        element_email = self.getElement(self._login_email_field, 'xpath')
        element_email.clear()
        element_pwd = self.getElement(self._login_pwd_field, 'xpath')
        element_pwd.clear()

    def invalidLoginError(self, LogInErrorKey):
        check = self.elementPresenceCheck(self._invalid_login_message, "xpath")
        invalidError = self.getElement(self._invalid_login_message, "xpath")
        if check:
            ErrorText = invalidError.text
            print(f'The Error is:: "{ErrorText}"')
            st.rememberTheValue(LogInErrorKey, ErrorText)
        else:
            print("No Error Message Present")
            
    def validateHomePageHeader(self, titleKey):
        check_element = self.elementPresenceCheck(self._home_page_header, 'xpath')
        ele = self.getElement(self._home_page_header, 'xpath')
        if check_element:
            header = ele.text
            print(f"The Text is :: {header}")
            st.rememberTheValue(titleKey, header)

        else:
            print("Header is not present")

    def validateLoginPageTitle(self):
        return self.verifyPageTitle("Login")

    '''
    Page Functionalities. 
    '''
    def login(self, email="", pwd=""):
        time.sleep(5)
        self.clickSignInLink()
        time.sleep(5)
        self.clearEmailPassword()
        time.sleep(2)
        self.enterEmail(email)
        self.enterPwd(pwd)
        time.sleep(2)
        self.clickLoginButton()
        time.sleep(20)
