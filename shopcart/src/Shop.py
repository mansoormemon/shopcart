import json
import os
from pathlib import Path
import importlib.resources

from PyQt6.QtCore import QDir, Qt
from PyQt6.QtWidgets import (
    QMainWindow,
    QScrollArea,
    QWidget,
    QGridLayout,
    QLineEdit,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QTabWidget,
    QSpacerItem,
    QGroupBox,
    QStackedWidget
)

from shopcart.utils import PyUI


class Shop(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__load_configurations()
        self.__load_custom_stylesheet()

        central_wgt = QStackedWidget()
        central_wgt.setObjectName('Shop')
        self.setCentralWidget(central_wgt)

        self.__create_page()

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
        self.showMaximized()

    def __load_custom_stylesheet(self):
        base_package_name = __package__.split(".")[0]
        configurations = Shop.__get_configurations()

        with importlib.resources.open_text(f'{base_package_name}.{configurations["stylesheet"]["path"]}',
                                           configurations["stylesheet"]["file"]) as stylesheet_file:
            stylesheet = stylesheet_file.read()
        self.setStyleSheet(stylesheet)

    def __create_page(self):
        main_wgt = QGroupBox()
        main_wgt.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        main_wgt.setStyleSheet(
            '''
            QGroupBox {
                border-color: transparent;
                margin: 96px 312px;
                padding: 72px 96px;
            }
            
            QGroupBox QLabel {
                background: none;
            }
            
            QLineEdit, QComboBox, QCheckBox {
                margin-bottom: 4px;
            }
            '''
        )

        lyt = QGridLayout()
        lyt.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_wgt.setLayout(lyt)

        heading = QLabel('Welcome to Shopping Portal')
        heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        heading.setStyleSheet('color: #3882b7; font-size: 28px; font-weight: bold; margin-bottom: 8px;')

        sub_heading = QLabel('Log In to Continue')
        sub_heading.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        sub_heading.setStyleSheet('color: #579bcb; font-size: 18px;')

        umode_lbl = QLabel('User Mode:')
        self.lg_umode_cb = PyUI.ComboBox()
        self.lg_umode_cb.addItems(['Customer', 'Administrator'])
        umode_lbl.setBuddy(self.lg_umode_cb)

        uname_lbl = QLabel('Username:')
        self.lg_uname_edt = QLineEdit()
        uname_lbl.setBuddy(self.lg_uname_edt)

        password_lbl = QLabel('Password:')
        self.lg_password_edt = QLineEdit()
        self.lg_password_edt.setEchoMode(QLineEdit.EchoMode.Password)
        password_lbl.setBuddy(self.lg_password_edt)

        show_pass_chk_box = PyUI.CheckBox('Show password')

        self.lg_submit_btn = PyUI.PrimaryButton('Log In')

        sign_up_btn = PyUI.PushButton('Create a new account instead?')
        sign_up_btn.setStyleSheet('color: #3882b7;')

        lyt.addWidget(heading)
        lyt.addWidget(sub_heading)

        lyt.addWidget(umode_lbl)
        lyt.addWidget(self.lg_umode_cb)

        lyt.addWidget(uname_lbl)
        lyt.addWidget(self.lg_uname_edt)

        lyt.addWidget(password_lbl)
        lyt.addWidget(self.lg_password_edt)
        lyt.addWidget(show_pass_chk_box)

        lyt.addWidget(self.lg_submit_btn)
        lyt.addWidget(sign_up_btn)

        self.centralWidget().addWidget(main_wgt)
