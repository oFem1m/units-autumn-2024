import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(3, 5), 8)
        self.assertEqual(self.calculator.addition(-2, 2), 0)
        self.assertEqual(self.calculator.addition(0, -7), -7)
        self.assertTrue(math.isinf(self.calculator.addition(math.inf, -10)))
        self.assertTrue(math.isnan(self.calculator.addition(math.nan, -5)))

    def test_subtract(self):
        self.assertEqual(self.calculator.subtraction(20, 8), 12)
        self.assertEqual(self.calculator.subtraction(-3, 3), -6)
        self.assertEqual(self.calculator.subtraction(0, -9), 9)
        self.assertTrue(math.isinf(self.calculator.subtraction(math.inf, -3)))
        self.assertTrue(math.isnan(self.calculator.subtraction(math.nan, 2)))

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(6, 7), 42)
        self.assertEqual(self.calculator.multiplication(-2, 5), -10)
        self.assertEqual(self.calculator.multiplication(0, 123), 0)
        self.assertTrue(math.isinf(self.calculator.multiplication(math.inf, -1)))
        self.assertTrue(math.isnan(self.calculator.multiplication(math.nan, 3)))

    def test_divide(self):
        self.assertEqual(self.calculator.division(45, 9), 5)
        self.assertEqual(self.calculator.division(8, 2), 4)
        self.assertEqual(self.calculator.division(0, 7), 0)
        self.assertIsNone(self.calculator.division(9, 0))
        self.assertTrue(math.isinf(self.calculator.division(math.inf, -2)))
        self.assertTrue(math.isnan(self.calculator.division(3, math.nan)))

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-50), 50)
        self.assertEqual(self.calculator.absolute(20), 20)
        self.assertEqual(self.calculator.absolute(0), 0)
        self.assertTrue(math.isinf(self.calculator.absolute(math.inf)))
        self.assertTrue(math.isnan(self.calculator.absolute(math.nan)))

    def test_degree(self):
        self.assertEqual(self.calculator.degree(3, 3), 27)
        self.assertEqual(self.calculator.degree(10, 0), 1)
        self.assertEqual(self.calculator.degree(-3, 2), 9)
        self.assertTrue(math.isinf(self.calculator.degree(math.inf, 3)))
        self.assertTrue(math.isnan(self.calculator.degree(math.nan, 3)))

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(2), math.log(2))
        self.assertAlmostEqual(self.calculator.ln(10), math.log(10))
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)
        self.assertTrue(math.isinf(self.calculator.ln(math.inf)))
        self.assertTrue(math.isnan(self.calculator.ln(math.nan)))

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(1000, 10), 3)
        self.assertAlmostEqual(self.calculator.log(27, 3), 3)
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)
        self.assertTrue(math.isinf(self.calculator.log(math.inf, 2)))
        self.assertTrue(math.isnan(self.calculator.log(math.nan, 2)))

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(64), 8)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(3), math.sqrt(3))
        self.assertTrue(math.isinf(self.calculator.sqrt(math.inf)))
        self.assertTrue(math.isnan(self.calculator.sqrt(math.nan)))

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(343, 3), 7)
        self.assertAlmostEqual(self.calculator.nth_root(81, 4), 3)
        self.assertTrue(math.isinf(self.calculator.nth_root(math.inf, 4)))
        self.assertTrue(math.isnan(self.calculator.nth_root(math.nan, 4)))


if __name__ == "__main__":
    unittest.main()
