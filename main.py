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

    def show(self):
        print(f"{self.numerator} / {self.denominator}")


fr = Fraction(4, 7)
fr1 = Fraction(2, 7)

fr.show()
fr1.show()

fr2 = fr + fr1

fr2.show()