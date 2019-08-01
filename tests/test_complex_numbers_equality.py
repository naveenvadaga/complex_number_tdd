import unittest
from ComplexNumber import ComplexNumber


class TestComplexNumbersEquality(unittest.TestCase):
    def test_complex_numbers_initialization(self):
        real_part = 1
        imaginary_part = 10
        assert ComplexNumber(real_part, imaginary_part).real == real_part
