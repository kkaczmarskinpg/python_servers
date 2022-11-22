#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Kacper Kaczmarski, 411814"""
"""Kacper Iwicki, nr albumu"""
"""Marceli Jach, nr albumu"""
"""Marek Janaszkiewicz, 411925"""
 

from typing import Optional, Dict, List
import re
from abc import abstractmethod
 
class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    pass
 
class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass
 
 
# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania
class Server:
    n_max_returned_entries = 5

    @abstractmethod
    def get_entries(self,n_letters):
        return NotImplementedError()
class ListServer:
    pass
 
class MapServer (Server):
    def __init__(self,products:Dict[str:int]):
        self.products = [Product(p,products[p]) for p in products]


    def get_entries(self,n_letters):
        expression = '^[a-zA-Z]{1,n_letters}[0-9]{2,3}$'.replace('n_letters', str(n_letters))
        for product in self.products:
            list_of_products = []
            if re.fullmatch(expression,product.name):
                list_of_products.append(product)
                if len(list_of_products) > Server.n_max_returned_entries:
                    return TooManyProductsFoundError('Za dużo produktów kolego',len(list_of_products))
        return list_of_products
 
 
class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
 
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()