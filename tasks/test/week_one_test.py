import unittest
import tasks.week_one.main_solution as main
from math import factorial

class TestOne(unittest.TestCase):

    def test_1_arithmetic(self):
        self.assertEqual(main.simple_arithmetic(), 6.5)
    def test_2_volume(self):
        self.assertEqual(main.simple_volume(), (3375, 15))
    def test_3_volume_2(self):
        self.assertEqual(main.simple_volume_2(), 1000)
    def test_4_birthday(self):
        self.assertEqual(main.birthday(), (133225, factorial(365) / factorial(365 - 23), 0.4927027656760146, 0.5072972343239854))
    def test_5_advanced_arithmetic(self):
        self.assertEqual(main.advanced_arithmetic(), (5, 6.4031242374328485, 11, 184.28510520386612, 0.6875237736635218))