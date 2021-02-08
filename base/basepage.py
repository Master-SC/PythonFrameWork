from base.selenium_webdriver import SeleniumDriver
from utilities.util import Util
from traceback import print_stack


class BasePage(SeleniumDriver):

    def __init__(self, driver):

        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verifyPageTitle(self, titleToVerify):
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextMatch(actualTitle, titleToVerify)

        except:
            self.log.error('Failed to get the page title')
            print_stack()
            return False

    def verifyTextContainCheck(self, textFromElement, textToCheck):
        try:
            return self.util.verifyTextContains(textFromElement, textToCheck)
        except:
            self.log.error(f"The text :{textFromElement} doesn't contains {textToCheck}")
            print_stack()
            return False

