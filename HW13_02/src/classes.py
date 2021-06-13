class Math:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add_func(self):
        return self.n1 + self.n2

    def substraction_func(self):
        return self.n1 - self.n2

    def mult_func(self):
        return round(self.n1 * self.n2, 4)

    def division_func(self):
        try:
            return round(self.n1 / self.n2, 4)
        except ZeroDivisionError:
            print('Cannot divide by zero')
