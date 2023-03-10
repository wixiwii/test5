import random

class Encryptor:
    def __init__(self, num):
        self.num = num
        self.__encrypt()

    def __encrypt(self):
        operation = random.choice(["+", "-", "*", "/"])
        if operation == "+":
            self.num += random.randint(1, 10)
        elif operation == "-":
            self.num -= random.randint(1, 10)
        elif operation == "*":
            self.num *= random.randint(1, 5)
        elif operation == "/":
            self.num /= random.randint(1, 5)

    def __str__(self):
        return str(self.num)