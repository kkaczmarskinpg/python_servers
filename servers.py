#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Kacper Kaczmarski, 411814"""
"""Kacper Iwicki, 412027"""
"""Marceli Jach, nr albumu 409669"""
"""Marek Janaszkiewicz, nr albumu"""




from typing import Optional, List
from abc import ABC, abstractmethod
import re

class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)

    def __eq__(self, other):
        return None  # FIXME: zwróć odpowiednią wartość

    def __hash__(self):
        return hash((self.name, self.price))


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
    def get_entries(n_letters: int) -> List[Product]:
        raise NotImplementedError()

class ListServer (Server):
    def __init__(self,products: List[Product]):
        self.products = [Product(p.name,p.price) for p in products]
    def get_entries(self,n_letters) -> List[Product]:
        pattern = '^[a-zA-Z]{n}[0-9]{2,3}'.replace('n', str(n_letters))
        good_prods = [p for p in self.products if re.fullmatch(pattern, p.name)]
        if len(good_prods) > Server.n_max_returned_entries:
            raise TooManyProductsFoundError("Za dużo produktów kolego!", len(good_prods))
        return good_prods


class MapServer:
    pass


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()
