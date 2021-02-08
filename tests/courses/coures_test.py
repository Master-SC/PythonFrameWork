from pages.login_page import login_page
from pages.courses_page import courses_page
from pages.home_page import home_page
from utilities.teststatus import TestStatus
import time
import unittest
import utilities.StorageUtil as st
import pytest


@pytest.mark.usefixtures("oneTimeSetup", "setup")
class course_test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.cd = login_page(self.driver)
        self.cp = courses_page(self.driver)
        self.ts = TestStatus(self.driver)
        self.hp = home_page(self.driver)

    @pytest.mark.run(order=1)
    def test_courses_enrollment_payment_Error(self):
        '''
        This Test contains
          * Login To the Application
          * Select a Course and Go to the payment page
          * Pay With Invalid Card Details
          * Verify the Payment Error.
        :return:
        '''
        result1 = self.hp.validateHomePageTitle()
        self.ts = TestStatus(self.driver)
        self.ts.mark(result1, " Home Page Validation")
        self.cd.login("test@email.com", "abcabc")
        time.sleep(20)
        result2 = self.cp.validateCoursesPageTitle()
        self.ts.mark(result2, "Courses Page Verification")
        self.cp.enterCourseName("JavaScript")
        self.cp.selectCourseToEnroll("JavaScript for beginners")
        time.sleep(10)
        result3 = self.cp.verifySelectedCourseTitle()
        self.ts.mark(result3, 'Verification of course selection')
        time.sleep(5)
        self.cp.clickOnEnrollCourse()
        self.cp.enterCreditCardInformation("4521458745874588", "1125", "525")
        self.cp.verifyErrorMessage()
        result4 = self.cp.verifyEnrollFailed("Your card was declined.")
        self.ts.markFinal("test_courses_enrollment_payment_Error", result4, "Payment Failed Verification")
