from demo import Calculator


class Summation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute(self):
        return self.x + self.y

class Difference:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute(self):
        return self.x - self.y

class Product:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute(self):
        return self.x * self.y

class Quotient:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute(self):
        if self.y == 0:
            raise ValueError("Cannot divide by zero")
        return self.x / self.y

class Calculator:
    def __init__(self):
        pass

    def execute_operation(self, operation, x, y):
        if operation == 'summation':
            return Summation(x, y).compute()
        elif operation == 'difference':
            return Difference(x, y).compute()
        elif operation == 'product':
            return Product(x, y).compute()
        elif operation == 'quotient':
            return Quotient(x, y).compute()
        else:
            raise ValueError("Invalid operation")

if __name__ == "__main__":
    calc = Calculator()
    x = 50
    y = 2
    print("Summation:", calc.execute_operation('summation', x, y))
    print("Difference:", calc.execute_operation('difference', x, y))
    print("Product:", calc.execute_operation('product', x, y))
    print("Quotient:", calc.execute_operation('quotient', x, y))