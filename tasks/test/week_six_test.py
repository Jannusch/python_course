import unittest
import tasks.week_six.main_solution as main

class TestCar(unittest.TestCase):

    def test_acceleration(self):
        self.assertEqual(main.Car(500, 1500, 250, 5).calc_acceleration(), 5.555555555555555)
    def test_distance_per_time(self):
        self.assertEqual(main.Car(500, 1500, 250, 5).distance_per_time(1), 8.333333333333332)
    def test_distance_per_long_time(self):
        
        car = main.Car(500, 1500, 250, 5)
        s = 0
        for i in range(10):
            s += car.distance_per_time(1)
        print(s)    
        self.assertEqual(s, 1375.0)

