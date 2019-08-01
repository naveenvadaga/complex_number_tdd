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

    def test_complex_numbers_addition(self):
        complex_number_one = ComplexNumber(0, 2)
        complex_number_two = ComplexNumber(1, 0)
        complex_number_three = complex_number_one + complex_number_two

        assert complex_number_three.real == 1

        complex_number_one = ComplexNumber(10, 2)
        complex_number_two = ComplexNumber(1, 0)
        complex_number_three = complex_number_one + complex_number_two

        assert complex_number_three.real == 11

        complex_number_one = ComplexNumber(10, 2)
        complex_number_two = ComplexNumber(1, 0)
        complex_number_three = complex_number_one + complex_number_two

        assert complex_number_three.imaginary == 2

        complex_number_one = ComplexNumber(10, 2)
        complex_number_two = ComplexNumber(1, 10)
        complex_number_three = complex_number_one + complex_number_two

        assert complex_number_three.imaginary == 12

    def test_complex_numbers_subtraction(self):
        complex_number_one = ComplexNumber(10, 2)
        complex_number_two = ComplexNumber(1, 0)
        complex_number_three = complex_number_one - complex_number_two

        assert complex_number_three.real == 9

        complex_number_one = ComplexNumber(15, 2)
        complex_number_two = ComplexNumber(5, 0)
        complex_number_three = complex_number_one - complex_number_two

        assert complex_number_three.real == 10
