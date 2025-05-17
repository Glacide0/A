import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 5), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        self.assertEqual(self.calc.divide(-1, 1), -1)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(2, -1), 0.5)
        self.assertEqual(self.calc.power(-2, 2), 4)
        self.assertEqual(self.calc.power(-2, 3), -8)
    
    def test_square_root(self):
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertAlmostEqual(self.calc.square_root(2), 1.4142135623730951)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(8, 4), 0)
        self.assertEqual(self.calc.modulo(-7, 3), 2)
        with self.assertRaises(ValueError):
            self.calc.modulo(5, 0)
    
    def test_floor_division(self):
        self.assertEqual(self.calc.floor_division(7, 3), 2)
        self.assertEqual(self.calc.floor_division(8, 4), 2)
        self.assertEqual(self.calc.floor_division(-7, 3), -3)
        with self.assertRaises(ValueError):
            self.calc.floor_division(5, 0)

if __name__ == "__main__":
    unittest.main()