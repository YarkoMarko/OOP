from datetime import datetime as d


class Auto:
    def __str__(self):
        return f"Name: {self._name}\nDate of release: {self._date}\nMighty: {self._mighty}\nPrice: {self._price}"

    def __lt__(self, other):
        return self.get_mighty() < other.get_mighty()

    def __le__(self, other):
        return self.get_mighty() <= other.get_mighty()

    def __gt__(self, other):
        return self.get_mighty() > other.get_mighty()

    def __ge__(self, other):
        return self.get_mighty() >= other.get_mighty()


class Porsche(Auto):
    def __init__(self, name, date, mighty, price):
        self._name = name
        self._date = date
        self._mighty = mighty
        self._price = price


p = Porsche("Porsche", d.strptime("05/12/1999", "%d/%m/%Y"), 12000, 120000)

print(p)