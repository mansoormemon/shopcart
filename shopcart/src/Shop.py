import json

from PyQt6.QtCore import QDir, Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QVBoxLayout,
    QWidget
)

from shopcart.src.Pages import LoginPage, SignupPage, AdminPanel, ShoppingPage
from shopcart.src.Inventory import *
from shopcart.src.Users import *


class Shop(QMainWindow):
    __project_root = Path(__file__).parent.parent

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__load_configurations()
        self.__load_custom_stylesheet()

        central_wgt = QStackedWidget()
        central_wgt.setObjectName('Shop')
        self.setCentralWidget(central_wgt)

        self.login_page = None
        self.signup_page = None
        self.user = None

        self.__inventory = Inventory(f'{Shop.__project_root}/res/records/inventory.csv')
        self.__inventory.load_from_disk()

        self.__create_login_page()
        self.__create_signup_page()
        self.__bind_login_and_signup_page()

        self.__create_admin_panel()
        self.__create_shopping_page()

    @staticmethod
    def __get_configurations():
        with open(f'{Shop.__project_root}/config.json') as config_file:
            configurations = json.load(config_file)
        return configurations

    def __load_configurations(self):
        QDir.addSearchPath('resources', f'{Shop.__project_root}/res')

        configurations = Shop.__get_configurations()
        self.setWindowTitle(configurations['window']['title'])
        self.setMinimumSize(configurations['window']['min_width'], configurations['window']['min_height'])

    def __load_custom_stylesheet(self):
        with open(f'{Shop.__project_root}/res/stylesheets/style.qss') as stylesheet_file:
            stylesheet = stylesheet_file.read()
        self.setStyleSheet(stylesheet)

    def __create_login_page(self):
        wgt = QWidget()
        wgt.setObjectName('LoginPage')
        wgt.setProperty('class', 'ContainerWithBackground')

        copyright = QLabel(
            '''
            <p style='text-align: center;'>
                <small>© ShopCart, 2022</small>
            </p>
            '''
        )

        vspacer_t = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        vspacer_b = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        lyt = QVBoxLayout()

        lyt.addItem(vspacer_t)
        self.login_page = LoginPage(f'{Shop.__project_root}/res/records/user.csv')
        lyt.addWidget(self.login_page)
        lyt.addItem(vspacer_b)

        lyt.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        wgt.setLayout(lyt)
        lyt.addWidget(copyright)

        self.login_page.parent_stack = self.centralWidget()

        self.centralWidget().addWidget(wgt)

    def __create_signup_page(self):
        wgt = QWidget()
        wgt.setObjectName('SignupPage')
        wgt.setProperty('class', 'ContainerWithBackground')

        copyright = QLabel(
            '''
            <p style='text-align: center;'>
                <small>© ShopCart, 2022</small>
            </p>
            '''
        )

        vspacer_t = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        vspacer_b = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        lyt = QVBoxLayout()

        lyt.addItem(vspacer_t)
        self.signup_page = SignupPage(f'{Shop.__project_root}/res/records/user.csv')
        lyt.addWidget(self.signup_page)
        lyt.addItem(vspacer_b)
        lyt.addWidget(copyright)

        lyt.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        wgt.setLayout(lyt)

        self.centralWidget().addWidget(wgt)

    def __bind_login_and_signup_page(self):
        self.login_page.create_acnt_btn.clicked.connect(
            lambda: (self.centralWidget().setCurrentIndex(self.signup_page.unique_page_ID), self.login_page.reset())
        )
        self.signup_page.already_have_an_acnt_btn.clicked.connect(
            lambda: (self.centralWidget().setCurrentIndex(self.login_page.unique_page_ID), self.signup_page.reset())
        )

    def __create_admin_panel(self):
        self.login_page.admin_panel = AdminPanel()
        self.login_page.admin_panel.setObjectName('AdminPanel')

        self.login_page.admin_panel.login_page = self.login_page
        self.login_page.admin_panel.parent_stack = self.centralWidget()
        self.login_page.admin_panel.inventory = self.__inventory

        self.centralWidget().addWidget(self.login_page.admin_panel)

    def __create_shopping_page(self):
        self.login_page.shopping_page = ShoppingPage()
        self.login_page.shopping_page.setObjectName('ShoppingPage')

        self.login_page.shopping_page.login_page = self.login_page
        self.login_page.shopping_page.parent_stack = self.centralWidget()
        self.login_page.shopping_page.inventory = self.__inventory

        self.centralWidget().addWidget(self.login_page.shopping_page)
