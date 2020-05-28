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
DASHBOARD_UPPER_RIGHT_MENU_X_PATH = '/html/body/div[1]/div[2]/div[' \
                                    '1]/div/div/div[2]/div/button '
LOGOUT_LINK_X_PATH = '/html/body/div[1]/div[2]/div[1]/div/div/div[' \
                     '2]/div/div/a[3] '
LOGIN_PAGE_X_PATHS = dict(email_field=LOGIN_EMAIL_FIELD_X_PATH,
                          password_field=LOGIN_PASSWORD_FIELD_X_PATH,
                          submit_button=LOGIN_SUBMIT_BUTTON_X_PATH)

REGISTRATION_USERNAME_FIELD_X_PATH = '/html/body/div/div/div/div/div/div/' \
                                     'div/form/div/div[1]/div/input[1]'
REGISTRATION_EMAIL_FIELD_X_PATH = '/html/body/div/div/div/div/div/div/div/' \
                                  'form/div/div[2]/div/input'
REGISTRATION_PASSWORD_FIELD_X_PATH = '/html/body/div/div/div/div/div/div/div/' \
                                     'form/div/div[3]/div/input'
REGISTRATION_CONFIRM_PASSWORD_FIELD_X_PATH = '/html/body/div/div/div/div/' \
                                             'div/div/div/form/div/div[4]/' \
                                             'div/input'
REGISTRATION_PHONE_FIELD_X_PATH = '/html/body/div/div/div/div/div/div/div/' \
                                  'form/div/div[5]/div/input'
REGISTRATION_SUBMIT_BUTTON_X_PATH = '/html/body/div/div/div/div/div/div/div/' \
                                    'form/div/div[6]/div/button'
REGISTRATION_VALIDATION_MESSAGE_BOX_X_PATHS = '//*[@id="notification_box"]/ul'
REGISTRATION_SUCCESS_MESSAGE_BOX_X_PATHS = '//*[@id="notification_box"]'

REGISTRATION_PAGE_X_PATHS = dict(
    username_field=REGISTRATION_USERNAME_FIELD_X_PATH,
    email_field=REGISTRATION_EMAIL_FIELD_X_PATH,
    password_field=REGISTRATION_PASSWORD_FIELD_X_PATH,
    confirm_password_field=REGISTRATION_CONFIRM_PASSWORD_FIELD_X_PATH,
    phone_field=REGISTRATION_PHONE_FIELD_X_PATH,
    submit_button=REGISTRATION_SUBMIT_BUTTON_X_PATH,
    error_message_box=REGISTRATION_VALIDATION_MESSAGE_BOX_X_PATHS,
    success_message_box=REGISTRATION_SUCCESS_MESSAGE_BOX_X_PATHS
)

REGISTRATION_ERROR_MESSAGES = [
    "Name field can not be empty",
    "Email field can not be empty",
    "Password field can not be empty",
    "Password confirmed field can not be empty",
    "The password confirmation does not match.",
    "Password length must be above 8 characters.",
    "Password must be consist of one Uppercase, one Lowercase and one Number!"
]

REGISTRATION_SUCCESS_MESSAGE = "We have just sent a verification link on " \
                               "Email ."
INVALID_EMAIL_MESSAGE = "Please enter an email address."

