import enum

MAX_WIDTH = 512


class Page(enum.Enum):
    __order__ = 'LoginPage SignupPage AdminPanel'
    LoginPage = 0
    SignupPage = 1
    AdminPanel = 2


class UserMode(enum.Enum):
    __order__ = 'Customer Administrator'
    Customer = 0
    Administrator = 1
