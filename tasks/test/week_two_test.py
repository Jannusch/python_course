import unittest
import tasks.week_two.main as main

class TestOne(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(main.fibonacci(), 144)
    def test_fibonacci_1337(self):
        self.assertEqual(main.fibonacci_two(), 16)
    def test_means(self):
        self.assertEqual(main.means(), (1.3195152184758603, 6.9669296488698045, 4.1432224336728325))
    def test_classify(self):
        self.assertEqual(main.classify(), (106, 106))
    def test_threshold(self):
        # in theory we need first to run read_data().
        # no plan why not possible...
        self.assertEqual(main.threshold(), (106, 106))