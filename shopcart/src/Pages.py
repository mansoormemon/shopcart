from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QWidget
)

from shopcart.src.Constants import *
from shopcart.utils import PyUI


class StackPage(QWidget):
    def __init__(self, unique_page_ID, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.unique_page_ID = unique_page_ID

        self.setMaximumWidth(MAX_WIDTH)


class LoginPage(StackPage):
    def __init__(self, *args, **kwargs):
        super().__init__(Page.LoginPage.value, *args, **kwargs)

        # Add widgets.

        lyt = QGridLayout()

        heading = QLabel(
            '''
            <h1 style='color: #388f83; font-size: 28px; font-weight: bold; margin-bottom: 8px; text-align:center;'>
                Welcome to Shopping Portal
            </h1>
            '''
        )

        sub_heading = QLabel(
            '''
            <h3 style='color: #3fa295; font-size: 18px; text-align:center;'>
                LOG IN TO CONTINUE
            </h3>
            '''
        )

        umode_lbl = QLabel('User Mode:')
        self.umode_cmb = PyUI.ComboBox()
        for user_mode in UserMode:
            self.umode_cmb.addItem(user_mode.name, user_mode.value)
        umode_lbl.setBuddy(self.umode_cmb)

        uname_lbl = QLabel('Username:')
        self.uname_edt = QLineEdit()
        uname_lbl.setBuddy(self.uname_edt)

        password_lbl = QLabel('Password:')
        self.password_edt = QLineEdit()
        self.password_edt.setEchoMode(QLineEdit.EchoMode.Password)
        password_lbl.setBuddy(self.password_edt)
        self.show_password_chkb = PyUI.QCheckBox('Show password')

        submit_btn = PyUI.SuccessButton('Submit')

        self.create_acnt_btn = PyUI.SecondaryButton('Create a new account instead?')

        lyt.addWidget(heading)
        lyt.addWidget(sub_heading)
        lyt.addWidget(umode_lbl)
        lyt.addWidget(self.umode_cmb)
        lyt.addWidget(uname_lbl)
        lyt.addWidget(self.uname_edt)
        lyt.addWidget(password_lbl)
        lyt.addWidget(self.password_edt)
        lyt.addWidget(self.show_password_chkb)
        lyt.addWidget(submit_btn)
        lyt.addWidget(self.create_acnt_btn)

        self.setLayout(lyt)

        # Add connections.

        self.show_password_chkb.toggled.connect(self.__toggle_show_password)

        submit_btn.clicked.connect(self.__process_form)

    def __toggle_show_password(self, checked):
        if checked:
            self.password_edt.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_edt.setEchoMode(QLineEdit.EchoMode.Password)

    def __process_form(self):
        user_mode = self.umode_cmb.currentText()
        username = self.uname_edt.text()
        password = self.password_edt.text()

    def reset(self):
        self.umode_cmb.setCurrentIndex(0)
        self.uname_edt.clear()
        self.password_edt.clear()
        self.show_password_chkb.setChecked(False)


class SignupPage(StackPage):
    def __init__(self, *args, **kwargs):
        super().__init__(Page.SignupPage.value, *args, **kwargs)

        # Add widgets.

        lyt = QGridLayout()

        heading = QLabel(
            '''
            <h1 style='color: #fcb53b; font-size: 28px; font-weight: bold; margin-bottom: 8px; text-align:center;'>
                Welcome to Shopping Portal
            </h1>
            '''
        )

        sub_heading = QLabel(
            '''
            <h3 style='color: #fcbe54; font-size: 18px; text-align:center;'>
                CREATE A NEW ACCOUNT
            </h3>
            '''
        )

        uname_lbl = QLabel('Username:')
        self.uname_edt = QLineEdit()
        uname_lbl.setBuddy(self.uname_edt)

        name_lbl = QLabel('Name:')
        self.name_edt = QLineEdit()
        name_lbl.setBuddy(self.name_edt)

        address_lbl = QLabel('Address:')
        self.address_edt = QLineEdit()
        address_lbl.setBuddy(self.address_edt)

        contact_lbl = QLabel('Contact:')
        self.contact_edt = QLineEdit()
        contact_lbl.setBuddy(self.contact_edt)

        password_lbl = QLabel('Password:')
        self.password_edt = QLineEdit()
        self.password_edt.setEchoMode(QLineEdit.EchoMode.Password)
        password_lbl.setBuddy(self.password_edt)
        self.show_password_chkb = PyUI.QCheckBox('Show password')

        self.submit_btn = PyUI.WarningButton('Submit')

        self.already_have_an_acnt_btn = PyUI.SecondaryButton('Already have an account?')

        lyt.addWidget(heading)
        lyt.addWidget(sub_heading)
        lyt.addWidget(uname_lbl)
        lyt.addWidget(self.uname_edt)
        lyt.addWidget(name_lbl)
        lyt.addWidget(self.name_edt)
        lyt.addWidget(address_lbl)
        lyt.addWidget(self.address_edt)
        lyt.addWidget(contact_lbl)
        lyt.addWidget(self.contact_edt)
        lyt.addWidget(password_lbl)
        lyt.addWidget(self.password_edt)
        lyt.addWidget(self.show_password_chkb)
        lyt.addWidget(self.submit_btn)
        lyt.addWidget(self.already_have_an_acnt_btn)

        self.setLayout(lyt)

        # Add connections.

        self.show_password_chkb.toggled.connect(self.__toggle_show_password)

        self.submit_btn.clicked.connect(self.__process_form)

    def __toggle_show_password(self, checked):
        if checked:
            self.password_edt.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_edt.setEchoMode(QLineEdit.EchoMode.Password)

    def __process_form(self):
        username = self.uname_edt.text()
        name = self.name_edt.text()
        address = self.address_edt.text()
        contact = self.contact_edt.text()
        password = self.password_edt.text()

    def reset(self):
        self.uname_edt.clear()
        self.name_edt.clear()
        self.address_edt.clear()
        self.contact_edt.clear()
        self.password_edt.clear()
        self.show_password_chkb.setChecked(False)
