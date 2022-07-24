from shopcart.src.Cart import *
from shopcart.src.Inventory import *


class User:
    def __init__(self, username='<?>', password='<?>'):
        self.__username = username
        self.__password = password

    def change_password(self, new_password):
        self.__password = new_password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


class Customer(User):
    def __init__(self, username, name, address, contact, password, history_folder_path):
        super().__init__(username, password)

        self.__history_file = f'{history_folder_path}/{username}.csv'

        target_file = Path(history_folder_path)
        target_file.mkdir(exist_ok=True, parents=True)
        if not target_file.exists():
            with open(self.__history_file, 'w') as _:
                pass

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
        with open(self.__history_file, 'a') as history_file:
            csv_writer = csv.writer(history_file, delimiter=';')
            for order in self.__cart.get_all():
                csv_writer.writerow([f'{order.get_item_ID()}', f'{order.get_quantity()}'])

        self.__cart.empty()

    def show_purchase_history(self):
        pass


class Admin(User):
    def __init__(self, username='<?>', password='<?>'):
        super().__init__(username, password)
        self.admin_privileges = 777

    def set_permissions(self, code):
        self.admin_privileges = code

    def update_inventory(self, inventory):
        pass
        
class Transaction:
    pass
