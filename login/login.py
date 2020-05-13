from time import sleep
from selenium import webdriver
from application.utils.helpers import console_print
from selenium.common.exceptions import ElementNotInteractableException, \
    NoSuchElementException, JavascriptException, TimeoutException


class LoginTest:

    def __init__(self, url: str, email: str, password: str,
                 email_field_x_path: str, password_field_x_path: str,
                 submit_button_x_path: str, dashboard_url: str):
        """
        :param url: Web application's login url
        :param email: user email
        :param password: user password
        :param email_field_x_path: email field XPath
        :param password_field_x_path: password field XPath
        :param submit_button_x_path: submit button XPath
        :param dashboard_url: dashboard url after login redirection

        """

        self.url = url
        self.email = email
        self.password = password
        self.email_field_x_path = email_field_x_path
        self.password_field_x_path = password_field_x_path
        self.submit_button_x_path = submit_button_x_path
        self.dashboard_url = dashboard_url
        self._browser = webdriver.Chrome()

    def visit_login_page(self):
        """
        Visit the web application's given login url
        :return: bool
        """
        try:
            self._browser.get(self.url)
            console_print('success', '[Login page OK!]')
            sleep(2)
        except TimeoutException as e:
            console_print('failed', '[Login page not OK!]')
            console_print('failed', str(e))
            self._browser.quit()

            raise

    def login_attempt_with_correct_credential(self):
        """
        Attempt a login with given correct credentials
        """
        self.login(self.email, self.password)
        console_print('success', '[Login is working!]')

    def secondary_login_attempt_in_new_tab(self):
        """
        After make a successful login attempt we will try to open a new tab and
        visit the login page again, generally it will redirect us to the after
        login redirect url which is dashboard in most cases.
        """
        self.open_and_switch_to_new_tab()
        self.visit_login_page()
        self.current_url_is_dashboard_url()
        console_print('success', '[Secondary login attempt redirected to '
                                 'dashboard!]')

    def open_and_switch_to_new_tab(self):
        """
        Execute javascript to open new tab and then switch to the new tab
        """
        try:
            self._browser.execute_script("window.open('');")
            sleep(1)
            self._browser.switch_to.window(self._browser.window_handles[1])
            console_print('success', '[New tab opened!]')
        except JavascriptException as e:
            console_print('failed', '[New tab open failed!]')
            console_print('failed', str(e))
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
                self.email_field_x_path)
            email_field.send_keys(email)
        except (ElementNotInteractableException, NoSuchElementException) as e:
            console_print('failed', '[Email input failed!]')
            console_print('failed', str(e))
            self._browser.quit()

            raise

    def set_password(self, password: str):
        """
        Set password to the password field which will be selected by its XPath
        :param password: user password
        """
        try:
            password_field = self._browser.find_element_by_xpath(
                self.password_field_x_path)
            password_field.send_keys(password)
        except (ElementNotInteractableException, NoSuchElementException) as e:
            console_print('failed', '[Password input failed!]')
            console_print('failed', str(e))
            self._browser.quit()

            raise

    def submit(self):
        """
        Get the submit button by its given XPath and click the button to submit
        the login form
        """
        try:
            submit_button = self._browser.find_element_by_xpath(
                self.submit_button_x_path)
            submit_button.click()
        except (ElementNotInteractableException, NoSuchElementException) as e:
            console_print('failed', '[Credential submit failed!]')
            console_print('failed', str(e))
            self._browser.quit()

            raise
