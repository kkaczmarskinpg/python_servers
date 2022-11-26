import unittest
from collections import Counter
 
from servers import ListServer, Product, Client, MapServer, TooManyProductsFoundError
 
server_types = (ListServer, MapServer)
 
 
class ServerTest(unittest.TestCase):  
    def TooManyProductsFoundError_throw_test(self):
        products = [Product(f"PP{(a*2)*100+(a+3)*10+a+4}", a*7+a*2) for a in range(7)]
        for server_type in server_types:
            self.assertRaises(TooManyProductsFoundError,server_type(),self,products)

if __name__ == '__main__':
    unittest.main()
