import sys

from shopcart.utils.PyUI import *

from shopcart.src.Shop import Shop
from shopcart.src.Pages import *

if __name__ == '__main__':
    app = PyUI.Application(sys.argv)

    shop = Shop()
    shop.show()

    app.exec()
