# Modules
from termcolor import *


def log_debug(text):
    cprint(text, color="blue", attrs=['bold'])


def log_info(text):
    cprint(text, color="white", attrs=['bold'])


def log_error(text):
    cprint(text, color="red", attrs=['bold'])


def log_warn(text):
    cprint(text, color="yellow", attrs=['bold'])


def log_success(text):
    cprint(text, color="green", attrs=['bold'])
    

