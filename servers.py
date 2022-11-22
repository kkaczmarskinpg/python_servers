#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Kacper Kaczmarski, 411814"""
"""Kacper Iwicki, 412027"""
"""Marceli Jach, nr albumu"""
"""Marek Janaszkiewicz, nr albumu"""




from typing import Optional, List
from abc import ABC, abstractmethod


class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)

    def __eq__(self, other):
        return None  # FIXME: zwróć odpowiednią wartość

    def __hash__(self):
        return hash((self.name, self.price))


class TooManyProductsFoundError(Exception):
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    def __init__(self, message: str, number_of_products: int):
        super().__init__(message)
        self.message = message
        self.number_of_products = number_of_products


# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania
class Server(ABC):
    n_max_returned_entries: int = 5

    @abstractmethod
    def get_entries(n_letters: int) -> List[Product]:
        raise NotImplementedError()


class ListServer:
    pass


class MapServer:
    pass


class Client:
    # DONE: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
    def __init__(self, server: Server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
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
