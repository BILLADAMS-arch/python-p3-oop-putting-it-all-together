#!/usr/bin/env python3
import sys

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count
        self._author = ""
        self._genre = ""

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            
            print("page_count must be an integer", file=sys.stdout)

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    def summary(self):
        return f"{self.title} by {self.author}, {self.page_count} pages, Genre: {self.genre}"


    def turn_page(self):
        print("Flipping the page...wow, you read fast!", file=sys.stdout)
