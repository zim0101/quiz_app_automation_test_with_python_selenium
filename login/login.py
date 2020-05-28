"""
    LoginTest module will test:
    1. Successful login
    2. Failed login with wrong credential
    3. Secondary Login attempt in a new tab after a successful login.

    If users redirect to the dashboard url or any given url, then login attempt
    will be successful

"""

from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, \
    NoSuchElementException, JavascriptException, TimeoutException
from application.utils.helpers import console_print


class LoginTest:
    """
        LoginTest class test successful and failed login attempt as well as try
        to login after a successful login in a new tab. Log out testing can
        also be done.
    """

    def __init__(self, url: str, login_page_x_paths: dict, dashboard_url: str):
        """
        :param url: Web application's login url
        :param login_page_x_paths: form and button XPaths
        :param dashboard_url: dashboard url after login redirection
        """

        self.url = url
        self.login_page_x_paths = login_page_x_paths
        self.dashboard_url = dashboard_url
        self._browser = webdriver.Firefox()

    def visit_login_page(self):
        """
        Visit the web application's given login url
        :return: bool
        """
        try:
            self._browser.get(self.url)
            console_print('success', '[Login page OK!]')
            sleep(2)
        except TimeoutException as error:
            console_print('failed', '[Login page not OK!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def login_attempt(self, email: str, password: str):
        """
        Attempt a login with given correct credentials
        :param email: given user email
        :param password: given user password
        """
        self.login(email, password)
        redirected_to_dashboard: bool = self.current_url_is_dashboard_url()
        console_print('success', '[Login is working!]') if \
            redirected_to_dashboard else \
            console_print('failed', '[Wrong credential, Login failed!]')

    def secondary_login_attempt_in_new_tab(self):
        """
        After make a successful login attempt we will try to open a new tab and
        visit the login page again, generally it will redirect us to the after
        login redirect url which is dashboard in most cases.
        """
        self.open_and_switch_to_new_tab()
        self.visit_login_page()
        redirected_to_dashboard: bool = self.current_url_is_dashboard_url()
        console_print('success', '[Secondary login attempt redirected to '
                                 'dashboard!]') if \
            redirected_to_dashboard else \
            console_print('failed', '[New tab redirection failed!]')

    def open_and_switch_to_new_tab(self):
        """
        Execute javascript to open new tab and then switch to the new tab
        """
        try:
            self._browser.execute_script("window.open('');")
            sleep(1)
            self._browser.switch_to.window(self._browser.window_handles[1])
            console_print('success', '[New tab opened!]')
        except JavascriptException as error:
            console_print('failed', '[New tab open failed!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def current_url_is_dashboard_url(self) -> bool:
        """
        Check the current url and if it is the dashboard url then return true
        otherwise return false
        :return: bool
        """
        current_url = self._browser.current_url
        if current_url == self.dashboard_url:
            console_print('success', '[Current url is dashboard url!]')

            return True
        console_print('failed', '[Current url is not dashboard url!]')

        return False

    def login(self, email: str, password: str):
        """
        Invoke methods to set email and password and submit the login form
        :param email: user email
        :param password: user password
        """
        self.set_email(email)
        self.set_password(password)
        self.submit()
        sleep(2)

    def set_email(self, email: str):
        """
        Set email to the email field which will be selected by its XPath
        :param email: user email
        """
        try:
            email_field = self._browser.find_element_by_xpath(
                self.login_page_x_paths['email_field'])
            email_field.send_keys(email)
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Email input failed!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def set_password(self, password: str):
        """
        Set password to the password field which will be selected by its XPath
        :param password: user password
        """
        try:
            password_field = self._browser.find_element_by_xpath(
                self.login_page_x_paths['password_field'])
            password_field.send_keys(password)
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Password input failed!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def submit(self):
        """
        Get the submit button by its given XPath and click the button to submit
        the login form
        """
        try:
            submit_button = self._browser.find_element_by_xpath(
                self.login_page_x_paths['submit_button'])
            submit_button.click()
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Credential submit failed!]')
            console_print('failed', str(error))
            self._browser.quit()
            print()

            raise

    def logout(self, menu: str, logout_link: str):
        """
        Logout from dashboard
        :param menu: Upper right menu in dashboard
        :param logout_link: logout link
        """
        try:
            self._browser.find_element_by_xpath(menu).click()
            self._browser.find_element_by_xpath(logout_link).click()
            console_print('success', '[Logout successful!]') if \
                self._browser.current_url == self.url else \
                console_print('failed', '[Logout failed!]')
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Logout failed!]')
            console_print('failed', str(error))
            self._browser.quit()
            print()

            raise
