import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError


class ListServerTest(unittest.TestCase):

    def test_TooManyProductsFoundError_throw(self):
        products = [Product(f"PPP{(a)*100+(a+3)*10+a+4}", a*3)
                    for a in range(1, 11)] + [Product(f"PP{(a)*100+(a+6)*10+a+1}", a*2) for a in range(1, 11)]
        server = ListServer(products)
        with self.assertRaises(TooManyProductsFoundError):
            server.get_entries(3)
        with self.assertRaises(TooManyProductsFoundError):
            server.get_entries(2)

        try:
            server.get_entries(1)
        except TooManyProductsFoundError:
            self.fail()


class MapServerTest(unittest.TestCase):

    def test_TooManyProductsFoundError_throw(self):
        products = [Product(f"PPP{(a)*100+(a+3)*10+a+4}", a*3)
                    for a in range(1, 11)] + [Product(f"PP{(a)*100+(a+6)*10+a+1}", a*2) for a in range(1, 11)]
        server = MapServer(products)
        with self.assertRaises(TooManyProductsFoundError):
            server.get_entries(3)
        with self.assertRaises(TooManyProductsFoundError):
            server.get_entries(2)

        try:
            server.get_entries(1)
        except TooManyProductsFoundError:
            self.fail()


if __name__ == '__main__':
    unittest.main()
