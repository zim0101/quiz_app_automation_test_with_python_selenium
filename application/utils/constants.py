"""Core constants"""

HOMEPAGE_NAV_BAR = ["Home", "About Us", "Feature", "How It Works", "Sign In"]

FULL_WINDOW_NAV_ITEMS_X_PATH = [
    '//*[@id="nav_menu"]/li[2]/a',
    '//*[@id="nav_menu"]/li[3]/a',
    '//*[@id="nav_menu"]/li[4]/a',
    '//*[@id="scrolltop"]/a'
]

MOBILE_MENU_NAV_BAR_X_PATH = '//*[@id="scrolltop"]/header/div/div/div/div[' \
                             '3]/div/div/a '

MOBILE_SCREEN_NAV_ITEMS_X_PATH = [
    '//*[@id="scrolltop"]/header/div/div/div/div[3]/div/div/nav/ul/li[2]/a',
    '//*[@id="scrolltop"]/header/div/div/div/div[3]/div/div/nav/ul/li[3]/a',
    '//*[@id="scrolltop"]/header/div/div/div/div[3]/div/div/nav/ul/li[4]/a',
    '//*[@id="scrolltop"]/a'
]

LOGIN_EMAIL_FIELD_X_PATH = '/html/body/div/div/div/div/div/div/div/form/div[' \
                           '1]/input '

LOGIN_PASSWORD_FIELD_X_PATH = '/html/body/div/div/div/div/div/div/div/form' \
                              '/div[2]/input '
LOGIN_SUBMIT_BUTTON_X_PATH = '/html/body/div/div/div/div/div/div/div/form' \
                             '/button '
LOGIN_PAGE_X_PATHS = dict(email_field=LOGIN_EMAIL_FIELD_X_PATH,
                          password_field=LOGIN_PASSWORD_FIELD_X_PATH,
                          submit_button=LOGIN_SUBMIT_BUTTON_X_PATH)
