from time import sleep
from selenium import webdriver
from termcolor import colored


class Homepage:
    """
        Automate homepage visiting process
    """

    def __init__(self, url: str, nav_bar_elements: list):
        """
        :param url: url of the web application
        :param nav_bar_elements: nav bar elements of the web application
        """
        self._browser = webdriver.Chrome()
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

    def scroll_homepage(self) -> bool:
        """
        Scroll down to the bottom
        :return: bool
        """
        try:
            position = 1000
            for timer in range(0, 50):
                self._browser.execute_script(
                    "window.scrollTo(0, " + str(position) + ")")
                position += 100
                sleep(3)

            console_message = colored('[success] ', 'green',
                                      attrs=['bold']) + colored(
                '[Scrolling OK!]', 'cyan')
            print(console_message)

            return True
        except Exception as e:
            console_message = colored('[failed] ', 'red', attrs=['bold']) + \
                              colored('Scrolling is not OK!', 'cyan')
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

            return False

    def compare_nav_elements(self, nav_list) -> bool:
        nav_elements_to_check = []
        for li in nav_list:
            nav_elements_to_check.append(li.text)

        nav_has_all_menu = all(element in self.nav_bar_elements
                               for element in nav_elements_to_check)

        return nav_has_all_menu
