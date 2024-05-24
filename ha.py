from demo import Calculator


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
        elif operation == 'division':
            return Division(a, b).calculate()
        else:
            raise ValueError("Invalid operation")

    if __name__ == "__main__":
        calc = Calculator()
    a = 50
    b = 2
    print("Addition:", calc.perform_operation('addition', a,
                                              b))
    print("Subtraction:", calc.perform_operation('subtraction',
                                                 a, b))
    print("Multiplication:",
          calc.perform_operation('multiplication', a, b))
    print("Division:", calc.perform_operation('division', a,
                                              b))