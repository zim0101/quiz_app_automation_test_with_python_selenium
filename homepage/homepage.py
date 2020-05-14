"""Homepage Automation testing"""

from time import sleep
from selenium import webdriver
from termcolor import colored
from application.utils.constants import FULL_WINDOW_NAV_ITEMS_X_PATH, \
    MOBILE_SCREEN_NAV_ITEMS_X_PATH, MOBILE_MENU_NAV_BAR_X_PATH


class HomepageTest:
    """
        Automate homepage visiting and navigation process both in fullscreen
        and medium screen
    """

    def __init__(self, url: str, nav_bar_elements: list):
        """
        :param url: url of the web application
        :param nav_bar_elements: nav bar elements of the web application
        """
        self._browser = webdriver.Chrome()
        self._browser.maximize_window()
        self.url = url
        self.nav_bar_elements = nav_bar_elements

    def visit_homepage(self) -> bool:
        """
        Visit the web application's given homepage url
        :return: bool
        """
        try:
            self._browser.get(self.url)
            console_message = colored('[success] ', 'green',
                                      attrs=['bold']) + colored(
                '[Homepage OK!]', 'cyan')
            print(console_message)
            sleep(5)

            return True
        except Exception as e:
            console_message = colored('[failed] ', 'red', attrs=['bold']) + \
                              colored('Homepage not OK', 'cyan')
            print(console_message)
            print(colored(str(e), 'red'))

            return False

    def nav_bar_content_testing(self) -> bool:
        """
        Test nav bar has all desired elements
        :return: bool
        """
        try:
            nav_menu = self._browser.find_element_by_id("nav_menu")
            nav_list = nav_menu.find_elements_by_tag_name('li')
            nav_element_matched = self.compare_nav_elements(nav_list)

            console_message = colored('[success] ', 'green',
                                      attrs=['bold']) + colored(
                '[Nav bar OK!]', 'cyan')
            print(console_message)

            return nav_element_matched
        except Exception as e:
            console_message = colored('[failed] ', 'red', attrs=['bold']) + \
                              colored('Nav bar is not OK!', 'cyan')
            print(console_message)
            print(colored(str(e), 'red'))
            self.close_browser()

            return False

    def compare_nav_elements(self, nav_list) -> bool:
        """
        Compare given nav list and web page nav list
        :param nav_list: Fetched from web page
        :return: bool
        """
        nav_elements_to_check = []
        for li in nav_list:
            nav_elements_to_check.append(li.text)

        nav_has_all_menu = all(element in self.nav_bar_elements
                               for element in nav_elements_to_check)

        return nav_has_all_menu

    def click_nav_elements_on_fullscreen(self) -> bool:
        """
        This will test nav bar element by clicking on their link while window
        size is in full screen
        :return: bool
        """
        try:
            for element in FULL_WINDOW_NAV_ITEMS_X_PATH:
                self.click_on_element(element)
            sleep(2)
            console_message = colored('[success] ', 'green',
                                      attrs=['bold']) + colored(
                '[Nav elements link OK!]', 'cyan')
            print(console_message)

            return True
        except Exception as e:
            console_message = colored('[failed] ', 'red', attrs=['bold']) + \
                              colored('Nav elements link is not OK!', 'cyan')
            print(console_message)
            print(colored(str(e), 'red'))
            self.close_browser()

            return False

    def click_nav_elements_on_mobile_screen(self) -> bool:
        """
        This will test nav bar element by clicking on their link after
        decreasing window size
        :return: bool
        """
        try:
            self.set_window_screen()
            self.click_on_element(MOBILE_MENU_NAV_BAR_X_PATH)
            for element in MOBILE_SCREEN_NAV_ITEMS_X_PATH:
                self.click_on_element(element)
            console_message = colored('[success] ', 'green',
                                      attrs=['bold']) + colored(
                '[Nav elements link on full screen OK!]', 'cyan')
            print(console_message)

            return True
        except Exception as e:
            console_message = colored('[failed] ', 'red', attrs=['bold']) + \
                              colored('Nav elements link on mobile screen is '
                                      'not OK!', 'cyan')
            print(console_message)
            print(colored(str(e), 'red'))
            self.close_browser()

            return False

    def click_on_element(self, x_path):
        """
        Will click on given x_path of html element
        :param x_path: x_path of html element
        """
        element = self._browser.find_element_by_xpath(x_path)
        element.click()
        sleep(1)

    def set_window_screen(self) -> bool:
        """
        This method is resize the browser window
        :return: bool
        """
        try:
            sleep(2)
            self._browser.set_window_size(768, 1024)
            console_message = colored('[success] ', 'green',
                                      attrs=['bold']) + colored(
                '[Custom window size OK!]', 'cyan')
            print(console_message)

            return True
        except Exception as e:
            console_message = colored('[failed] ', 'red', attrs=['bold']) + \
                              colored('Custom window size is not OK!', 'cyan')
            print(console_message)
            print(colored(str(e), 'red'))
            self.close_browser()

            return False

    def close_browser(self):
        """
        Close the browser
        """
        self._browser.quit()
