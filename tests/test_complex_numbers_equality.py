import unittest
from ComplexNumber import ComplexNumber


class TestComplexNumbers(unittest.TestCase):
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

        complex_number_one = ComplexNumber(15, 12)
        complex_number_two = ComplexNumber(5, 5)
        complex_number_three = complex_number_one - complex_number_two

        assert complex_number_three.imaginary == 7

        complex_number_one = ComplexNumber(10, 18)
        complex_number_two = ComplexNumber(5, 5)
        complex_number_three = complex_number_one - complex_number_two

        assert complex_number_three.imaginary == 13

    def test_complex_numbers_multiplication(self):
        complex_number_one = ComplexNumber(2, 0)
        complex_number_two = ComplexNumber(1, 0)
        complex_number_three = complex_number_one * complex_number_two

        assert complex_number_three.real == 2

        complex_number_one = ComplexNumber(2, 0)
        complex_number_two = ComplexNumber(2, 0)
        complex_number_three = complex_number_one * complex_number_two

        assert complex_number_three.real == 4

        complex_number_one = ComplexNumber(0, 2)
        complex_number_two = ComplexNumber(0, 1)
        complex_number_three = complex_number_one * complex_number_two

        assert complex_number_three.imaginary == 0
        assert complex_number_three.real == -2

        complex_number_one = ComplexNumber(0, 2)
        complex_number_two = ComplexNumber(0, 1)
        complex_number_three = complex_number_one * complex_number_two

        assert complex_number_three.imaginary == 0
        assert complex_number_three.real == -2

        complex_number_one = ComplexNumber(5, 1)
        complex_number_two = ComplexNumber(2, 3)
        complex_number_three = complex_number_one * complex_number_two

        assert complex_number_three.imaginary == 17
        assert complex_number_three.real == 7

    def test_complex_number_real_part_division(self):
        complex_number_one = ComplexNumber(2, 0)
        complex_number_two = ComplexNumber(1, 0)
        complex_number_three = complex_number_one / complex_number_two

        assert complex_number_three.real == 2

        complex_number_one = ComplexNumber(3, 0)
        complex_number_two = ComplexNumber(1, 0)
        complex_number_three = complex_number_one / complex_number_two

        assert complex_number_three.real == 3

    def test_complex_number_imaginary_part_division(self):
        complex_number_one = ComplexNumber(0, 2)
        complex_number_two = ComplexNumber(0, 1)
        complex_number_three = complex_number_one / complex_number_two

        assert complex_number_three.real == 2

        complex_number_one = ComplexNumber(0, 6)
        complex_number_two = ComplexNumber(0, 2)
        complex_number_three = complex_number_one / complex_number_two

        assert complex_number_three.real == 3

    def test_complex_number_conjugate_real_part(self):
        complex_number_one = ComplexNumber(1, 0)
        conjugated_complex_number = complex_number_one.conjugate()
        assert conjugated_complex_number.real == 1

        complex_number_one = ComplexNumber(2, 0)
        conjugated_complex_number = complex_number_one.conjugate()
        assert conjugated_complex_number.real == 2

    def test_complex_number_conjugate_imaginary_part(self):
        complex_number_one = ComplexNumber(0, 2)
        conjugated_complex_number = complex_number_one.conjugate()
        assert conjugated_complex_number.imaginary == -2

        complex_number_one = ComplexNumber(0, -2)
        conjugated_complex_number = complex_number_one.conjugate()
        assert conjugated_complex_number.imaginary == 2

    def test_complex_number_conjugate_both_parts(self):
        complex_number_one = ComplexNumber(1, 2)
        conjugated_complex_number = complex_number_one.conjugate()
        assert conjugated_complex_number.imaginary == -2
        assert conjugated_complex_number.real == 1

        complex_number_one = ComplexNumber(3, 4)
        conjugated_complex_number = complex_number_one.conjugate()
        assert conjugated_complex_number.imaginary == -4
        assert conjugated_complex_number.real == 3

    def test_complex_number_division_both_parts(self):
        complex_number_one = ComplexNumber(1, 2)
        complex_number_two = ComplexNumber(1, 2)
        complex_number_three = complex_number_one / complex_number_two

        assert complex_number_three.real == 1
        assert complex_number_three.imaginary == 0

        complex_number_one = ComplexNumber(1, 5)
        complex_number_two = ComplexNumber(2, 1)
        complex_number_three = complex_number_one / complex_number_two

        assert complex_number_three.real == 1.4
        assert complex_number_three.imaginary == 1.8

    def test_complex_number_absolute_real_part(self):
        complex_number_one = ComplexNumber(1, 0)

        assert abs(complex_number_one) == 1

        complex_number_one = ComplexNumber(2, 0)

        assert abs(complex_number_one) == 2

    def test_complex_number_absolute_imaginary_part(self):
        complex_number_one = ComplexNumber(0, 1)

        assert abs(complex_number_one) == 1

        complex_number_one = ComplexNumber(0, 2)

        assert abs(complex_number_one) == 2

    def test_complex_number_absolute_both_parts(self):
        complex_number_one = ComplexNumber(1, 1)

        assert abs(complex_number_one) == 1.4142135623730951

        complex_number_one = ComplexNumber(3, 4)

        assert abs(complex_number_one) == 5

    def test_complex_number_phase_real_part(self):
        complex_number_one = ComplexNumber(1, 0)

        assert complex_number_one.phase() == 0
