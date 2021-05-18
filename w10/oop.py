The class i.e. blueprint for my objects
class Person:

  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight
    self.energy = 100

person1 = Person("Peter", 35, 80)
person2 = Person("Ramona", 36, 60)
print(f"Person 1 is called {person1.name} and Person 2 is called {person2.name}. The combine weight of this 2 people is {person1.weight + person2.weight}")

