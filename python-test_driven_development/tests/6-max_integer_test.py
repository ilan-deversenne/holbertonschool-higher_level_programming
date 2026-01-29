#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test(self):
        ints = [60, 6, 20, 9, 3, 8, 42]
        self.assertEqual(max_integer(ints), 60)

    def test2(self):
        ints = [0, 5, 10, 15, 8, 6]
        self.assertEqual(max_integer(ints), 15)

    def test3(self):
        ints = [5, 10, 8, 2, 40]
        self.assertEqual(max_integer(ints), 40)

    def test4(self):
        ints = [5, 8, 12, 18, -22]
        self.assertEqual(max_integer(ints), 18)

    def test5(self):
        ints = [-5, -10, -8, -2, -40]
        self.assertEqual(max_integer(ints), -2)

    def test6(self):
        ints = [30]
        self.assertEqual(max_integer(ints), 30)

    def test7(self):
        ints = []
        self.assertEqual(max_integer(ints), None)
