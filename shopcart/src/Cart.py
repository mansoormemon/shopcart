from shopcart.src.Inventory import *


class Order:
    count = 0

    def __init__(self, ID, item_ID, quantity):
        Order.count += 1
        self.__ID = ID
        self.__item_ID = item_ID
        self.__quantity = quantity

    def get_ID(self):
        return self.__ID

    def get_item_ID(self):
        return self.__item_ID

    def get_quantity(self):
        return self.__quantity

    def calculate_total(self, inventory: Inventory):
        if inventory.has_item(self.__item_ID):
            item = inventory.get_item(self.__item_ID)
            return float(self.__quantity) * float(item.price)


class Cart:
    def __init__(self):
        self.__orders = []

    def __len__(self):
        return len(self.__orders)

    def get_all(self):
        return self.__orders

    def get_order(self, order_ID):
        for order in self.__orders:
            if order.get_ID() == order_ID:
                return order

    def add_order(self, order: Order):
        self.__orders.append(order)

    def remove_order(self, order_ID):
        for order in self.__orders:
            if order.get_ID == order_ID:
                del order

    def calculate_total(self, inventory: Inventory):
        acc = 0
        for order in self.__orders:
            acc += order.calculate_total(inventory)
        return acc
