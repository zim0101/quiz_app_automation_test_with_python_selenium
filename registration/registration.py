"""
    Registration module tasks:
    1. Register with correct credentials
    2. Register with wrong credentials
    3. Validation messages
"""
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, \
    NoSuchElementException, TimeoutException
from application.utils.helpers import console_print


class RegistrationTest:
    """RegistrationTest class"""

    def __init__(self, url: str, registration_x_paths: dict):
        self.url = url
        self.registration_x_paths = registration_x_paths
        self._browser = webdriver.Firefox()

    def visit_registration_page(self):
        """
        Will visit the registration page
        """
        try:
            self._browser.get(self.url)
            console_print('success', '[Registration page OK!]')
            sleep(2)
        except TimeoutException as error:
            console_print('failed', '[Registration page not OK!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def register(self, username: str, email: str, password: str,
                 confirm_password: str, phone: str):
        """
        Invoke methods to set username, email, password, confirm password and
        submit the registration form
        :param phone:
        :param confirm_password:
        :param username:
        :param email: user email
        :param password: user password
        """
        self.set_username(username)
        sleep(1)
        self.set_email(email)
        sleep(1)
        self.set_password(password)
        sleep(1)
        self.set_confirm_password(confirm_password)
        sleep(1)
        self.set_phone(phone)
        self.submit()
        sleep(2)

    def check_registration_success_message(self, username: str, email: str,
                                           password: str,
                                           confirm_password: str,
                                           phone: str,
                                           success_message: list) -> bool:
        try:
            self.register(username, email, password, confirm_password, phone)
            sleep(2)
            message = self._browser.find_element_by_xpath(
                self.registration_x_paths['success_message_box']).text
            if message is not success_message:
                console_print('failed', '[Validation message didnt match!]')
                return False
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self._browser.quit()

            return False

    def check_registration_validation_message(self, username: str, email: str,
                                              password: str,
                                              confirm_password: str,
                                              phone: str,
                                              error_messages: list) -> bool:
        """
        Attempt a failed registration and then will check the validation
        messages is in our predefined expected list
        :param username: will be empty
        :param email: will be empty or invalid email
        :param password: invalid password will be given
        :param confirm_password: password and confirm password will not be same
        :param phone: might be empty for this particular test
        :param error_messages: predefined expected validation messages
        :return: True / False according to the test
        """
        try:
            self._browser.refresh()
            sleep(1)
            self.register(username, email, password, confirm_password, phone)
            sleep(2)
            validation_message_ul = self._browser.find_element_by_xpath(
                self.registration_x_paths['error_message_box'])
            validation_messages_li = validation_message_ul. \
                find_elements_by_tag_name('li')
            validation_messages = []
            for li in validation_messages_li:
                validation_messages.append(li.text)
            print(validation_messages)
            for message in validation_messages:
                if message not in error_messages:
                    console_print('failed', '[Validation message didnt match!]')
                    print(message)
                    return False
            console_print('success', '[All validation message matched!]')

            return True
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self._browser.quit()

            return False

    def set_username(self, username: str):
        """
        Set username to the username field which will be selected by its XPath
        :param username: user email
        """
        try:
            username_field = self._browser.find_element_by_xpath(
                self.registration_x_paths['username_field'])
            username_field.send_keys(username)
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Username input failed!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def set_email(self, email: str):
        """
        Set email to the email field which will be selected by its XPath
        :param email: user email
        """
        try:
            email_field = self._browser.find_element_by_xpath(
                self.registration_x_paths['email_field'])
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
                self.registration_x_paths['password_field'])
            password_field.send_keys(password)
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Password input failed!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def set_confirm_password(self, confirm_password):
        """
        Set same or wrong password to the confirm password field which will be
        selected by its XPath
        :param confirm_password: user password
        """
        try:
            confirm_password_field = self._browser.find_element_by_xpath(
                self.registration_x_paths['confirm_password_field'])
            confirm_password_field.send_keys(confirm_password)
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Confirm Password input failed!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def set_phone(self, phone: str):
        """
        Set phone to the phone field which will be selected by its XPath
        :param phone: user phone number
        """
        try:
            phone_field = self._browser.find_element_by_xpath(
                self.registration_x_paths['confirm_password_field'])
            phone_field.send_keys(phone)
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Phone input failed!]')
            console_print('failed', str(error))
            self._browser.quit()

            raise

    def submit(self):
        """
        Get the submit button by its given XPath and click the button to submit
        the registration form
        """
        try:
            submit_button = self._browser.find_element_by_xpath(
                self.registration_x_paths['submit_button'])
            submit_button.click()
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', '[Credential submit failed!]')
            console_print('failed', str(error))
            self._browser.quit()
            print()

            raise
