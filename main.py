class Pet:
   def __init__(self, name, species):
       self.name = name
       self.species = species
       self.is_alive = True
       self.age = 0
   def grow(self):
       self.age += 1
cat = Pet("Kitty", "cat")
cat.grow()
print(f"{cat.name} grow up for {cat.age} year")

