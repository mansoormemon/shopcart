import enum

MAX_WIDTH = 512


class Page(enum.Enum):
    __order__ = 'LoginPage SignupPage'
    LoginPage = 0
    SignupPage = 1


class UserMode(enum.Enum):
    __order__ = 'Customer Administrator'
    Customer = 0
    Administrator = 1
