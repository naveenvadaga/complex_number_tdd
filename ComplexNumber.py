class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __sub__(self, other):
        real_part = self.real - other.real
        imaginary_part = self.imaginary - other.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + \
                         other.real * self.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def __truediv__(self, other):
        conjugate = other.conjugate()
        numerator = self * conjugate
        denominator = (other * conjugate).real
        real_part = numerator.real / denominator
        imaginary_part = numerator.imaginary / denominator
        return ComplexNumber(real_part, imaginary_part)

    def __abs__(self):
        import math
        return math.sqrt(
            self.real ** 2 + self.imaginary ** 2)

    def phase(self):
        if self.imaginary == 0:
            if self.real < 0:
                return 3.141592653589793
            else:
                return 0
        elif self.real == 0:
            return 1.5707963267948966
