import csv
from pathlib import Path

from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QWidget,
    QMessageBox,
    QTableWidget,
    QSizePolicy,
    QTreeView,
    QSpacerItem
)

from shopcart.src.Constants import *
from shopcart.utils import PyUI


class StackPage(QWidget):
    def __init__(self, unique_page_ID, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.unique_page_ID = unique_page_ID

        self.setMaximumWidth(MAX_WIDTH)


class LoginPage(StackPage):
    def __init__(self, csv_file_path, *args, **kwargs):
        super().__init__(Page.LoginPage.value, *args, **kwargs)

        target_file = Path(csv_file_path)
        target_file.parent.mkdir(exist_ok=True, parents=True)
        if not target_file.exists():
            with open(csv_file_path, 'w') as _:
                pass

        self.__csv_file_path = csv_file_path

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

        if user_mode == 'Customer':
            user_exists = False
            with open(self.__csv_file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                for row in csv_reader:
                    if row[0] == username:
                        user_exists = True
        else:
            if username == 'admin' and password == 'admin':
                pass
            else:
                error_msg_box = QMessageBox()
                error_msg_box.setText('Invalid credentials!')
                error_msg_box.setWindowTitle('Error')
                error_msg_box.exec()

    def reset(self):
        self.umode_cmb.setCurrentIndex(0)
        self.uname_edt.clear()
        self.password_edt.clear()
        self.show_password_chkb.setChecked(False)


class SignupPage(StackPage):
    def __init__(self, csv_file_path, *args, **kwargs):
        super().__init__(Page.SignupPage.value, *args, **kwargs)

        target_file = Path(csv_file_path)
        target_file.parent.mkdir(exist_ok=True, parents=True)
        if not target_file.exists():
            with open(csv_file_path, 'w') as _:
                pass

        self.__csv_file_path = csv_file_path

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

        user_exists = False
        with open(self.__csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                if row[0] == username:
                    user_exists = True

        if not user_exists:
            with open(self.__csv_file_path, 'a') as csv_file:
                csv_writer = csv.writer(csv_file, delimiter=';')
                csv_writer.writerow([username, name, address, contact, password])
                self.reset()
        else:
            error_msg_box = QMessageBox()
            error_msg_box.setText('Username taken!')
            error_msg_box.setWindowTitle('Error')
            error_msg_box.exec()

    def reset(self):
        self.uname_edt.clear()
        self.name_edt.clear()
        self.address_edt.clear()
        self.contact_edt.clear()
        self.password_edt.clear()
        self.show_password_chkb.setChecked(False)


class AdminPanel(StackPage):
    def __init__(self, *args, **kwargs):
        super().__init__(Page.AdminPanel, *args, **kwargs)

        # Add widgets.

        lyt = QGridLayout()

        heading = QLabel(
            '''
            <h1 style='color: #388f83; font-size: 28px; font-weight: bold; margin-bottom: 8px; text-align:center;'>
                Admin Panel
            </h1>
            '''
        )

        table_view = QTableWidget()
        table_view.setRowCount(32)
        table_view.setColumnCount(32)

        update_btn = PyUI.PrimaryButton('Update')
        cancel_btn = PyUI.ErrorButton('Cancel')

        lyt.addWidget(heading, 0, 0, 1, 2)
        lyt.addWidget(table_view, 1, 0, 1, 2)
        lyt.addWidget(cancel_btn, 2, 0)
        lyt.addWidget(update_btn, 2, 1)

        self.setLayout(lyt)
