#!/usr/bin/env python3
import sys

class Shoe:
    def __init__(self, brand="", size=0, color="", price=0.0):
        self._brand = brand
        self._size = size
        self._color = color
        self._price = price
        self._condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._size = value
        else:
            print("size must be an integer", file=sys.stdout)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = value
        else:
            raise ValueError("price must be a non-negative number")

    @property
    def condition(self):
        return self._condition

    def description(self):
        return f"{self.color.capitalize()} {self.brand} shoe, size {self.size}, priced at ${self.price:.2f}, condition: {self.condition}"

    def cobble(self):
        self._condition = "New" 
        print("Your shoe is as good as new!", file=sys.stdout)
