"""Helper methods"""
from termcolor import colored


def console_print(message_type: str, message: str):
    """
    Print console message with color both for success and fail
    :param message_type: success or failed
    :param message: message to print
    """
    status, color = ('[success] ', 'green') \
        if message_type == 'success' \
        else ('[failed] ', 'red')
    state = colored(status, color, attrs=['bold'])
    message = colored(message, 'white')
    console_message = state + message
    print(console_message)
