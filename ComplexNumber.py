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

    def __truediv__(self, other):
        if self.imaginary == 0 and other.imaginary == 0:
            real_part = self.real / other.real
            return ComplexNumber(real_part, 0)
        if self.real == 0 and other.real == 0:
            real_part = self.imaginary / other.imaginary
            return ComplexNumber(real_part, 0)
