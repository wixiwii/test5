def my_decorator(func):
    def wrapper():
        print("Сейчас что то случится")
        func()
        print("Сейчас что то случится")
    return wrapper

@my_decorator
def say_hello():
    print("привет!")

say_hello()
