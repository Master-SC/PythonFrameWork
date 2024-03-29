"""
@package base
WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == "Edge":
            # Set ie driver
            edgedriver = 'D:\\Selenium_Drivers\\msedgedriver.exe'
            driver = webdriver.Edge(executable_path=edgedriver)
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "Chrome":
            # Set chrome driver
            chromedriver = "D:\\Selenium_Drivers\\chromedriver.exe"
            driver = webdriver.Chrome(executable_path=chromedriver)
        else:
            driver = webdriver.Edge()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
