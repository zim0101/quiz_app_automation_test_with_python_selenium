from termcolor import colored


def console_print(message_type: str, message: str):
    status, color = ('[success] ', 'green') \
        if message_type == 'success' \
        else ('[failed] ', 'red')
    state = colored(status, color, attrs=['bold'])
    message = colored(message, 'white')
    console_message = state + message
    print(console_message)
