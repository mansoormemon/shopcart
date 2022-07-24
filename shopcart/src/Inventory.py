import csv
from pathlib import Path


class Item:
    def __init__(self, unique_id, name, price):
        self.unique_id = unique_id
        self.name = name
        self.price = price


class Inventory:
    def __init__(self, csv_file_path):
        target_file = Path(csv_file_path)
        target_file.parent.mkdir(exist_ok=True, parents=True)
        if not target_file.exists():
            with open(csv_file_path, 'w') as _:
                pass

        self.__csv_file_path = csv_file_path
        self.__stock = []

    def __len__(self):
        return len(self.__stock)

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self) -> Item:
        self.counter += 1
        if self.counter < len(self.__stock):
            return self.__stock[self.counter]
        raise StopIteration

    def add_item(self, unique_id, name, price):
        item = Item(unique_id, name, price)
        self.__stock.append(item)

    def remove_item(self, target_id):
        for item in self.__stock:
            if item.unique_id == target_id:
                self.__stock.remove(item)

    def update(self, stock):
        self.__stock = stock

    def has_item(self, target_id):
        for item in self.__stock:
            if item.unique_id == target_id:
                return True
        return False

    def get_item(self, target_id):
        for item in self.__stock:
            if item.unique_id == target_id:
                return item

    def load_from_disk(self):
        with open(self.__csv_file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                if row:
                    self.add_item(*row)

    def save_to_disk(self):
        with open(self.__csv_file_path, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=';')
            for item in self.__stock:
                csv_writer.writerow([item.unique_id, item.name, item.price])
