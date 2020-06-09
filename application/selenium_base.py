"""Base class for selenium operation"""
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class SeleniumBase:
    """Base class for selenium driver"""
    def __init__(self, browser=None):
        """
        :param browser: for cain testing
        """
        if browser is None:
            self.browser = webdriver.Firefox()
        else:
            self.browser = browser

    def visit_url(self, url: str):
        """
        Visit a specific url
        :param url:
        """
        try:
            self.browser.get(url)
        except WebDriverException:
            self.close_browser()

            raise

    def close_browser(self):
        """
        Quit this browser instance
        """
        self.browser.quit()
