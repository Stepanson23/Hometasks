# 2. Class Exercise:
# Create a Python class representing a basic calculator with methods for addition,
# subtraction, multiplication, and division.

class Calculator:
    def gum(self, x, y):
        return x + y

    def han(self, x, y):
        return x - y

    def bazm(self, x, y):
        return x * y
    
    def baj(self, x, y):
        if y != 0:
            return x / y
        else:
            return False

calculator = Calculator()
print(calculator.gum(5,6))  