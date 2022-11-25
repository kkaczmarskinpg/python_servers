import unittest
from operator import attrgetter
 
from servers import ListServer, Product, Client, MapServer
 
server_types = (ListServer, MapServer)
 
 
class ServerTest(unittest.TestCase):
 
    def test_get_entries_returns_in_ascending_order(self):
        products = [Product('Pp12', 3), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(products.sort(key=attrgetter('price')), entries)

if __name__ == '__main__':
    unittest.main()