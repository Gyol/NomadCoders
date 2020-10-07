def say_hello(your_name, age):
    print(f'Hello {your_name} you are {age} years old')

say_hello('Gyol', 27)

class Calculator:
    def __init__(self, number, by_what):
        self.number = number
        self.by_what = by_what

    def plus(self):
        plus = self.number + self.by_what
        return plus

    def minus(self):
        minus = self.number - self.by_what
        return minus


number = Calculator(2, 5)

print(number.plus())
print(number.minus())
