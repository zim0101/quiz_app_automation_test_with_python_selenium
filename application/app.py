"""Main application test execution area"""

from homepage.homepage import HomepageTest
from application.utils.urls import (
    HOMEPAGE_URL, LOGIN_URL, ADMIN_DASHBOARD, REGISTRATION_URL)
from login.login import LoginTest
from registration.registration import RegistrationTest
from application.utils.constants import (
    HOMEPAGE_NAV_BAR, LOGIN_PAGE_X_PATHS, REGISTRATION_PAGE_X_PATHS,
    REGISTRATION_ERROR_MESSAGES, REGISTRATION_SUCCESS_MESSAGE,
    DASHBOARD_UPPER_RIGHT_MENU_X_PATH, LOGOUT_LINK_X_PATH,
    INVALID_EMAIL_MESSAGE
)
from settings import (
    ADMIN_EMAIL, ADMIN_PASSWORD, WRONG_EMAIL, WRONG_PASSWORD,
    REGISTRATION_USER_USERNAME,
    REGISTRATION_USER_EMAIL,
    REGISTRATION_USER_PASSWORD,
    REGISTRATION_USER_PHONE,
    INVALID_EMAIL,
    INVALID_PASSWORD,
    DIFFERENT_CONFIRM_PASSWORD
)

if __name__ == '__main__':
    # Homepage Testing
    homepage = HomepageTest(HOMEPAGE_URL, HOMEPAGE_NAV_BAR)
    homepage.visit_homepage()
    homepage.nav_bar_content_testing()
    homepage.click_nav_elements_on_fullscreen()
    homepage.click_nav_elements_on_mobile_screen()
    homepage.close_browser()

    # Successful Login Testing
    login_test = LoginTest(LOGIN_URL, LOGIN_PAGE_X_PATHS, ADMIN_DASHBOARD)
    login_test.visit_login_page()
    login_test.login_attempt(ADMIN_EMAIL, ADMIN_PASSWORD)
    login_test.secondary_login_attempt_in_new_tab()
    login_test.logout(DASHBOARD_UPPER_RIGHT_MENU_X_PATH, LOGOUT_LINK_X_PATH)

    # Failed Login Testing
    login_test.visit_login_page()
    login_test.login_attempt(WRONG_EMAIL, WRONG_PASSWORD)

    # Registration Testing
    registration_test = RegistrationTest(REGISTRATION_URL,
                                         REGISTRATION_PAGE_X_PATHS)
    registration_test.visit_registration_page()

    # Failed registration testing without any values in form
    registration_test.check_registration_validation_message(
        '', '', '', '', '', REGISTRATION_ERROR_MESSAGES
    )

    # Failed registration with invalid email
    registration_test.registration_with_invalid_email(
        REGISTRATION_USER_USERNAME,
        INVALID_EMAIL,
        REGISTRATION_USER_PASSWORD,
        REGISTRATION_USER_PASSWORD,
        REGISTRATION_USER_PHONE,
        INVALID_EMAIL_MESSAGE
    )

    # Failed registration with invalid password
    registration_test.check_registration_validation_message(
        REGISTRATION_USER_USERNAME,
        REGISTRATION_USER_EMAIL,
        INVALID_PASSWORD,
        INVALID_PASSWORD,
        REGISTRATION_USER_PHONE,
        REGISTRATION_ERROR_MESSAGES
    )

    # Failed registration with different password and confirm password
    registration_test.check_registration_validation_message(
        REGISTRATION_USER_USERNAME,
        REGISTRATION_USER_EMAIL,
        REGISTRATION_USER_PASSWORD,
        DIFFERENT_CONFIRM_PASSWORD,
        REGISTRATION_USER_PHONE,
        REGISTRATION_ERROR_MESSAGES
    )

    # Successful registration test
    registration_test.check_registration_success_message(
        REGISTRATION_USER_USERNAME,
        REGISTRATION_USER_EMAIL,
        REGISTRATION_USER_PASSWORD,
        REGISTRATION_USER_PASSWORD,
        REGISTRATION_USER_PHONE,
        LOGIN_URL
    )
