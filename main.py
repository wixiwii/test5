import random

class Person:
    def __init__(self, name, age, health=100, state="idle"):
        self.name = name
        self.age = age
        self.health = health
        self.state = state
        
    def __str__(self):
        return f"{self.name} ({self.age} year, health: {self.health}%, statistic: {self.state})"
    
    def work(self):
        self.state = "working"
        self.health -= random.randint(5, 15)
        if self.health <= 0:
            self.state = "death"
    
    def rest(self):
        self.state = "rest"
        self.health += random.randint(5, 15)
        if self.health > 100:
            self.health = 100

class Simulation:
    def __init__(self):
        self.people = []
    
    def add_person(self, person):
        self.people.append(person)
    
    def remove_person(self, person):
        self.people.remove(person)
    
    def run(self, days):
        for i in range(days):
            print(f"\nDay {i + 1}")
            for person in self.people:
                action = random.choice(["work", "rest"])
                if action == "work":
                    person.work()
                else:
                    person.rest()
                print(person)
