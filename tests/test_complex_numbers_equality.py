import unittest
from ComplexNumber import ComplexNumber


class TestComplexNumbersEquality(unittest.TestCase):
    def test_complex_numbers_initialization(self):
        real_part = 1
        imaginary_part = 10
        assert ComplexNumber(real_part, imaginary_part).real == real_part
        assert ComplexNumber(real_part,
                             imaginary_part).imaginary == imaginary_part
        real_part = 10
        imaginary_part = 10

        assert ComplexNumber(real_part, imaginary_part).real == real_part
        assert ComplexNumber(real_part,
                             imaginary_part).imaginary == imaginary_part
        real_part = 13
        imaginary_part = -1

        assert ComplexNumber(real_part, imaginary_part).real == real_part
        assert ComplexNumber(real_part,
                             imaginary_part).imaginary == imaginary_part

    def test_two_complex_numbers_equality(self):
        complex_number_1 = ComplexNumber(1, 2)
        complex_number_2 = ComplexNumber(1, 2)

        assert complex_number_1 == complex_number_2

        complex_number_1 = ComplexNumber(2, 4)
        complex_number_2 = ComplexNumber(-2, 4)

        assert complex_number_1 != complex_number_2

        complex_number_1 = ComplexNumber(2, 4)
        complex_number_2 = ComplexNumber(2, -4)

        assert complex_number_1 != complex_number_2
