#!/bin/env python3

import unittest
from decimalMatch import decimalMatch

class TestStringMethods(unittest.TestCase):

    def test_book(self):
        a = decimalMatch()

        a.appendToList("booaa")
        a.appendToList("book")

        self.assertEqual(set(a.findInList("2151511")), set(['BOOAA', 'BOOK']))

    def test_books(self):
        a = decimalMatch()

        a.appendToList("books")

        self.assertEqual(a.findInList("215151119"), ['BOOKS'])

    def test_flower(self):
        a = decimalMatch()

        a.appendToList("FLOWER")

        self.assertEqual(a.findInList("6121523518"), ['FLOWER'])

    def test_city(self):
        a = decimalMatch()

        a.appendToList("CiTy")

        self.assertEqual(a.findInList("392025"), ['CITY'])

    def test_ghfyt(self):
        a = decimalMatch()

        a.appendToList("Ghfyt")

        self.assertEqual(a.findInList("7862520"), ['GHFYT'])

if __name__ == '__main__':
    unittest.main()
