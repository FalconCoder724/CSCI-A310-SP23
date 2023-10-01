class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return None
    def __str__(self):
        return "(" + self.makeSound() + ")"
    def makeSound(self):
        return self.a + ", " + self.b

class Fraction(Pair):
    def __init__(self, num, denom):
        super().__init__(num, denom)
    def __add__(self, other):
        a = self.a * other.b + self.b * other.a
        b = self.b * other.b
        return Fraction(a, b)
    def makeSound(self):
        return str(self.a) + " / " + str(self.b)
    

a = Fraction(1, 2)
b = Fraction(1, 2)
c = a + b
print(str(a) + " + " + str(b) + " = " + str(c))
# (1 / 2) + (1 / 2) = (4 / 4)


class Complex(Pair):
    def __init__(self, real, imag):
        super().__init__(real, imag)
    def __add__(self, other):
        a = self.a + other.a
        b = self.b * other.b
        return Complex(a, b)
    def makeSound(self):
        return str(self.a) + " + i * " + str(self.b)

a = Complex(1, 2)
b = Complex(1, -2)
c = a + b
print(str(a) + " + " + str(b) + " = " + str(c))
# (1 + i * 1) + (1 + i * -2) = (2 + i * -1)
