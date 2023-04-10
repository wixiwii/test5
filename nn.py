import random

class Encoder:
    def __init__(self, num):
        self.__num = num
        self.__encode()
        
    def __encode(self):
        operator = random.choice(['+', '-', '*', '/'])
        operand = random.randint(1, 10)
        
        if operator == '+':
            self.__num += operand
        elif operator == '-':
            self.__num -= operand
        elif operator == '*':
            self.__num *= operand
        else:
            self.__num //= operand
        
    def __str__(self):
        return str(self.__num)

num = 42
encoder = Encoder(num)
print(encoder)
