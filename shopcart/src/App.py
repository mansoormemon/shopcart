import sys

from shopcart.utils.PyUI import *

from shopcart.src.Shop import Shop

if __name__ == '__main__':
    app = PyUI.Application(sys.argv)

    shop = Shop()
    shop.show()

    app.exec()
