class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_even_prozedurale(self):
        # Prozedurale Implementierung
        return [num for num in self.numbers if num % 2 == 0]

    def filter_even_funktionale(self):
        # Funktionale Implementierung
        return list(filter(lambda num: num % 2 == 0, self.numbers))

