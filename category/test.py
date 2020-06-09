"""Category automation testing unit"""

from application.utils.urls import (LOGIN_URL, ADMIN_DASHBOARD)
from category.edit import CategoryEditTest
from login.login import LoginTest
from category.create import CategoryCreateTest
from application.utils.constants import LOGIN_PAGE_X_PATHS
from settings import (
    ADMIN_EMAIL, ADMIN_PASSWORD
)
from category.constants import *

if __name__ == '__main__':
    # Successful Login
    login_test = LoginTest(LOGIN_URL, LOGIN_PAGE_X_PATHS, ADMIN_DASHBOARD)
    login_test.visit_url(LOGIN_URL)
    login_test.login_attempt(ADMIN_EMAIL, ADMIN_PASSWORD)

    # Category Successful create Test
    category_create_test = CategoryCreateTest(login_test.browser)
    category_create_test.visit_url(CREATE_CATEGORY_URL)
    category_create_test.create(CATEGORY_FORM_DATA)
    category_create_test.success_validation_message_is_ok(
        CATEGORY_CREATION_SUCCESS_VALIDATION_MESSAGE)

    # Category create validation message Test
    category_create_test.visit_url(CREATE_CATEGORY_URL)
    category_create_test.submit()
    category_create_test.error_validation_message_is_ok()

    # Try to save with duplicate name
    category_create_test.duplicate_category_creation(CATEGORY_FORM_DATA)

    # Edit test
    category_edit_test = CategoryEditTest(login_test.browser)
    category_edit_test.visit_url(CATEGORY_LIST_URL)
    category_edit_test.get_edit_form()
    category_edit_test.update(CATEGORY_FORM_EDIT_DATA)
    category_edit_test.success_validation_message_is_ok(
        CATEGORY_UPDATE_SUCCESS_VALIDATION_MESSAGE)

    category_edit_test.visit_url(CATEGORY_LIST_URL)
    category_edit_test.get_edit_form()
    category_edit_test.clear_all_input_field()
    category_edit_test.submit()
    category_edit_test.error_validation_message_is_ok()

