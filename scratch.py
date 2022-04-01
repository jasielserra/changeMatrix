apples = [20, 4, 5, 10, 15]

class Sorted:
    def __init__(self, items):
        self.data = items

    def sort(self):
        self.data.sort()

    def get(self, index):
        return self.data[index]

def consumer1(cesta):
    """ Pega a maçã mais pesada."""
    s = Sorted(cesta)
    s.sort()
    return s.get(-1)

print(consumer1(apples))
