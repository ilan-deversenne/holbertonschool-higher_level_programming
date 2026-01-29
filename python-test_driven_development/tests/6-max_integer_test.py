#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test(self):
        ints = [0, 5, 10, 15, 8, 6]
        self.assertEqual(max_integer(ints), 15)
