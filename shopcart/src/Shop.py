import json
import os
from pathlib import Path
import importlib.resources

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

from shopcart.src.Pages import LoginPage, SignupPage


class Shop(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__load_configurations()
        self.__load_custom_stylesheet()

        central_wgt = QStackedWidget()
        central_wgt.setObjectName('Shop')
        self.setCentralWidget(central_wgt)

        self.login_page = None
        self.signup_page = None

        self.__create_login_page()
        self.__create_signup_page()
        self.__bind_login_and_signup_page()

    @staticmethod
    def __get_configurations():
        base_package_name = __package__.split(".")[0]
        with importlib.resources.open_text(base_package_name, 'config.json') as config_file:
            configurations = json.load(config_file)
        return configurations

    def __load_configurations(self):
        pkg_root = Path(os.path.dirname(__file__)).parent.absolute()
        QDir.addSearchPath('resources', f'{pkg_root}/res')

        configurations = Shop.__get_configurations()
        self.setWindowTitle(configurations['window']['title'])
        self.setMinimumSize(configurations['window']['min_width'], configurations['window']['min_height'])

    def __load_custom_stylesheet(self):
        base_package_name = __package__.split(".")[0]
        configurations = Shop.__get_configurations()

        with importlib.resources.open_text(f'{base_package_name}.{configurations["stylesheet"]["path"]}',
                                           configurations["stylesheet"]["file"]) as stylesheet_file:
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
        self.login_page = LoginPage()
        lyt.addWidget(self.login_page)
        lyt.addItem(vspacer_b)

        lyt.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        wgt.setLayout(lyt)
        lyt.addWidget(copyright)

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
        self.signup_page = SignupPage()
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
