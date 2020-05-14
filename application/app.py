"""Main application test execution area"""

from homepage.homepage import HomepageTest
from application.utils.urls import HOMEPAGE_URL, LOGIN_URL, ADMIN_DASHBOARD
from login.login import LoginTest
from application.utils.constants import HOMEPAGE_NAV_BAR, LOGIN_PAGE_X_PATHS, \
    DASHBOARD_UPPER_RIGHT_MENU_X_PATH, LOGOUT_LINK_X_PATH
from settings import ADMIN_EMAIL, ADMIN_PASSWORD, WRONG_EMAIL, WRONG_PASSWORD


if __name__ == '__main__':
    # Homepage Testing
    homepage = HomepageTest(HOMEPAGE_URL, HOMEPAGE_NAV_BAR)
    homepage.visit_homepage()
    homepage.nav_bar_content_testing()
    homepage.click_nav_elements_on_fullscreen()
    homepage.click_nav_elements_on_mobile_screen()

    # Successful Login Testing
    login_test = LoginTest(LOGIN_URL, LOGIN_PAGE_X_PATHS, ADMIN_DASHBOARD)
    login_test.visit_login_page()
    login_test.login_attempt(ADMIN_EMAIL, ADMIN_PASSWORD)
    login_test.secondary_login_attempt_in_new_tab()
    login_test.logout(DASHBOARD_UPPER_RIGHT_MENU_X_PATH, LOGOUT_LINK_X_PATH)

    # Failed Login Testing
    login_test.visit_login_page()
    login_test.login_attempt(WRONG_EMAIL, WRONG_PASSWORD)
