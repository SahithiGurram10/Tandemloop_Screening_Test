class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def operate(self, operation):
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Division by zero is not allowed"
        else:
            return "Invalid operation"

# Input
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
operation = input("Enter operation (add/subtract/multiply/divide): ").lower()

# Calculate
calc = Calculator(a, b)
result = calc.operate(operation)
print("Result:", result)
