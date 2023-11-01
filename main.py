class Fraction:
    numerator = None
    denominator = None

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)

        else:
            new_denominator = self.denominator * other.denominator
            new_numerator1 = self.numerator * other.denominator
            new_numerator2 = other.numerator * self.denominator

            return Fraction(new_numerator1 + new_numerator2, new_denominator)

    def __sub__(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)

        else:
            new_denominator = self.denominator * other.denominator
            new_numerator1 = self.numerator * other.denominator
            new_numerator2 = other.numerator * self.denominator

            return Fraction(new_numerator1 - new_numerator2, new_denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def short(self):
        i = 1
        while i <= self.numerator:
            if self.numerator % i == 0 and self.denominator % i == 0 and i != 1:
                self.numerator //= i
                self.denominator //= i

            elif self.numerator % i != 0 or self.denominator % i != 0 or i == 1:
                i += 1

    def show(self):
        print(f"{self.numerator} / {self.denominator}")


# fr = Fraction(4, 6)
# fr1 = Fraction(1, 3)
#
# fr.show()
# fr1.show()
#
# fr2 = fr / fr1
#
# fr2.show()

fr3 = Fraction(3, 9)

fr3.show()

fr3.short()

fr3.show()