apples = [20, 4, 5, 10, 15]

class Sorted:
    def __init__(self, items):
        self.data = items

    def heavier(self):
        return max(self.data)

    def get(self, index):
        return self.data[index]

def consumer1(cesta):
    """ Pega a maçã mais pesada."""
    s = Sorted(cesta)
    return s.head()

print(consumer1(apples))
