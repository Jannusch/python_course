import unittest
import tasks.week_four.main as main


class ProblemOne(unittest.TestCase):

    def test_tets(self):
        self.assertEqual(main.check_solution_part_one_test(), 7)
    def test_problem(self):
        self.assertEqual(main.check_solution_part_one(), 1665)

class ProblemTwo(unittest.TestCase):
    def test_tets(self):
        self.assertEqual(main.check_solution_part_two_test(), 5)
    def test_problem(self):
        self.assertEqual(main.check_solution_part_two(), 1702)