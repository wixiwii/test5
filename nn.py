class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")

class Learner:
    def __init__(self, school, grade):
        self.school = school
        self.grade = grade

    def study(self):
        print("I am studying.")

class Student(Person, Learner):
    def __init__(self, name, age, gender, school, grade):
        Person.__init__(self, name, age, gender)
        Learner.__init__(self, school, grade)

    def say_hello(self):
        Person.say_hello(self)
        print(f"I go to {self.school} and I am in grade {self.grade}.")

    def do_homework(self):
        print("I am doing homework.")
