import unittest
from operator import attrgetter
from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError

server_types = (ListServer, MapServer)


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


class ProductTest(unittest.TestCase):
    def test_equality_of_products(self):
        p1 = Product("JP2", 21.37)
        p2 = Product("JP2", 21.37)
        p3 = Product("J2", 21.37)
        p4 = Product("JP2", 21.47)
        p5 = Product("Jp200000000000000000000", 21.47)
        self.assertEqual(p1, p2)
        self.assertNotEqual(p2, p3)
        self.assertNotEqual(p1, p4)
        self.assertNotEqual(p5, p4)

    def test_ValueError_throw(self):
        with self.assertRaises(ValueError):
            p = Product("L0L", 11)
        with self.assertRaises(ValueError):
            p = Product("LL", 11)
        with self.assertRaises(ValueError):
            p = Product("_LL01", 11)
        with self.assertRaises(ValueError):
            p = Product("0LL0", 11)
        with self.assertRaises(ValueError):
            p = Product("AB202022_", 11)
        with self.assertRaises(ValueError):
            p = Product("AB.202", 11)

class ServerTest(unittest.TestCase):
 
    def test_get_entries_returns_in_ascending_order(self):
        products = [Product('Pp12', 3), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(products.sort(key=attrgetter('price')), entries)
 
 
class ClientTest(unittest.TestCase):
    TestServer = ListServer([Product('aa12',1.0),Product('Ae34',3.5),Product('mn980',4.6),Product('g64',2.0),Product('h5',3.0)])
    def test_get_total_price(self):
        #przypadki braku produktów pasujących do kryterium wyszukiwania
        self.assertEqual(Client(self.TestServer).get_total_price(0),None)
        self.assertEqual(Client(self.TestServer).get_total_price(10),None)
        #wyjątki
        self.assertEqual(Client(self.TestServer).get_total_price(-3),None)
        self.assertEqual(Client(self.TestServer).get_total_price('a'),None)
        #poprawne
        self.assertEqual(Client(self.TestServer).get_total_price(2),9.1)
        self.assertEqual(Client(self.TestServer).get_total_price(1),2.0)


if __name__ == '__main__':
    unittest.main()
