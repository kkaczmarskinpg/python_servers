#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Kacper Kaczmarski, 411814"""
"""Kacper Iwicki, 412027"""
"""Marceli Jach, 409669"""
"""Marek Janaszkiewicz, 411925"""




from typing import Optional, List, Dict
from abc import ABC, abstractmethod
from operator import attrgetter
import re
class Product:
    # Done: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    def __init__(self, name: str, price: float):
        if re.match(r"^[a-zA-Z]{1,}\d{1,}$", name) is not None:
            self.name: str = name
            self.price: float = price
        else:
            raise ValueError(
                "Nazwa musi składać się z conajmniej jednej litery i cyfry!")

    def __eq__(self, other) -> bool:
        if self.name == other.name and self.price == other.price:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.name, self.price))


class TooManyProductsFoundError(Exception):
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    def __init__(self, message: str, number_of_products: int):
        super().__init__(message)
        self.message = message
        self.number_of_products = number_of_products


# Done: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania
class Server(ABC):
    n_max_returned_entries: int = 5

    @abstractmethod
    def get_entries(n_letters: int) -> List[Product]:
        raise NotImplementedError()


class ListServer(Server):
    def __init__(self, products: List[Product]):
        self.products = [Product(p.name, p.price) for p in products]

    def get_entries(self, n_letters) -> List[Product]:
        pattern = '^[a-zA-Z]{n}[0-9]{2,3}'.replace('n', str(n_letters))
        good_prods = [
            p for p in self.products if re.fullmatch(pattern, p.name)]
        if len(good_prods) > Server.n_max_returned_entries:
            raise TooManyProductsFoundError(
                "Za dużo produktów kolego!", len(good_prods))
        good_prods.sort(key=attrgetter('price'))
        return good_prods


class MapServer(Server):
    def __init__(self, products: List[Product]):
        self.products = {p.name: p for p in products}

    def get_entries(self, n_letters):
        expression = '^[a-zA-Z]{n_letters}[0-9]{2,3}$'.replace(
            'n_letters', str(n_letters))
        list_of_products = []
        for product in self.products:
            if re.fullmatch(expression, product):
                list_of_products.append(self.products[product])
        if len(list_of_products) > Server.n_max_returned_entries:
            raise TooManyProductsFoundError(
                'Za dużo produktów kolego!', len(list_of_products))
        list_of_products.sort(key=attrgetter('price'))
        return list_of_products


class Client:
    # DONE: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, server: Server):
        self.server = server

    def get_total_price(self, n_letters: int) -> Optional[float]:
        try:
            products = self.server.get_entries(n_letters)
        except TooManyProductsFoundError as e:
            print(e.message)
            return None
        if not products:
            return None
        sum = 0
        for p in products:
            sum += p.price
        return sum
