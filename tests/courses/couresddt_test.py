from pages.login_page import login_page
from pages.courses_page import courses_page
from pages.home_page import home_page
from utilities.teststatus import TestStatus
import time
import unittest
import utilities.StorageUtil as st
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetup", "setup")
@ddt
class course_test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.cd = login_page(self.driver)
        self.cp = courses_page(self.driver)
        self.ts = TestStatus(self.driver)
        self.hp = home_page(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript", "JavaScript for beginners", "4521458745874588", "1125", "525"),
          ("TestNG", "TestNG Complete Bootcamp - Novice To Ninja", "4521458745874588", "1128", "989"))
    @unpack
    def test_courses_enrollment_payment_Error_Ddt(self, shortName, fulName, cardNum, cardExp, cardCvv):
        '''
        This Test contains Test with multiple data set (Data Driven Testing)
          * Login To the Application
          * Select a Course and Go to the payment page
          * Pay With Invalid Card Details
          * Verify the Payment Error.
          * logout
        :return:
        '''
        result1 = self.hp.validateHomePageTitle()
        self.ts.mark(result1, " Home Page Validation")
        self.cd.login("test@email.com", "abcabc")
        result2 = self.cp.validateCoursesPageTitle()
        self.ts.mark(result2, "Courses Page Verification")
        self.cp.enterCourseName(shortName)
        self.cp.selectCourseToEnroll(fulName)
        result3 = self.cp.verifySelectedCourseTitle(titleToVerify=fulName)
        self.ts.mark(result3, 'Verification of course selection')
        self.cp.clickOnEnrollCourse()
        self.cp.enterCreditCardInformation(cardNum, cardExp, cardCvv)
        self.cp.verifyErrorMessage()
        result4 = self.cp.verifyEnrollFailed("Your card was declined.")
        self.ts.markFinal("test_courses_enrollment_payment_Error", result4, "Payment Failed Verification")
        self.cp.logOffFromTheAccount()
