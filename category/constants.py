# urls
CREATE_CATEGORY_URL = 'https://quiz.itech-theme.com/question-category-create'
CATEGORY_LIST_URL = 'https://quiz.itech-theme.com/question-category-list'

# constants
# ---------------------------- Create Form XPath -------------------------------
TITLE_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/div/div/div/div/form/' \
               'div[1]/div[1]/div/input'

PARENT_CATEGORY_DROPDOWN_X_PATH = '/html/body/div[1]/div[2]/div[' \
                                  '3]/div/div/div/div/div/form/div[1]/div[' \
                                  '2]/div/div/select '
COIN_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/' \
              'div/div/div/div/form/div[1]/div[3]/div/input'
QUESTION_LIMIT_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/' \
                        'div/div/div/div/form/div[1]/div[4]/div/input'
QUIZ_LIMIT_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/div/' \
                    'div/div/div/form/div[1]/div[5]/div/input'
TIME_LIMIT_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/' \
                    'div/div/div/div/form/div[1]/div[6]/div/input'
SERIAL_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/div/' \
                'div/div/div/form/div[1]/div[7]/div/input'
ACTIVATION_STATUS_DROPDOWN_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/' \
                                   'div/div/div/div/form/div[1]/div[8]/' \
                                   'div/div/select'
DESCRIPTION_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/div/' \
                    'div/div/div/form/div[1]/div[9]/div/textarea'
THUMBNAIL_IMAGE_X_PATH = '//*[@id="input-file-now"]'
WHITE_IMAGE_X_PATH = '//*[@id="input-file-now"]'
SUBMIT_BUTTON_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/' \
                      'div/div/div/div/form/div[2]/div/button'

# ------------------------------------------------------------------------------

PARENT_CATEGORY_OPTION_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/div/' \
                                'div/div/div/form/div[1]/div[2]/div/div/' \
                                'select/option[53]'
STATUS_ACTIVE_OPTION_X_PATH = '/html/body/div[1]/div[2]/div[3]/div/div/' \
                              'div/div/div/form/div[1]/div[8]/div/' \
                              'div/select/option[1]'
SAMPLE_IMAGE_FILE_PATH = '/home/trex/Downloads/python_image.jpg'

SUCCESS_VALIDATION_BOX_XPATH = '//*[@id="notification_box"]'

CATEGORY_CREATION_SUCCESS_VALIDATION_MESSAGE = "Sub Category " \
                                               "Created Successfully"
CATEGORY_UPDATE_SUCCESS_VALIDATION_MESSAGE = "Sub Category Updated Successfully"

TARGET_CATEGORY_X_PATH = '//*[@id="category-table"]/tbody/tr[21]/td[4]/a'
TARGET_SUBCATEGORY_X_PATH = '//*[@id="category-table"]/tbody/tr[1]/td[9]/ul' \
                            '/a[1]'

EDIT_FORM_HEADER_X_PATH = '/html/body/div[1]/div[2]/div[2]/div/div/div/div/h2'
EDIT_FORM_HEADER_TEXT = 'Edit Sub Category'

ERROR_VALIDATION_MESSAGES = [
    "This name already taken",
    "Title field can not be empty",
    "Max limit field can not be empty",
    "Quiz limit field can not be empty",
    "Time limit field can not be empty",
    "Serial field can not be empty",

]

# dictionaries
CATEGORY_FORM_X_PATHS = dict(
    title=TITLE_X_PATH,
    parent_category=PARENT_CATEGORY_DROPDOWN_X_PATH,
    coin=COIN_X_PATH,
    question_limit=QUESTION_LIMIT_X_PATH,
    quiz_limit=QUIZ_LIMIT_X_PATH,
    time_limit=TIME_LIMIT_X_PATH,
    serial=SERIAL_X_PATH,
    status=ACTIVATION_STATUS_DROPDOWN_X_PATH,
    description=DESCRIPTION_X_PATH,
    thumbnail_image=THUMBNAIL_IMAGE_X_PATH,
    white_image=WHITE_IMAGE_X_PATH,
    submit=SUBMIT_BUTTON_X_PATH
)

CATEGORY_FORM_DATA = dict(
    title='Python3.1.5',
    parent_category=PARENT_CATEGORY_OPTION_X_PATH,
    coin=100,
    question_limit=10,
    quiz_limit=10,
    time_limit=1,
    serial=243,
    status=STATUS_ACTIVE_OPTION_X_PATH,
    description='Programming category',
    thumbnail_image=SAMPLE_IMAGE_FILE_PATH,
    white_image=SAMPLE_IMAGE_FILE_PATH
)

CATEGORY_FORM_EDIT_DATA = dict(
    title='Python2.4.3',
    parent_category=PARENT_CATEGORY_OPTION_X_PATH,
    coin=200,
    question_limit=20,
    quiz_limit=20,
    time_limit=2,
    serial=405,
    status=STATUS_ACTIVE_OPTION_X_PATH,
    description='Programming category',
    thumbnail_image=SAMPLE_IMAGE_FILE_PATH,
    white_image=SAMPLE_IMAGE_FILE_PATH
)

ERROR_VALIDATION_MESSAGE_X_PATHS = dict(
    title='/html/body/div[1]/div[2]/div[3]/div/div/'
          'div/div/div/form/div[1]/div[1]/div/span/strong',
    quistion_limit='/html/body/div[1]/div[2]/div[3]/div/div/'
                   'div/div/div/form/div[1]/div[4]/div/span/strong',
    quiz_limit='/html/body/div[1]/div[2]/div[3]/div/div/'
               'div/div/div/form/div[1]/div[5]/div/span/strong',
    time_limit='/html/body/div[1]/div[2]/div[3]/div/div/'
               'div/div/div/form/div[1]/div[6]/div/span/strong',
    serial='/html/body/div[1]/div[2]/div[3]/div/div/'
           'div/div/div/form/div[1]/div[7]/div/span/strong'
)

DUPLICATE_NAME_VALIDATION_MESSAGE_X_PATH = '/html/body/div[1]/div[2]/div[3]/' \
                                           'div/div/div/div/div/form/div[1]/' \
                                           'div[1]/div/span/strong'
