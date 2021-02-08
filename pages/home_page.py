from base.basepage import BasePage

from pages.login_page import login_page


class home_page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validateHomePageTitle(self):
        return self.verifyPageTitle("Complete Test Automation Bundle")
