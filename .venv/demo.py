class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b

class Subtraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a - self.b

class Multiplication:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a * self.b

class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

class Calculator:
    def __init__(self):
        pass

    def perform_operation(self, operation, a, b):
        if operation == 'addition':
            return Addition(a, b).calculate()
        elif operation == 'subtraction':
            return Subtraction(a, b).calculate()
        elif operation == 'multiplication':
            return Multiplication(a, b).calculate() 