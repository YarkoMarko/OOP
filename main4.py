from datetime import datetime as d

class Book:
    def __str__(self):
        return f"Name: {self._name}\nDate of release: {self._date}\nAmount of pages: {self._amount}\nPrice: {self._price}"

    def __lt__(self, other):
        return self.get_amount() < other.get_amount()

    def __le__(self, other):
        return self.get_amount() <= other.get_amount()

    def __gt__(self, other):
        return self.get_amount() > other.get_amount()

    def __ge__(self, other):
        return self.get_amount() >= other.get_amount()


class HarryPotter(Book):
    def __init__(self, name, date, amount, price):
        self._name = name
        self._date = date
        self._amount = amount
        self._price = price


h = HarryPotter("Harry Potter", d.strptime("03/10/1996", "%d/%m/%Y"), 230, 99)

print(h)
