import datetime as d


class Stadium:
    def __str__(self):
        return f"Name: {self._name}\nDate: {self._date}\nCountry: {self._country}\nTown: {self._town}\nCapacity: {self._capacity}"

    def __lt__(self, other):
        return self.get_capacity() < other.get_capacity()

    def get_capacity(self):
        return self._capacity

class OldTrafford(Stadium):
    def __init__(self):
        Stadium.__init__(self)
        self._name = "Old Trafford"
        self._date = d.datetime.strptime("19/02/1910", "%d/%m/%Y")
        self._country = "England"
        self._town = "Manchester"
        self._capacity = 74310


tr = OldTrafford()

print(tr)


