from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    '''
    Changed Print Statement with logger (self.log.info)
    '''

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'name':
            return By.NAME
        elif locatorType == 'css':
            return By.CSS_SELECTOR
        elif locatorType == 'link':
            return By.LINK_TEXT
        elif locatorType == 'class':
            return By.CLASS_NAME
        else:
            self.log.info(f'The locator Type : {locatorType}  is not supported')
        return False

    def getElement(self, locator, locatorType='xpath'):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f'Element is found with locator: {locator} and locator type {locatorType}')
        except:
            self.log.info(f'Element not found with locator:  {locator} and locator type {locatorType}')
        return element

    def elementClick(self, locator="", locatorType="xpath", element=None):

        """
        Click on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info(f'Element is clickable with locator: {locator} and locator type: {locatorType}')
        except:
            self.log.info(f'Element is not clickable with locator: {locator} and locator type: {locatorType}')
            print_stack()

    def sendKeys(self, data, locator="", locatorType="id", element=None):

        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info(f'Data is sent with locator: {locator} and locator type: {locatorType}')
        except:
            self.log.info(f'Sending value is not possible with locator: {locator} and  locator type:{locatorType}')
            print_stack()

    def elementPresenceCheck(self, locator, byType):
        elementList = self.driver.find_elements(byType, locator)
        try:
            if len(elementList) > 0:
                self.log.info("Element is found")
                return True
            else:
                self.log.info("Element is not found")
                return False
        except:
            self.log.info("Element is not found")
            return False

    def waitForElement(self, locator, locatorType='xpath', timeout=20, pollFrequency=0.05):

        element = None
        try:
            byType = self.getByType(locatorType)

            self.log.info(f'Waiting for Maximum :: {timeout} sec. for the element to be visible')

            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[ElementNotSelectableException,
                                                     ElementNotVisibleException, NoSuchElementException])

            element = wait.until\
                (EC.element_to_be_clickable((byType, locator)))

            self.log.info(f'Element Appeared on the page')
        except:
            self.log.info(f'Element is not present on the webpage')
            print_stack()
        return element

    def getTitle(self):
        return self.driver.title

    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time()) * 1000) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFilename = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFilename)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info(f"### Screenshot saved to :: {destinationFile}")
        except:
            self.log.error("### Exception occurred while taking ScreenShot")
            print_stack()

    def getElementList(self, locator, locatorType="id"):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def getText(self, locator="", locatorType="id", element=None, info=""):
        """
        NEW METHOD
        Get 'Text' on an element
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                self.log.debug("In locator condition")
                element = self.getElement(locator, locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: " + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementDisplayed(self, locator="", locatorType="id", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        isDisplayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element not displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False

    def webScroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def isElementPresent(self, locator="", locatorType="id", element=None):
        """
        Check if element is present
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False

    def switchToIframe(self, frameName):
        self.driver.switch_to.frame(frameName)

    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def selectWebElementArea(self, locator):
        return self.driver.getElement(locator, "xpath")

    def switchFrameByIndex(self, locator, locatorType='xpath'):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType='xpath')
            self.log.info("Length of iframe List :: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.switchToDefaultFrame()
            return result
        except:
            print("iFrame index not found")
            return result

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        if name:
            self.driver.switch_to.frame(name)
        if index:
            self.log.info("Switch frame with index:")
            self.log.info(str(index))
            self.driver.switch_to.frame(index)
