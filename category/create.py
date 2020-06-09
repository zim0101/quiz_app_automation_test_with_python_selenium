"""Category Create"""
from time import sleep
from selenium.common.exceptions import (
    ElementNotInteractableException,
    NoSuchElementException,
    JavascriptException)
from application.selenium_base import SeleniumBase
import unittest
from application.utils.helpers import console_print
from category.constants import (CATEGORY_FORM_X_PATHS,
                                SUCCESS_VALIDATION_BOX_XPATH,
                                ERROR_VALIDATION_MESSAGE_X_PATHS,
                                ERROR_VALIDATION_MESSAGES,
                                DUPLICATE_NAME_VALIDATION_MESSAGE_X_PATH)


class CategoryCreateTest(SeleniumBase, unittest.TestCase):
    def __init__(self, browser=None):
        """
        :param browser: chained previous browser
        """
        super().__init__(browser)
        if browser is not None:
            self.browser = browser

    def set_title(self, title: str):
        """
        Set title
        :param title: category title
        """
        try:
            title_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['title'])
            title_field.send_keys(title)
            console_print('success', '[Title has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_parent_category(self, option_xpath: str):
        """
        Set parent category
        :param option_xpath: option xpath
        """
        try:
            parent_category_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['parent_category'])
            parent_category_field.click()
            option = self.browser.find_element_by_xpath(option_xpath)
            option.click()
            console_print('success', '[Parent category has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_coin(self, coin: str):
        """
        Set coin
        :param coin: category coin
        """
        try:
            coin_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['coin'])
            coin_field.send_keys(coin)
            console_print('success', '[Coin has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_question_limit(self, question_limit: str):
        """
        Set question_limit
        :param question_limit: category question_limit
        """
        try:
            question_limit_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['question_limit'])
            question_limit_field.send_keys(question_limit)
            console_print('success', '[Question limit has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_quiz_limit(self, quiz_limit: str):
        """
        Set quiz_limit
        :param quiz_limit: category quiz_limit
        """
        try:
            quiz_limit_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['quiz_limit'])
            quiz_limit_field.send_keys(quiz_limit)
            console_print('success', '[Quiz limit has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_time_limit(self, time_limit: str):
        """
        Set time_limit
        :param time_limit: category time_limit
        """
        try:
            time_limit_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['time_limit'])
            time_limit_field.send_keys(time_limit)
            console_print('success', '[Time limit has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_serial(self, serial: str):
        """
        Set serial
        :param serial: category serial
        """
        try:
            serial_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['serial'])
            serial_field.send_keys(serial)
            console_print('success', '[Serial has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_status(self, option_xpath: str):
        """
        Set status
        :param option_xpath: option xpath
        """
        try:
            status_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['status'])
            status_field.click()
            option = self.browser.find_element_by_xpath(option_xpath)
            option.click()
            console_print('success', '[Status has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_description(self, description: str):
        """
        Set description
        :param description: category description
        """
        try:
            description_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['description'])
            description_field.send_keys(description)
            console_print('success', '[Serial has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_thumbnail_image(self, thumbnail_image_path: str):
        """
        Upload thumbnail image for category
        :param thumbnail_image_path: given image path in local machine
        """
        try:
            thumbnail_image_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['thumbnail_image'])
            thumbnail_image_field.send_keys(thumbnail_image_path)
            console_print('success', '[Thumbnail image has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def set_white_image(self, white_image_path: str):
        """
        Upload white image for category
        :param white_image_path: given image path in local machine
        """
        try:
            white_image_field = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['white_image'])
            white_image_field.send_keys(white_image_path)
            console_print('success', '[White image has been set]')
            self.assertTrue(True)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def submit(self):
        """
        Submit category creation form
        """
        try:
            submit_button = self.browser.find_element_by_xpath(
                CATEGORY_FORM_X_PATHS['submit'])
            submit_button.click()
            console_print('success', '[Submit button clicked]')
            self.assertTrue(True)
            sleep(1)

        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))
            self.close_browser()

            raise

    def create(self, form_data: dict):
        """
        Set all input fields by invoking their methods
        and submit the create form
        :param form_data: given form data as dictionary from constant file
        """
        try:
            self.set_title(form_data['title'])
            self.set_parent_category(form_data['parent_category'])
            self.set_coin(form_data['coin'])
            self.set_question_limit(form_data['question_limit'])
            self.set_quiz_limit(form_data['quiz_limit'])
            self.set_time_limit(form_data['time_limit'])
            self.set_serial(form_data['serial'])
            self.set_status(form_data['status'])
            self.set_description(form_data['description'])
            self.set_thumbnail_image(form_data['thumbnail_image'])
            self.set_white_image(form_data['white_image'])
            self.submit()
            console_print('success', '[Form has been submitted]')
            self.assertTrue(True)

        except Exception as error:
            console_print('failed', str(error))

            raise

    def success_validation_message_is_ok(self, message):
        """
        Check the validation message of a successful category creation
        :param message: success validation message
        """
        try:
            message_box = self.browser.find_element_by_xpath(
                SUCCESS_VALIDATION_BOX_XPATH)
            inner_text = message_box.text
            clean_text = inner_text.replace('x', '')
            print(len(clean_text.strip()))
            print(len(message.strip()))
            if clean_text.strip() == message.strip():
                console_print('success', '[Success validation message matched]')
                self.assertTrue(True)
            else:
                console_print('failed', '[Success validation didnt'
                                        ' message match]')
        except (
                ElementNotInteractableException,
                NoSuchElementException,
                JavascriptException) as error:
            console_print('failed', str(error))

            raise

    def error_validation_message_is_ok(self):
        """
        Check all error validation message by giving empty string to all fields
        """
        try:
            for message_x_path in ERROR_VALIDATION_MESSAGE_X_PATHS:
                message = self.browser.find_element_by_xpath(
                    ERROR_VALIDATION_MESSAGE_X_PATHS[message_x_path]).text
                if message not in ERROR_VALIDATION_MESSAGES:
                    console_print('failed', '[' + message_x_path
                                  + 'validation message didnt match!]')
                    print(message)
                else:
                    console_print('success',
                                  '[All validation message matched!]')
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))

            raise

    def duplicate_category_creation(self, form_data):
        """
        Submit form with a duplicate category name
        :param form_data:
        """
        try:
            self.create(form_data)
            message = self.browser.find_element_by_xpath(
                DUPLICATE_NAME_VALIDATION_MESSAGE_X_PATH)
            if message not in ERROR_VALIDATION_MESSAGES:
                console_print('success', '[Duplicate name '
                                         'validation message didnt match!]')
            else:
                console_print('failed', '[Duplicate name '
                                        'validation message matched!]')
        except (
                ElementNotInteractableException,
                NoSuchElementException) as error:
            console_print('failed', str(error))

            raise
