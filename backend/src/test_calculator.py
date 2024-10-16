import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # Тесты для сложения
    def test_add_positive_numbers(self):
        self.assertEqual(self.calculator.addition(3, 5), 8)

    def test_add_negative_and_positive_numbers(self):
        self.assertEqual(self.calculator.addition(-2, 2), 0)

    def test_add_floating_point_numbers(self):
        self.assertAlmostEqual(self.calculator.addition(3.2, 5.1), 8.3)

    def test_add_with_zero(self):
        self.assertEqual(self.calculator.addition(0, -7), -7)

    def test_add_with_infinity(self):
        self.assertTrue(math.isinf(self.calculator.addition(math.inf, -10)))

    def test_add_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.addition(math.nan, -5)))

    def test_add_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.addition("abc", 5)

    def test_add_strings(self):
        self.assertEqual(self.calculator.addition("3", "5"), "35")

    # Тесты для вычитания
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calculator.subtraction(20, 8), 12)

    def test_subtract_negative_and_positive_numbers(self):
        self.assertEqual(self.calculator.subtraction(-3, 3), -6)

    def test_subtract_floating_point_numbers(self):
        self.assertAlmostEqual(self.calculator.subtraction(10.5, 3.2), 7.3)

    def test_subtract_with_zero(self):
        self.assertEqual(self.calculator.subtraction(0, -9), 9)

    def test_subtract_with_infinity(self):
        self.assertTrue(math.isinf(self.calculator.subtraction(math.inf, -3)))

    def test_subtract_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(math.nan, 2)))

    def test_subtract_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction("xyz", 10)

    def test_subtract_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction("10", "3")

    # Тесты для умножения
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calculator.multiplication(6, 7), 42)

    def test_multiply_negative_and_positive_numbers(self):
        self.assertEqual(self.calculator.multiplication(-2, 5), -10)

    def test_multiply_floating_point_numbers(self):
        self.assertAlmostEqual(self.calculator.multiplication(2.5, 4.2), 10.5)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 123), 0)

    def test_multiply_with_infinity(self):
        self.assertTrue(math.isinf(self.calculator.multiplication(math.inf, -1)))

    def test_multiply_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.multiplication(math.nan, 3)))

    def test_multiply_invalid_data_type(self):
        self.assertEqual(self.calculator.multiplication("a", 2), "aa")

    def test_multiply_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication("4", "2")

    # Тесты для деления
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calculator.division(45, 9), 5)

    def test_divide_floating_point_numbers(self):
        self.assertAlmostEqual(self.calculator.division(7.5, 2.5), 3.0)

    def test_divide_with_repeating_decimal(self):
        self.assertAlmostEqual(self.calculator.division(10, 3), 3.333333, places=6)

    def test_divide_with_zero_numerator(self):
        self.assertEqual(self.calculator.division(0, 7), 0)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calculator.division(9, 0))

    def test_divide_with_infinity(self):
        self.assertTrue(math.isinf(self.calculator.division(math.inf, -2)))

    def test_divide_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.division(3, math.nan)))

    def test_divide_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.division(10, "abc")

    def test_divide_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.division("8", "2")

    # Тесты для взятия модуля
    def test_absolute_negative_number(self):
        self.assertEqual(self.calculator.absolute(-50), 50)

    def test_absolute_positive_number(self):
        self.assertEqual(self.calculator.absolute(20), 20)

    def test_absolute_with_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_with_infinity(self):
        self.assertTrue(math.isinf(self.calculator.absolute(math.inf)))

    def test_absolute_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.absolute(math.nan)))

    def test_absolute_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.absolute("negative")

    # Тесты для степени
    def test_degree_positive_numbers(self):
        self.assertEqual(self.calculator.degree(3, 3), 27)

    def test_degree_floating_point_numbers(self):
        self.assertAlmostEqual(self.calculator.degree(2.5, 2), 6.25)

    def test_degree_with_zero_exponent(self):
        self.assertEqual(self.calculator.degree(10, 0), 1)

    def test_degree_negative_base(self):
        self.assertEqual(self.calculator.degree(-3, 2), 9)

    def test_degree_with_infinity(self):
        self.assertTrue(math.isinf(self.calculator.degree(math.inf, 3)))

    def test_degree_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.degree(math.nan, 3)))

    def test_degree_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.degree("3", 2)

    def test_degree_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.degree("3", "2")

    # Тесты для ln
    def test_ln_positive_number(self):
        self.assertAlmostEqual(self.calculator.ln(2), math.log(2))

    def test_ln_with_inf(self):
        self.assertTrue(math.isinf(self.calculator.ln(math.inf)))

    def test_ln_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.ln(math.nan)))

    def test_ln_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.ln("test")

    def test_ln_with_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    # Тесты для log
    def test_log_base_10(self):
        self.assertAlmostEqual(self.calculator.log(1000, 10), 3)

    def test_log_with_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)

    def test_log_with_inf(self):
        self.assertTrue(math.isinf(self.calculator.log(math.inf, 2)))

    def test_log_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.log(math.nan, 2)))

    def test_log_with_negative_number(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-1, 2)

    def test_log_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.log("test", 2)

    def test_log_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.log("test", "2")

    # Тесты для sqrt
    def test_sqrt_positive_number(self):
        self.assertEqual(self.calculator.sqrt(64), 8)

    def test_sqrt_floating_point_number(self):
        self.assertAlmostEqual(self.calculator.sqrt(6.25), 2.5)

    def test_sqrt_with_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_with_inf(self):
        self.assertTrue(math.isinf(self.calculator.sqrt(math.inf)))

    def test_sqrt_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.sqrt(math.nan)))

    def test_sqrt_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt("test")

    # Тесты для nth_root
    def test_nth_root_positive_number(self):
        self.assertAlmostEqual(self.calculator.nth_root(343, 3), 7)

    def test_nth_root_with_inf(self):
        self.assertTrue(math.isinf(self.calculator.nth_root(math.inf, 4)))

    def test_nth_root_with_nan(self):
        self.assertTrue(math.isnan(self.calculator.nth_root(math.nan, 4)))

    def test_nth_root_invalid_data_type(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root("test", 3)

    def test_nth_root_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root("test", "2")


if __name__ == "__main__":
    unittest.main()
