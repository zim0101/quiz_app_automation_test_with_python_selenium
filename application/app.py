from homepage.homepage import HomepageTest
from application.utils.urls import HOMEPAGE_URL
from application.utils.constants import HOMEPAGE_NAV_BAR


if __name__ == '__main__':
    homepage = HomepageTest(HOMEPAGE_URL, HOMEPAGE_NAV_BAR)
    homepage.visit_homepage()
    homepage.nav_bar_content_testing()
    homepage.click_nav_elements_on_fullscreen()
    homepage.click_nav_elements_on_mobile_screen()
    homepage.close_browser()
