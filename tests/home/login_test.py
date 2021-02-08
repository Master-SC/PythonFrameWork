from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.login_page import login_page
from pages.courses_page import courses_page
from pages.home_page import home_page
from utilities.teststatus import TestStatus
import time
import unittest
import utilities.StorageUtil as st
import pytest


@pytest.mark.usefixtures("oneTimeSetup", "setup")
class login_test(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetup):
        self.cd = login_page(self.driver)
        self.hp = home_page(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.cd1 = login_page(self.driver)
        result2 = self.cd1.validateLoginPageTitle()
        print(f'{result2}')
        self.ts.mark(result2, "Login Page Verification")
        self.lp = login_page(self.driver)
        self.lp.login("test@email.com", "abcabc")
        time.sleep(20)
        self.cp = courses_page(self.driver)
        result3 = self.cp.validateCoursesPageTitle()
        print(f'{result3}')
        self.ts.markFinal("test_validate_login", result3, "Courses Page Verification")
        self.cp.validateHomePageHeader("header")
        self.assertEqual(st.whatIsTheValue("header"), "All Courses")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        result4 = self.hp.validateHomePageTitle()
        print(f'{result4}')
        self.ts = TestStatus(self.driver)
        self.ts.mark(result4, " Home Page Validation")
        self.cd.login("testqwe@email.com", "abc123abc")
        time.sleep(5)
        self.cd.invalidLoginError("ErrorMsg")
        self.assertEqual(st.whatIsTheValue("ErrorMsg"), "Your username or password is invalid. Please try again.")
