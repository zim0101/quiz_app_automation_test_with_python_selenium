"""Main application test execution area"""

from homepage.homepage import HomepageTest
from application.utils.urls import HOMEPAGE_URL, LOGIN_URL, ADMIN_DASHBOARD
from login.login import LoginTest
from application.utils.constants import HOMEPAGE_NAV_BAR, LOGIN_PAGE_X_PATHS
from settings import ADMIN_EMAIL, ADMIN_PASSWORD


if __name__ == '__main__':
    # Homepage Testing
    homepage = HomepageTest(HOMEPAGE_URL, HOMEPAGE_NAV_BAR)
    homepage.visit_homepage()
    homepage.nav_bar_content_testing()
    homepage.click_nav_elements_on_fullscreen()
    homepage.click_nav_elements_on_mobile_screen()

    # Successful Login Testing
    login_test = LoginTest(LOGIN_URL, ADMIN_EMAIL, ADMIN_PASSWORD,
                           LOGIN_PAGE_X_PATHS, ADMIN_DASHBOARD)
    login_test.visit_login_page()
    login_test.login_attempt_with_correct_credential()
    login_test.secondary_login_attempt_in_new_tab()
