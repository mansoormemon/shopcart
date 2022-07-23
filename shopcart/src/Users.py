from shopcart.src.Cart import *
from shopcart.src.Inventory import *


class User:
    def __init__(self):
        self.username = '<?>'
        self.password = '<?>'

    def change_password(self, new_password):
        self.password = new_password


class Customer(User):
    def __init__(self, name, address, contact):
        super().__init__()

        self.__name = name
        self.__address = address
        self.__contact = contact

        self.__cart = Cart()

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_contact(self, contact):
        self.__contact = contact

    def get_contact(self):
        return self.__contact

    def get_cart(self):
        return self.__cart

    def view_cart(self):
        pass

    def place_order(self):
        pass

    def remove_order(self):
        pass

    def checkout(self):
        pass

    def show_purchase_history(self):
        pass


class Admin(User):
    def __init__(self):
        super().__init__()
        self.admin_privileges = 777

    def set_permissions(self, code):
        self.admin_privileges = code

    def update_inventory(self, inventory):
        pass
