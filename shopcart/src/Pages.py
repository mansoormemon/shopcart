import csv
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QWidget,
    QMessageBox,
    QTableWidget,
    QSizePolicy,
    QTreeView,
    QSpacerItem,
    QTableWidgetItem,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QScrollArea,
    QDialog,
    QSpinBox,
    QScrollBar
)

from shopcart.src.Constants import *
from shopcart.utils import PyUI
from shopcart.src.Inventory import *
from shopcart.src.Users import *


class StackPage(QWidget):
    def __init__(self, unique_page_ID, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.unique_page_ID = unique_page_ID


class LoginPage(StackPage):
    def __init__(self, csv_file_path, *args, **kwargs):
        super().__init__(Page.LoginPage.value, *args, **kwargs)

        self.setMaximumWidth(MAX_WIDTH)

        target_file = Path(csv_file_path)
        target_file.parent.mkdir(exist_ok=True, parents=True)
        if not target_file.exists():
            with open(csv_file_path, 'w') as _:
                pass

        self.__csv_file_path = csv_file_path

        self.parent_stack = None
        self.admin_panel = None
        self.shopping_page = None

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
            credentials = None
            with open(self.__csv_file_path, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                for row in csv_reader:
                    if row[0] == username and row[4] == password:
                        credentials = row
                        break
            if credentials is not None:
                customer = Customer(*row)
                self.reset()
                self.shopping_page.update_display(customer)
                self.parent_stack.setCurrentIndex(self.shopping_page.unique_page_ID)
            else:
                error_msg_box = QMessageBox()
                error_msg_box.setText('Invalid credentials!')
                error_msg_box.setWindowTitle('Error')
                error_msg_box.exec()
        else:
            if username == 'admin' and password == 'admin':
                user = Admin(username, password)
                self.reset()
                self.admin_panel.update_display(user)
                self.parent_stack.setCurrentIndex(self.admin_panel.unique_page_ID)
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

        self.setMaximumWidth(MAX_WIDTH)

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
                error_msg_box = QMessageBox()
                error_msg_box.setText('User created!')
                error_msg_box.setWindowTitle('Success')
                error_msg_box.exec()
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
        super().__init__(Page.AdminPanel.value, *args, **kwargs)

        # Add widgets.
        self.parent_stack = None
        self.login_page = None
        self.inventory = None

        lyt = QGridLayout()

        heading = QLabel(
            '''
            <h1 style='color: #388f83; font-size: 28px; font-weight: bold; margin-bottom: 8px; text-align:center;'>
                Admin Panel
            </h1>
            '''
        )

        self.table_wgt = QTableWidget()
        self.table_wgt.setRowCount(32)
        self.table_wgt.setColumnCount(32)

        self.label_status = QLabel()

        update_btn = PyUI.PrimaryButton('Update')
        log_out_btn = PyUI.SecondaryButton('Log Out')

        update_btn.clicked.connect(self.__update_inventory)
        log_out_btn.clicked.connect(self.__logout)

        lyt.addWidget(heading, 0, 0, 1, 2)
        lyt.addWidget(self.table_wgt, 1, 0, 1, 2)
        lyt.addWidget(self.label_status, 2, 0)
        lyt.addWidget(log_out_btn, 3, 0)
        lyt.addWidget(update_btn, 3, 1)

        self.setLayout(lyt)

    def __logout(self):
        self.parent_stack.setCurrentIndex(self.login_page.unique_page_ID)
        self.inventory.save_to_disk()

    def update_display(self, user):
        print(user.get_username(), user.get_password())
        i = 0
        for item in self.inventory:
            self.table_wgt.setItem(i, 0, QTableWidgetItem(str(item.unique_id)))
            self.table_wgt.setItem(i, 1, QTableWidgetItem(str(item.name)))
            self.table_wgt.setItem(i, 2, QTableWidgetItem(str(item.price)))
            i += 1

        self.label_status.setText(f'Currently logged in as \'{user.get_username()}\'.')

    def __update_inventory(self):
        def is_empty(cell):
            return cell is None or not cell.text()

        stock = []

        for i in range(self.table_wgt.rowCount()):
            cell1 = self.table_wgt.item(i, 0)
            cell2 = self.table_wgt.item(i, 1)
            cell3 = self.table_wgt.item(i, 2)
            if is_empty(cell1) or is_empty(cell2) or is_empty(cell3):
                break
            item = Item(cell1.text(), cell2.text(), cell3.text())
            stock.append(item)

        self.inventory.update(stock)


class ShoppingItemCard(QWidget):
    def __init__(self, item: Item, cart: Cart, cart_panel_lyt, *args, **kwargs):
        super().__init__(*args, **kwargs)

        lyt = QHBoxLayout()

        self.item_ID = item.unique_id
        self.cart = cart
        self.cart_panel_lyt = cart_panel_lyt

        lyt.addWidget(QLabel(f'{item.unique_id}'), stretch=1)
        lyt.addWidget(QLabel(f'{item.name}'), stretch=1)
        lyt.addWidget(QLabel(f'Rs. {item.price}'), stretch=1)

        self.quantity_box = QSpinBox()
        self.quantity_box.setMinimum(1)
        lyt.addWidget(self.quantity_box, stretch=1)

        self.add_to_cart_btn = PyUI.WarningButton('Add to Cart')
        lyt.addWidget(self.add_to_cart_btn, stretch=1)

        self.add_to_cart_btn.clicked.connect(self.__add_item_to_cart)

        self.setLayout(lyt)

    def __add_item_to_cart(self):
        order = Order(Order.count, self.item_ID, self.quantity_box.value())

        self.cart.add_order(order)

        cart_item = CartItemCard(order, self.cart, self.cart_panel_lyt)
        self.cart_panel_lyt.addWidget(cart_item)

        self.quantity_box.setValue(1)


class CartItemCard(QWidget):
    def __init__(self, order: Order, cart: Cart, cart_panel_lyt, *args, **kwargs):
        super().__init__(*args, **kwargs)

        lyt = QHBoxLayout()

        self.order = order
        self.cart = cart
        self.cart_panel_lyt = cart_panel_lyt

        lyt.addWidget(QLabel(f'{order.get_ID()}'), stretch=1)
        lyt.addWidget(QLabel(f'{order.get_item_ID()}'), stretch=1)
        lyt.addWidget(QLabel(f'{order.get_quantity()}'), stretch=1)

        self.remove_from_cart_btn = PyUI.ErrorButton('X')
        lyt.addWidget(self.remove_from_cart_btn, stretch=1)

        self.remove_from_cart_btn.clicked.connect(self.__remove_item_from_cart)

        self.setLayout(lyt)

    def __remove_item_from_cart(self):
        self.cart.remove_order(self.order.get_ID())
        self.cart_panel_lyt.removeWidget(self)


class Header(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()

        lyt = QHBoxLayout()

        for heading in args:
            lyt.addWidget(QLabel(f'<h4>{heading}</h4>'))

        self.setLayout(lyt)


class ShoppingPage(StackPage):
    def __init__(self, *args, **kwargs):
        super().__init__(Page.ShoppingPage.value, *args, **kwargs)

        # Add widgets.
        self.parent_stack = None
        self.login_page = None
        self.inventory = None

        lyt = QGridLayout()

        heading = QLabel(
            '''
            <h1 style='color: #388f83; font-size: 28px; font-weight: bold; margin-bottom: 8px; text-align:center;'>
                Shopping Page
            </h1>
            '''
        )

        user_info_cnt = QGroupBox('User Info')

        user_info_cnt_lyt = QVBoxLayout()
        self.cname = QLabel()
        self.caddr = QLabel()
        self.ccont = QLabel()
        user_info_cnt_lyt.addWidget(self.cname)
        user_info_cnt_lyt.addWidget(self.caddr)
        user_info_cnt_lyt.addWidget(self.ccont)

        user_info_cnt.setLayout(user_info_cnt_lyt)

        sub_wgt = QGroupBox('Available Items')

        sub_wgt_lyt = QHBoxLayout()

        self.item_panel = QScrollArea()
        self.item_panel.setWidgetResizable(True)
        self.item_panel_wgt = QWidget()
        self.item_panel.setWidget(self.item_panel_wgt)

        self.item_panel_lyt = QVBoxLayout()
        self.item_panel_lyt.addWidget(Header('ID', 'Product', 'Price', 'Quantity', ''))
        self.item_panel_wgt.setLayout(self.item_panel_lyt)

        self.cart_panel = QScrollArea()
        self.cart_panel.setWidgetResizable(True)
        self.cart_panel_wgt = QWidget()
        self.cart_panel.setWidget(self.cart_panel_wgt)

        self.cart_panel_lyt = QVBoxLayout()
        self.cart_panel_lyt.addWidget(Header('Order', 'Item', 'Quantity', ''))
        self.cart_panel_lyt.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.cart_panel_wgt.setLayout(self.cart_panel_lyt)

        sub_wgt_lyt.addWidget(self.item_panel, stretch=2)
        sub_wgt_lyt.addWidget(self.cart_panel, stretch=1)

        sub_wgt.setLayout(sub_wgt_lyt)

        self.label_status = QLabel()

        checkout_btn = PyUI.SuccessButton('Checkout')
        log_out_btn = PyUI.SecondaryButton('Log Out')

        checkout_btn.clicked.connect(self.__checkout)
        log_out_btn.clicked.connect(self.__logout)

        lyt.addWidget(heading, 0, 0, 1, 2)
        lyt.addWidget(user_info_cnt, 1, 0, 1, 2)
        lyt.addWidget(sub_wgt, 2, 0, 1, 2)
        lyt.addWidget(self.label_status, 3, 0, 1, 2)
        lyt.addWidget(log_out_btn, 4, 0, 1, 1)
        lyt.addWidget(checkout_btn, 4, 1, 1, 1)

        self.setLayout(lyt)

    def update_display(self, customer):
        self.customer = customer

        self.cname.setText(f'<b>Name:</b> {customer.get_name()}')
        self.caddr.setText(f'<b>Address:</b> {customer.get_address()}')
        self.ccont.setText(f'<b>Contact:</b> {customer.get_contact()}')

        self.label_status.setText(f'Currently logged in as \'{customer.get_username()}\'.')

        for item in self.inventory:
            item_card = ShoppingItemCard(item, customer.get_cart(), self.cart_panel.widget().layout())
            self.item_panel.widget().layout().addWidget(item_card)

    def __checkout(self):
        transaction_modal_dialog = TransactionModalDialog(self.customer)
        transaction_modal_dialog.exec()

        self.customer.get_cart().empty()

        for child in self.cart_panel_wgt.children():
            if type(child) == CartItemCard:
                self.cart_panel_lyt.removeWidget(child)

    def __logout(self):
        self.parent_stack.setCurrentIndex(self.login_page.unique_page_ID)

        for child in self.item_panel_wgt.children():
            if type(child) == ShoppingItemCard:
                self.item_panel_lyt.removeWidget(child)

        for child in self.cart_panel_wgt.children():
            if type(child) == CartItemCard:
                self.cart_panel_lyt.removeWidget(child)


class TransactionModalDialog(QDialog):
    def __init__(self, customer, *args, **kwargs):
        super().__init__(*args, **kwargs)

        lyt = QVBoxLayout()

        proceed_btn = PyUI.PrimaryButton('Proceed Transaction')
        proceed_btn.clicked.connect(lambda: self.close())

        lyt.addWidget(proceed_btn)

        self.setLayout(lyt)
