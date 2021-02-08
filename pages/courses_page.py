from base.basepage import BasePage
import utilities.StorageUtil as cs
import utilities.custom_logger as cl
import logging
import time


class courses_page(BasePage):

    """
    locators
    """
    _courses_page_header = "//h1[text()='All Courses']"
    _courses_search_box_field = "//input[contains(@id, 'search')]"
    _course_search_button = "//button[contains(@class, 'find-course search-course')]"
    _course_enrollment_button = '//button[@class="dynamic-button btn btn-default btn-lg btn-enroll"]'
    _courses_payment_card_number = '//input[@placeholder="Card Number"]'
    _courses_payment_card_expiry = '//input[@placeholder="MM / YY"]'
    _courses_payment_card_cvv = '//input[@placeholder="Security Code"]'
    _courses_card_number_iframe_name = '__privateStripeFrame1965'
    _courses_payment_area = '//div[@class  = "payment-outer "]'
    _courses_buy_button = '//button[@class="zen-subscribe sp-buy btn btn-default btn-lg btn-block ' \
                          'btn-gtw btn-submit checkout-button dynamic-button"]'
    _courses_payment_status = '(//p[@class="dynamic-text"])[1]'
    _courses_all_courses_link = '//a[contains(text(), "ALL COURSES")]'
    _courses_my_account_menu_link = '//span[@class = "caret"]'
    _courses_my_account_logoff_link = '//a[contains(text(), "Logout")]'

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validateCoursesPageTitle(self):
        return self.verifyPageTitle('All Courses')

    def validateHomePageHeader(self, titleKey):
        checkele = self.elementPresenceCheck(self._courses_page_header, 'xpath')
        ele = self.getElement(self._courses_page_header, 'xpath')
        if checkele:
            header = ele.text
            print(f"The Text is :: {header}")
            cs.rememberTheValue(titleKey, header)
        else:
            print("Header is not present")

    def clickOnCourseSearch(self):
        self.elementClick(self._course_search_button, "xpath")

    def selectCourseToEnroll(self, courseFullName):
        ele = self.getElement(f'//*[contains(text(), "{courseFullName}")]')
        self.elementClick(element=ele)
        time.sleep(10)

    def verifySelectedCourseTitle(self, titleToVerify=""):
        return self.verifyPageTitle(titleToVerify)

    def clickOnEnrollCourse(self):
        time.sleep(5)
        return self.elementClick(self._course_enrollment_button, "xpath")

    def clickOnAllCourses(self):
        return self.elementClick(self._courses_all_courses_link, "xpath")

    def clickOnMyAccountLink(self):
        return self.elementClick(self._courses_my_account_menu_link, "xpath")

    def clickOnLogOffOption(self):
        return self.elementClick(self._courses_my_account_logoff_link, "xpath")

    def enterCourseName(self, courseName):
        self.sendKeys(courseName, self._courses_search_box_field, "xpath")
        self.clickOnCourseSearch()

    def enterCardNum(self, number):
        '''
        card number : 4521 4587 4587 4588
        :param number:
        :return:
        '''

        if len(number) == 16:
            self.switchToIframe(0)
            self.sendKeys(number, self._courses_payment_card_number, "xpath")
            self.switchToDefaultFrame()
        else:
            print(f'Entered number:: {number} is not 16 digit')

    def enterCardExp(self, exp):
        if len(exp) == 4:
            ##self.switchToIframe(1)
            self.switchFrameByIndex(self._courses_payment_card_expiry, "xpath")
            self.sendKeys(exp, self._courses_payment_card_expiry, "xpath")
            self.switchToDefaultFrame()
        else:
            print(f'Entered expiry date :: {exp} is not of 4 digit')

    def enterCardCVV(self, cvv):
        if len(cvv) == 3:
            self.switchToIframe(2)
            self.sendKeys(cvv, self._courses_payment_card_cvv, "xpath")
            self.switchToDefaultFrame()
        else:
            print(f'Entered cvv number:: {cvv} is not of 4 digit')

    def clickOnBuyButton(self):
        self.elementClick(self._courses_buy_button, "xpath")

    def enterCreditCardInformation(self, num="", exp="", cvv=""):
        time.sleep(10)
        self.webScroll("down")
        self.enterCardNum(num)
        self.enterCardCVV(cvv)
        self.enterCardExp(exp)
        self.clickOnBuyButton()
        time.sleep(5)
        self.webScroll("up")

    def verifyErrorMessage(self):
        EnrolmentStatus = self.isElementDisplayed(self._courses_payment_status, "xpath")
        if EnrolmentStatus:
            ErrorMsg = self.getText(self._courses_payment_status, 'xpath')
            print(f'The Error Message is :: {ErrorMsg}')
        else:
            print("Error in Validation")

    def verifyEnrollFailed(self, ErrorMsg):
        expectedText = self.getText(self._courses_payment_status, "xpath")
        if self.verifyTextContainCheck(expectedText, ErrorMsg):
            self.log.info("Error Message Verification Successful")
            return True
        else:
            self.log.error("Error Message Verification is not Successful")
            return False

    def logOffFromTheAccount(self):
        self.clickOnMyAccountLink()
        self.clickOnLogOffOption()
        time.sleep(10)
