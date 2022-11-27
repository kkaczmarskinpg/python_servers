import unittest
from collections import Counter
 
from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError
 
server_types = (ListServer, MapServer)
 
 
class ServerTest(unittest.TestCase):  
    def TooManyProductsFoundError_throw_test(self):
        products = [Product(f"PPP{(a)*100+(a+3)*10+a+4}", a*3) for a in range(1,11)] + [Product(f"PP{(a)*100+(a+6)*10+a+1}", a*2) for a in range(1,11)]
        for server_type in server_types:
            server = server_type(products)
            self.assertRaises(TooManyProductsFoundError,server.get_entries(),3)

if __name__ == '__main__':
    unittest.main()

