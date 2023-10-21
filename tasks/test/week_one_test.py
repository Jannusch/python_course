import unittest
import tasks.week_one.main as main
from math import factorial

class TestOne(unittest.TestCase):

    def test_arithmetic(self):
        self.assertEqual(main.simple_arithmetic(), 6.5)#
    def test_volume(self):
        self.assertEqual(main.simple_volume(), (3375, 15))
    def test_volume_2(self):
        self.assertEqual(main.simple_volume_2(), 1000)
    def test_birthday(self):
        self.assertEqual(main.birthday(), (133225, factorial(365) / factorial(365 - 23), 0.4927027656760146, 0.5072972343239854))