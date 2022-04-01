apples = [20, 4, 5, 10, 15]

class Sorted:
    def __init__(self, items):
        self.data = items

    def heavier(self):
        self.data.sort()
        return self.data[-1]

    def get(self, index):
        return self.data[index]

def consumer1(cesta):
    """ Pega a maçã mais pesada."""
    s = Sorted(cesta)
    return s.heavier()

print(consumer1(apples))
